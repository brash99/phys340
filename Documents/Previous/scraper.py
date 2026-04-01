import csv
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_SEARCH_URL = "https://link.springer.com/search"
PARAMS = {
    "query": "LLM",
    "content-type": "Article",
    "sortBy": "relevance",
    "search-within": "Journal",
    "facet-journal-id": "13347",
    "page": 1,
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}

SESSION = requests.Session()
SESSION.headers.update(HEADERS)


def get_soup(url, params=None):
    resp = SESSION.get(url, params=params, timeout=30)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def extract_results_from_search_page(soup):
    results = []

    # Springer search results usually live in li.app-card-open or article/app-card blocks.
    cards = soup.select("li.app-card-open, article.c-card, div.app-card-open")
    if not cards:
        # fallback: look for article title links directly
        for a in soup.select("a[href*='/article/']"):
            title = a.get_text(" ", strip=True)
            href = a.get("href")
            if title and href:
                results.append({
                    "title": title,
                    "url": urljoin("https://link.springer.com", href)
                })
        # deduplicate
        seen = set()
        deduped = []
        for r in results:
            if r["url"] not in seen:
                deduped.append(r)
                seen.add(r["url"])
        return deduped

    for card in cards:
        a = card.select_one("a[href*='/article/']")
        if not a:
            continue
        title = a.get_text(" ", strip=True)
        href = a.get("href")
        if title and href:
            results.append({
                "title": title,
                "url": urljoin("https://link.springer.com", href)
            })

    # deduplicate
    seen = set()
    deduped = []
    for r in results:
        if r["url"] not in seen:
            deduped.append(r)
            seen.add(r["url"])
    return deduped


def extract_abstract(article_url):
    try:
        soup = get_soup(article_url)
    except Exception as e:
        return f"[ERROR fetching article: {e}]"

    # Common Springer abstract containers
    selectors = [
        "section#Abs1",
        "section.Abstract",
        "div.c-article-section__content",
        "div#Abs1-content",
        "section[data-title='Abstract']",
    ]

    for sel in selectors:
        node = soup.select_one(sel)
        if node:
            text = node.get_text(" ", strip=True)
            if text:
                return text

    # Fallback: look for heading with "Abstract"
    for heading in soup.find_all(["h2", "h3"]):
        if "abstract" in heading.get_text(" ", strip=True).lower():
            parent = heading.parent
            if parent:
                text = parent.get_text(" ", strip=True)
                if text:
                    return text

    return "[ABSTRACT NOT FOUND]"


def scrape_all_pages(max_pages=5, delay_seconds=1.5):
    all_results = []

    for page in range(1, max_pages + 1):
        print(f"Scraping search page {page}...")
        params = PARAMS.copy()
        params["page"] = page
        soup = get_soup(BASE_SEARCH_URL, params=params)

        page_results = extract_results_from_search_page(soup)
        if not page_results:
            print("No more results found.")
            break

        print(f"  Found {len(page_results)} article links on page {page}")

        for i, item in enumerate(page_results, start=1):
            print(f"    [{i}/{len(page_results)}] Fetching abstract for: {item['title']}")
            abstract = extract_abstract(item["url"])
            item["abstract"] = abstract
            all_results.append(item)
            time.sleep(delay_seconds)

        time.sleep(delay_seconds)

    return all_results


def save_to_csv(rows, filename="springer_llm_pt_articles.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "url", "abstract"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved {len(rows)} rows to {filename}")


if __name__ == "__main__":
    rows = scrape_all_pages(max_pages=10, delay_seconds=1.5)
    save_to_csv(rows)