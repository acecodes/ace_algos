var Main = (function() {

    "use strict";

    function Recursion() {}

    Recursion.prototype = {
        euclid: function euclid(p, q) {
            // Euclid's algorithm for finding GCFs
            if (q === 0) {
                return p;
            } else {
                var r = p % q;
                return euclid(q, r);
            }
        },

        summer: function summer(n) {
            // Recursively sum up to n
            if (n > 0) {
                return n + summer(n - 1);
            } else {
                return 0;
            }
        },

        powers: function powers(n, power) {
            // Recursively calculate power of n
            if (power == 1) {
                return n;
            } else {
                return n * powers(n, power - 1);
            }
        },

        factorial: function factorial(n) {
            // Factorial
            if (n === 1 || n === 0) {
                return 1;
            } else {
                return n * factorial(n - 1);
            }
        },

        fibonacci: function fibonacci(n) {
            // Fibonacci series
            if (n <= 1) {
                return n;
            } else {
                return fibonacci(n - 1) + fibonacci(n - 2);
            }
        },

        fibonacciMemo: function fibonacciMemo() {
            // Fibonacci with memoization
            var memo = [0, 1];
            var fib = function(n) {
                var result = memo[n];
                if (typeof result !== "number") {
                    result = fib(n - 1) + fib(n - 2);
                    memo[n] = result;
                }
                return result;
            };
            return fib;
        },

        hanoi: function hanoi(disk, src, aux, dst) {
            // Tower of Hanoi solver
            if (disk > 0) {
                hanoi(disk - 1, src, dst, aux);
                console.log("Move disk " + disk + " from " + src + " to " + dst);
                hanoi(disk - 1, aux, src, dst);
            }
        },

        palindrome: function palindrome(str) {
            // Palindrome checker
            newstr = str.toLowerCase();
            if (newstr[0] !== newstr.slice(-1)) {
                return false;
            } else {
                return true;
            }
            return palindrome(newstr[0]) + palindrome(newstr[newstr.slice(-1)]);
        },

        flatten: function flattenArrays(a, r) {
            // Flatten an array
            var len = a.length;
            if (!r) {
                r = [];
            }
            for (var i = 0; i < len; i++) {
                if (a[i].constructor === Array) {
                    flattenArrays(a[i], r);
                } else {
                    r.push(a[i]);
                }
            }
            return r;
        }
    };

    function Search() {}

    Search.prototype = {
        linearSearch: function linearSearch(array, target) {
            // Linear search
            var len = array.length;
            for (var i = 0; i < len; i++) {
                if (array[i] === target) {
                    return i;
                }
            }
            return -1;
        }
    };

    function Sorting() {}

    Sorting.prototype = {
        mergeSort: function mergeSort(array, start, end) {
            if (start < end) {
                var mid = Math.floor((start + end) / 2);
                mergeSort(array, start, mid);
                mergeSort(array, mid + 1, end);
                merge(array, start, mid, end); // Implement merge
            }

            // Merge, which performs most of the work in merge sort
            function merge(left, right) {
                var result = [],
                    indexLeft = 0,
                    indexRight = 0,
                    leftLength = left.length,
                    rightLength = right.length;

                while (indexLeft < leftLength && indexRight < rightLength) {
                    if (left[indexLeft] < right[indexRight]) {
                        result.push(left[indexLeft++]);
                    } else {
                        result.push(right[indexRight++]);
                    }
                }
                return result.concat(left.slice(indexLeft).concat(right.slice(indexRight)));
            }
            // Merge sort, recursive sorting algorithm with guaranteed n log n performance
            function mergeSort(array) {
                var len = array.length;
                if (len < 2) {
                    return array;
                }

                var middle = Math.floor(len / 2),
                    left = array.slice(0, middle),
                    right = array.slice(middle);

                return merge(mergeSort(left), mergeSort(right));
            }
        }
    };

    // Memoizer for usage in other recursive algorithms
    function memoizer(memo, formula) {
        var recur = function(n) {
            var result = memo[n];
            if (typeof result !== "number") {
                result = formula(recur, n);
                memo[n] = result;
            }
            return result;
        };
        return recur;
    }
    // Fibonacci and factorial utilizing the memoizer function
    var fibonacciShortMemo = memoizer([0, 1], function(recur, n) {
        return recur(n - 1) + recur(n - 2);
    });
    var factorialShortMemo = memoizer([1, 1], function(recur, n) {
        return n * recur(n - 1);
    });

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
            var len = this._length;
            //Check for out-of-bounds values
            if (index > -1 && index < len) {
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
            var len = this._length;
            if (index > -1 && index < len) {
                var current = this._head,
                    previous, i = 0;
                if (index === 0) {
                    this._head = current.next;
                } else {
                    while (i++ < index) {
                        previous = current;
                        current = current.next;
                    }
                    previous.next = current.next;
                }
                len--;
                return current.data;
            } else {
                return null;
            }
        }
    };

    function Solutions() {}

    Solutions.prototype = {
        triplets: function triplets(A) {
            // Find maximum triplet, from Codility
            // A is an array
            var len = A.length;
            Array.prototype.max = function() {
                return Math.max.apply(null, this);
            };
            if (len < 3) {
                throw "The array is too small";
            }

            function sorter(a, b) {
                return a - b;
            }
            A = A.sort(sorter);
            var result = [A[0] * A[1] * A[len - 1], A[len - 1] * A[len - 2] * A[len - 3]].max();
            return result;
        },

        palindrome: function palindrome(s) { 
            // Palindrome checker without recursion
            return s === s.split("").reverse().join(""); 
        }
    };
})();
