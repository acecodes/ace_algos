// Euclid's algorithm for finding GCFs
var Euclid = function Euclid(p, q) {
	if (q === 0) { return p; }
	else {
		var r = p % q;
		return Euclid(q, r);
	}

};

// Factorial
var factorial = function factorial(n) {
    if (n === 1 || n === 0) { return 1; }
    else { return n*factorial(n-1); }
};

// Fibonacci series
var Fibonaccio = function Fibonacci(n) {
	if (n <= 1) { return n; }
	else { return Fibonacci(n-1) + Fibonacci(n-2); }

};

// Palindrome checker
var palindrome = function palindrome(str) {
  newstr = str.toLowerCase();
  if (newstr[0] !== newstr.slice(-1)) {
    return false;
  }
  else {
    return true;
  }
   return palindrome(newstr[0]) + palindrome(newstr[newstr.slice(-1)]);
};

// Tower of Hanoi solver
var Hanoi = function Hanoi(disk, src, aux, dst) {
  if (disk > 0) {
    Hanoi(disk - 1, src, dst, aux);
    console.log('Move disk ' + disk + ' from ' + src + ' to ' + dst);
    Hanoi(disk - 1, aux, src, dst);
  }

};

Hanoi(3, 'source', 'aux', 'destination');