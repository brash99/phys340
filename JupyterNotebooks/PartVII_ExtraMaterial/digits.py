import numpy as np

for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            lhs = 5*a*b*c
            rhs = 100*a + 10*b + c
            if lhs == rhs:
                print(f"{a} {b} {c}")