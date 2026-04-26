import numpy as np
import matplotlib.pyplot as plt

n_sims = 100000
n_true_correct = 7
round_up = 8
round_up_flag = True

known_number_of_true_values = True

mean_correct = []
error_correct = []
for n_guess in range(11):
    guess_history = []

    for i in range(n_sims):
        # Generate some random data for true and false values - 10 initial values
        # true_values = np.random.choice([True, False], size=10)

        # Generate an array of true values with 10 values, n_true = 7, and the rest false
        if known_number_of_true_values:
            n_true = n_true_correct
            true_values = np.array([True] * n_true + [False] * (10 - n_true))
            np.random.shuffle(true_values)
        else:
            # choose randomly
            true_values = np.random.choice([True, False], size=10)

        # Generate an array of guesses with 10 values, and n_true = n_guess true values
        n_true = n_guess
        guesses = np.array([True] * n_true + [False] * (10 - n_true))
        np.random.shuffle(guesses)

        # print the true values and guesses for debugging
        #print(f"True Values: {true_values}")
        #print(f"Guesses: {guesses}")

        # Calculate the number of correct guesses
        correct_guesses = np.sum(true_values == guesses)

        if round_up_flag:
            if (correct_guesses < round_up):
                correct_guesses = round_up
        #print(f"Correct Guesses: {correct_guesses}")
        guess_history.append(correct_guesses)

    # Histogram of correct guesses
    #plt.hist(guess_history, bins=np.arange(-0.5, 10.5, 1), edgecolor='black')
    #plt.title('Distribution of Correct Guesses')
    #plt.xlabel('Number of Correct Guesses')
    #plt.ylabel('Frequency')
    #plt.xticks(np.arange(0, 11, 1))
    #plt.grid(axis='y', alpha=0.75)
    #plt.show()

    mean_correct.append(np.mean(guess_history))
    error_correct.append(np.std(guess_history)/np.sqrt(n_sims))

# Plot mean correct guesses vs n_guess
plt.errorbar(range(11), mean_correct, error_correct,marker='o', label=(f'Round Up to {round_up} Enabled' if round_up_flag else 'Round Up Disabled'))
plt.title('Mean Number of Correct Guesses vs Number of True Guesses')
plt.xlabel('Number of True Guesses (n_guess)')
plt.ylabel('Mean Number of Correct Guesses')
plt.xticks(range(11))
plt.legend()
plt.grid()
plt.show()