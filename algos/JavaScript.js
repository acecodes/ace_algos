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
var fibonacci = function fibonacci(n) {
	if (n <= 1) { return n; }
	else { return fibonacci(n-1) + fibonacci(n-2); }

};


// Fibonacci with memoization
var fibonacciMemo = (function() {
    var memo = [0, 1];
    var fib = function(n) {
        var result = memo[n];
        if (typeof result !== 'number') {
            result = fib(n - 1) + fib(n - 2);
            memo[n] = result;
        }
        return result;
    };
    return fib;
})();

// Memoizer for usage in other recursive algorithms
var memoizer = function (memo, formula) {
  var recur = function (n) {
    var result = memo[n];
    if (typeof result !== 'number') {
      result = formula(recur, n);
      memo[n] = result;
    }
    return result;
  };
  return recur;
};


// Fibonacci and factorial utilizing the memoizer function
var fibonacciShortMemo = memoizer([0, 1], function (recur, n) {
  return recur(n-1) + recur(n-2);
});

var factorialShortMemo = memoizer([1, 1], function (recur, n) {
  return n * recur(n-1);
});

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
