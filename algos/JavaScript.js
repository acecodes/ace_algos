// Euclid's algorithm for finding GCFs
function Euclid(p, q) {
	if (q == 0) { return p; }
	else {
		var r = p % q
		return Euclid(q, r);
	}

};

// Factorial
function factorial(n) {
    if (n == 1 || n == 0) { return 1; }
    else { return n*factorial(n-1); }
};