"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""
import time


def collatz_length(n):
    n_steps = 0
    start_n = n
    while True:
        # invariant if n in COLLATZ_LENGTH_CACHE then
        # COLLATZ_LENGTH_CACHE[n] is length of collatz sequence
        # and n_steps is the number of steps -1 taken so far
        if n in COLLATZ_LENGTH_CACHE:
            n_steps += COLLATZ_LENGTH_CACHE[n]
            break
        if n % 2 == 0:
            n_steps += 1
            n = n // 2
        else:
            n_steps += 2
            n = (3*n+1) // 2
    COLLATZ_LENGTH_CACHE[start_n] = n_steps
    return n_steps


if __name__ == '__main__':
    start_time = time.time()
    COLLATZ_LENGTH_CACHE = {
        1: 1
    }
    max_steps = 0
    max_val = 0
    print(collatz_length(1))
    for n in range(10**6//2, 10**6+1):
        steps = collatz_length(n)
        if steps > max_steps:
            max_steps = steps
            max_val = n
        #print(TOTAL_STEPS)
    print(max_val, max_steps)
    end_time = time.time()
    print(end_time-start_time)
