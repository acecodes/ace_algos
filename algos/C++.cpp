#include <iostream>
#include <algorithm>
#include <vector>

// Typedefs to save space
typedef std::vector<int> vi;

// Test for greater-than or less-than
bool test_function (int i, int j) { return (i < j); }

// Data to work with
int test_array[] = {1, 5, 2, 9, 3, 6, 4};
vi test_vector{1, 5, 6, 7, 9, 12, 19};

class Recursion {
public:
	int Euclid(int p, int q) {
    // Euclid's algorithm
		if (q == 0) {
			return p;
		}

		else {
			int r = p % q;
			return Euclid(q, r);
		}
    }

	int Fibonacci(int n) {
		// Fibonacci sequence
		if (n <= 1) {
			return 1;
		}

		else {
			return Fibonacci(n-1) + Fibonacci(n-2);
		}
	}

	int Factorial(int n) {
		// Recursive factorial
		if (n == 0 | n == 1) {
			return 1;
		}

		else {
			return n * Factorial(n-1);
		}
	}

	int Summer(int n) {
		if (n > 0) {
			return n + Summer(n-1);
		} else {
			return 0;
		}
	}

	int Power(int n, int power) {
		if (power == 1) {
			return n;
		} else {
			return n * Power(n, power-1);
		}
	}

};

class Search {
public:
	int BinarySearch(vi search_vector, int seek) {

		int first = 0;
		int last = search_vector.size() - 1;
		int middle = (first + last) / 2;
		int pos = -1;

		while (first <= last) {
			if (search_vector[middle] < seek) {
				first = middle + 1;
			}
			else if (search_vector[middle] == seek) {
				pos = middle;
				return pos;
			}
			else {
				last = middle - 1;
			}

			middle = (first + last) / 2;
		}

		return pos;

	}

	int LinearSearch (vi search_array, int seek) {
		// Slow and inefficient, but it works
		int i;
		int length = search_array.size();

		for (i = 0; i < length; i++) {
			if (search_array[i] == seek) {
				return i;
			}

		}
		return -1;
	};
};

int main() {
	Search search;

	std::cout << "Binary searches:" << std::endl;
	std::cout << search.BinarySearch(test_vector, 6) << std::endl;
	std::cout << search.BinarySearch(test_vector, 12) << std::endl;
	std::cout << search.BinarySearch(test_vector, 201) << std::endl;
	
	std::cout << "Linear search: " << search.LinearSearch(test_vector, 5) << std::endl;
	
	Recursion recur;
	std::cout << "Recursive Fibonacci: " << recur.Fibonacci(5) << std::endl;
	std::cout << "Recursive summing up to 5: " << recur.Summer(5) << std::endl;
	std::cout << "Recursive 5 to the third power: " << recur.Power(5, 3) << std::endl;
	return 0;
}
