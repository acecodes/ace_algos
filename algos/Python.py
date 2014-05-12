# Euclid's algorithm
# Finds the greatest common factor (GCF) between two numbers

# Test array for sorting algorithms
test_array = [4, 5, 9, 1, 3, 2, 12, 7]

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



if __name__ == '__main__':
	print(Euclid(5, 0)) # 5
	print(Euclid(25, 100)) # 25
	print(factorial(5)) # 120
	print(merge_sort(test_array))