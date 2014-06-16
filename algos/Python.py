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

# Luhn's algorith, for checking the validity of certain number combinations
# AKA mod 10 algorithm
def Luhn(digits):
	### WORK IN PROGRESS, NOT FUNCTIONING CORRECTLY YET ###
	digits = list(str(digits))
	
	# From the rightmost digit, double the value of ever second digit
	double_second = [int(x)*2 for x in digits[-1::-2]]
	
	# Check if any doubles are over 9
	check_9 = [x for x in double_second if x > 9]

	# Add digits of doubled items together
	add_digits = [int(str(x)[0])+int(str(x)[1]) for x in check_9]

	# Replace digits whose doubled product is larger than 9 with summed digits
	for items in double_second:
		if int(items) > 9:
			items = add_digits.pop()

	final = ''.join(digits)

	print(final)



if __name__ == '__main__':
	Luhn(7992739871)
