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

// Fibonacci series
function Fibonacci(n) {
	if (n <= 1) { return n; }
	else { return Fibonacci(n-1) + Fibonacci(n-2); }

};

// Palindrome checker
function palindrome(str) {
  newstr = str.toLowerCase();
  if (newstr[0] !== newstr.slice(-1)) {
    return false;
  }
  else {
    return true;
  }
   return palindrome(newstr[0]) + palindrome(newstr[newstr.slice(-1)]);
  }