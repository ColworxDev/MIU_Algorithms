
import math

# def power(x, k):
#         if k == 0:
#                 return 1
#         pwr = power(x, math.floor(k/2))
#         pwr = pwr * pwr
#         if k % 2 == 1:
#             pwr = pwr * x
#         return pwr

# def power(x, k):
#     if k == 0:
#         return 1
#     elif k == 1: return x
#     else:
#         return x * power(x, k-1)

# print(power(2,6))

def factorial(x):
    if x == 1:
        return 1
    x = x * factorial(x-1)
    return x

print(factorial(4))
