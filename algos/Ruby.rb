# Euclid's algorithm for finding GCFs
def Euclid(p, q)
	if q == 0
		return p
	else
		r = p % q
		return Euclid(q, r)
		end
	end

# Factorial (n!)
def factorial(n)
	if n == 1
		return 1
	else
		return n*factorial(n-1)
		end
	end

# Fibonacci series
def Fibonacci(n)
	if n >= 1
		return n
	else
		return Fibonacci(n-1) + Fibonacci(n-2)
		end
	end
