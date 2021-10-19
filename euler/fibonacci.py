# def fibonacci(n):

#     a = 0
#     b = 1

#     if n < 0:
#         return False

#     elif n == 0:
#         return 0

#     elif n == 1:
#         return b


#     else:
#         for i in range(2,n):
#             c = a + b
#             a = b
#             b = c



# fibonacci(10)


def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2

    else:
        return fib(n-1) + fib(n-2)

total = 0
n = 0
while fib(n) <= 4000000:
    if fib(n) % 2 == 0:
        total += fib(n)
    n += 1

print(total, n)

    
