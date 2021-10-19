# def prime(n):
#     for y in range(2, n+1):
#         if n % y == 0:
#             return False

#         else:
#             return True

# if __name__ == "__main__":
#     print(prime(10))
# import math
# def prime(n):
#     if n <= 1:
#         return False
#     for y in range(2, int(math.sqrt(n)) +1):
#         if n % y == 0:
#             return False

#     return True
# if __name__ == "__main__":
#     print(prime(1))


# sieve of erathenoes python
import math
def prime(n):
    primes = []
    for i in range(2, n+1):
        primes.append(i)

    i = 2
    while(i <= int(math.sqrt(n))):
        if i in primes:
            for j in range(i*2, n+1, i):
                if j in primes:

        i = i + 1

    print(sum(primes))

if __name__ == "__main__":
    print(prime(2000000))


