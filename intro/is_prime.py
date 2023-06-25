'''
Write a function, is_prime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.

A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.

You can assume that the input number is a positive integer.
'''

import math

def is_prime(n):
  is_prime_num = True
  numbers_to_check = [*range(2, n)]
  print(numbers_to_check)
  if n == 1:
    return False
  if n != 2:
    for num in numbers_to_check:
      print("Checking " + str(num))
      if n % num == 0:
        return False
    return True
  else:
    return True
  
print(is_prime(2))
print(is_prime(3))
print(is_prime(8))
print(is_prime(11))
print(is_prime(25))
print(is_prime(1))