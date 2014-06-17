# Compatability imports that allow usage in Python 2 & 3
from __future__ import print_function

# Euclid's algorithm
# Finds the greatest common factor (GCF) between two numbers
def Euclid(p, q):
	if q == 0:
		return p
	r = p % q
	return Euclid(q, r)


# Factorial (n!)
def factorial(n):
	if n == 0 or n == 1:
		return 1
	return n*factorial(n-1)

# Fibonacci
def Fibonacci(n):
	if n <= 1:
		return n
	return Fibonacci(n-1) + Fibonacci(n-2)

# Test array for sorting algorithms
test_array = [4, 5, 9, 1, 3, 2, 12, 7]

# Merge sort
def merge_sort(array):
	if len(array) == 1 or len(array) == 0:
		return array
	midpoint = len(array)/2
	left_side = array[:midpoint]
	right_side = array[midpoint:]

	merge_sort(left_side)
	merge_sort(right_side)

	left_count = 0
	right_count = 0
	sorted_count = 0

	while left_count < len(left_side) and right_count < len(right_side):
		if left_side[left_count] < right_side[right_count]:
			array[sorted_count] = left_side[left_count]
			left_count += 1
		else:
			array[sorted_count] = right_side[right_count]
			right_count += 1
		sorted_count += 1

	while left_count < len(left_side):
		array[sorted_count] = left_side[left_count]
		left_count += 1
		sorted_count += 1

	while right_count < len(right_side):
		array[sorted_count] = right_side[right_count]
		right_count += 1
		sorted_count += 1

	return array

# Luhn's algorith, for generating and validating number sequences
# AKA mod 10 algorithm

# Generate a proper sum for a given sequence
def Luhn(digits):
	# Ensure that the data entered can become a list
	if type(digits) != 'str':
		digits = str(digits)
	
	# Convert data entered 
	digits = [int(x) for x in digits]

	# Run heart of the algorithm, a description of which can be found on Wikipedia:
	# https://en.wikipedia.org/wiki/Luhn_algorithm

	for chars in digits[-1::-2]:
		if chars*2 > 9:
			subscript = digits.index(chars)
			chars = chars*2
			chars = int(int(str(chars)[0])+int(str(chars)[1]))
			digits[subscript] = chars
		else:
			subscript = digits.index(chars)
			chars = chars*2
			digits[subscript] = chars

	return sum(digits)

# Generate a check digit
def Luhn_digit(digits):
	return str(Luhn(digits)*9)[-1]

# See if a sequence of digits and a key match up
def Luhn_check(digits, check):
	return (Luhn(digits) + check) % 10 == 0

# Recursively sum up a list of numbers
def listsum(lst):
	# Define a base case
	if len(lst) == 1:
		return lst[0]
	# Move through the list recursively
	else:
		return lst[0] + listsum(lst[1:])


if __name__ == '__main__':
	print(Luhn_digit(7992739871)) # Generate a valid key sum for a check digit
	print(Luhn_check(7992739871, 3)) # Check a valid digit and key - should return True
	print(Luhn_check(7992739871, 2)) # Check an invalid digit and key - should return False
	print(listsum([1,56,9,12,22])) # Should return 100
