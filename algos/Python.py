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