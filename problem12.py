"""
The sequence of triangle numbers is generated by adding the natural numbers. So
the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten
terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""
import collections


def prime_decomposition(n):
    """Return list of prime factors of n."""
    max_test = int(n**0.5)
    prime_list = collections.defaultdict(int)
    for factor in [2, 3]:
        while n % factor == 0:
            prime_list[factor] += 1
            n = n // factor

    factor = 5  # do 6k+/-1
    while factor < max_test:
        if n == 1:
            break
        while n % factor == 0:
            prime_list[factor] += 1
            n = n // factor

        while n % (factor+2) == 0:
            prime_list[factor+2] += 1
            n = n // (factor+2)
        factor += 6

    if n != 1:
        prime_list[n] += 1

    return prime_list


def n_factors(n):
    if n == 1:
        return 1
    if n in n_factors.cache:
        return n_factors.cache[n]
    prime_count = iter(prime_decomposition(n).values())
    count = 1+next(prime_count)
    for x in prime_count:
        count *= 1+x
    n_factors.cache[n] = count
    return count


if __name__ == '__main__':
    n_factors.cache = {}
    n = 3
    last_prime_decomp = prime_decomposition(n)
    while True:
        tri_n = n*(n+1)/2
        cur_prime_decom = prime_decomposition(n+1)
        total_prime_decom = last_prime_decomp.copy()
        for val, count in cur_prime_decom.items():
            total_prime_decom[val] += count
        total_prime_decom[2] -= 1
        n_factors = 1
        for count in total_prime_decom.values():
            n_factors *= (count+1)
        last_prime_decomp = cur_prime_decom
        if n_factors > 500:
            print('%d %d %s' % (tri_n, n_factors, total_prime_decom))
            break
        n += 1
