#!/usr/bin/python
import math

""" 
Shared functions
"""

def primality_test(n):
    n = int(n)
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f +=6
    return True

def prob1():
	""" 
	Problem 1:

	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
	The sum of these multiples is 23.

	Find the sum of all the multiples of 3 or 5 below 1000.

	"""
	multiples = [x for x in range(1,1000) if x % 3 == 0 or x % 5 == 0]
	return sum(multiples)

def prob2():
	"""
	Problem 2:

	Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

	1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

	By considering the terms in the Fibonacci sequence whose values do not exceed four million, find
	the sum of the even-valued terms.
	"""
	answer = 0
	a, b = 0, 1
	endpoint = 4000000

	while b < endpoint:
		a, b = b, a + b
		if b % 2 == 0:
			answer = answer + b 
	return answer

def prob3():
	"""
	Problem 3:

	The prime factors of 13195 are 5, 7, 13 and 29.

	What is the largest prime factor of the number 600851475143?
	"""
	end = 600851475143
	start = 2

	while (start**2 <= end):
		if (end % start == 0):
			end /= start
		else:
			start += 2 if start > 2 else 1

	return start

def prob4():
	"""
	Problem 4:

	A palindromic number reads the same both ways. The largest palindrome made from the product
	of two 2-digit numbers is 9009 = 91 * 99.

	Find the largest palindrome made from the product of two 3-digit numbers.
	"""
	palindromes = []

	for i in range(100, 999, 1):
		for j in range(999, 100, -1):
			if str(i*j)[::-1] == str(i*j):
				palindromes.append(i*j)

	return max(palindromes)

def prob5():
	"""
	Problem 5:

	2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any 
	remainder.

	What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
	"""
	smaller_list = [11, 13, 14, 16, 17, 18, 19, 20]

	for numbers in range(2520, 999999999, 2520):
		if all(numbers % n == 0 for n in smaller_list):
			return numbers
	return None

def prob6():
	"""
	Problem 6:

	The sum of the squares of the first ten natural numbers is,

	1^2 + 2^2 + ... + 10^2 = 385

	The square of the sum of the first ten natural numbers is,

	(1 + 2 + ... + 10)^2 = 55^2 = 3025

	Hence the difference between the sum of the squares of the first ten natural numbers
	and the square of the sum is 3025 - 385 = 2640.

	Find the difference between the sum of the squares of the first hundred natural numbers and
	the square of the sum.

	"""

	# Sum of the squares between 1 and 100
	sum_of_squares = sum([x**2 for x in range(1, 101)])

	# Square of the sum
	square_of_sum = sum([x for x in range(1, 101)])**2

	# Difference between two
	difference = square_of_sum - sum_of_squares

	return difference

def prob7():
	"""
	Problem 7:

	By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

	What is the 10,001st prime number?
	"""
	end = 10001
	start = 2
	count = 1
	primes = []

	while count <= end:
		if primality_test(start) == True:
			primes.append(start)
			count += 1
		start += 1

	return max(primes)



if __name__ == '__main__':
	print("Problem 1: " + str(prob1()))
	print("Problem 2: " + str(prob2()))
	print("Problem 3: " + str(prob3()))
	print("Problem 4: " + str(prob4()))
	print("Problem 5: " + str(prob5()))
	print("Problem 6: " + str(prob6()))
	print("Problem 7: " + str(prob7()))