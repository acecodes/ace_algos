# Euclid's algorithm
# Finds the greatest common factor (GCF) between two numbers

def Euclid(p, q):
	if q == 0:
		return p
	r = p % q
	return Euclid(q, r)

if __name__ == '__main__':
	print(Euclid(5, 0)) # 0
	print(Euclid(100, 25)) # 25