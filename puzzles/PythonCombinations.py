# Using nested for loops - obviously not the optimal way to do this!
def combinations(data):
	result = []
	for p1 in range(len(data)):
		for p2 in range(p1+1, len(data)):
			result.append([data[p1], data[p2]])
	return result


if __name__ == '__main__':
	flat = [1,2,3,4,5,6]
	nested = [[1,2], [4, 7, 8], [9, 2, 5]]
	print len(flat)
	print combinations(flat)