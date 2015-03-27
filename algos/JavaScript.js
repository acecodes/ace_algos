// Euclid's algorithm for finding GCFs
var Euclid = function Euclid(p, q) {
    if (q === 0) {
        return p;
    } else {
        var r = p % q;
        return Euclid(q, r);
    }

};

// Factorial
var factorial = function factorial(n) {
    if (n === 1 || n === 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
};

// Fibonacci series
var fibonacci = function fibonacci(n) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

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
var memoizer = function(memo, formula) {
    var recur = function(n) {
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
var fibonacciShortMemo = memoizer([0, 1], function(recur, n) {
    return recur(n - 1) + recur(n - 2);
});

var factorialShortMemo = memoizer([1, 1], function(recur, n) {
    return n * recur(n - 1);
});

// Palindrome checker
var palindrome = function palindrome(str) {
    newstr = str.toLowerCase();
    if (newstr[0] !== newstr.slice(-1)) {
        return false;
    } else {
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

// Linked list
var firstNode = {
    data: 0,
    next: null
};

// Attach first node, creating the list
firstNode.next = {
    data: 1,
    next: null
};

// Linked list constructor
function LinkedList() {
    this._length = 0;
    this._head = null;
}

// Linked list methods
LinkedList.prototype = {

    // Create new node with data
    add: function(data) {
        var node = {
                data: data,
                next: null
            },

            current;

        if (this._head === null) {
            this._head = node;
        } else {
            current = this._head;

            while (current.next) {
                current = current.next;
            }

            current.next = node;
        }

        this._length++;
    },

    // Check for item at index, return null if empty
    item: function(index) {
        //Check for out-of-bounds values
        if (index > -1 && index < this._length) {
            var current = this._head,
                i = 0;

            while (i++ < index) {
                current = current.next;
            }
            return current.data;
        } else {
            return null;
        }
    },

    remove: function(index) {
        if (index > -1 && index < this._length) {
            var current = this._head,
                previous,
                i = 0;

            if (index === 0) {
                this._head = current.next;
            } else {
                while (i++ < index) {
                    previous = current;
                    current = current.next;
                }

                previous.next = current.next;
            }

            this._length--;

            return current.data;
        } else {
            return null;
        }
    }
};

// Array flattener
function flattenArrays(a, r) {
    if (!r) {
        r = [];
    }
    for (var i = 0; i < a.length; i++) {
        if (a[i].constructor == Array) {
            flattenArrays(a[i], r);
        } else {
            r.push(a[i]);
        }
    }
    return r;
}

// Find maximum triplet, from Codility
function solution(A) { // A is an array

    Array.prototype.max = function() {
        return Math.max.apply(null, this);
    };

    if (A.length < 3) {
        throw "The array is too small";
    }

    function sorter(a, b) {
        return a - b;
    }

    A = A.sort(sorter);

    var result = [A[0] * A[1] * A[A.length - 1],
        A[A.length - 1] * A[A.length - 2] * A[A.length - 3]
    ].max();

    return result;
}