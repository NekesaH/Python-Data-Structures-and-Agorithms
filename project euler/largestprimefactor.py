def get_prime_factors(n):
    prime_factors = []
    div = 2
    while div <= n:
        if n % div == 0:
            prime_factors.append(div)
            n = n / div
        else:
            div += 1

    return max(prime_factors)
