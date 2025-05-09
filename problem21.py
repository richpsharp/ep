"""
<p>Let $d(n)$ be defined as the sum of proper divisors of $n$ (numbers less than $n$ which divide evenly into $n$).<br>
If $d(a) = b$ and $d(b) = a$, where $a \ne b$, then $a$ and $b$ are an amicable pair and each of $a$ and $b$ are called amicable numbers.</p>
<p>For example, the proper divisors of $220$ are $1, 2, 4, 5, 10, 11, 20, 22, 44, 55$ and $110$; therefore $d(220) = 284$. The proper divisors of $284$ are $1, 2, 4, 71$ and $142$; so $d(284) = 220$.</p>
<p>Evaluate the sum of all the amicable numbers under $10000$.</p>
"""

import collections
import math
import time

start = time.time()

prime_factors = collections.defaultdict(list)
sum_of_factors = {}
for val in reversed(range(10000)):
    remaining_val = val
    local_prime_factors = []
    while True:
        if remaining_val in prime_factors:
            local_prime_factors += prime_factors[remaining_val]
            break
        upper_test = math.floor(math.sqrt(remaining_val))
        found = False
        for test in range(2, math.floor(math.sqrt(remaining_val))):
            if remaining_val % test == 0:
                local_prime_factors.append(test)
                remaining_val //= test
                found = True
                break
        if not found:
            # last prime
            local_prime_factors.append(remaining_val)
            prime_factors[remaining_val] = local_prime_factors
            factor_sum = sum(prime_factors[remaining_val])
            sum_of_factors[sum(prime_factors[remaining_val])] = val
            if sum_of_factors[val] == factor_sum if val in sum_of_factors:
                print()
            break
    # print(f"the prime factors of {val} are {local_prime_factors}")
print(f"done in {time.time()-start:.4f}s")
