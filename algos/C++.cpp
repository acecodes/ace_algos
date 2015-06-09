#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// Euclid's algorithm

int Euclid(int p, int q) {

	if (q == 0) {
		return p;
	}

	else {
		int r = p % q;
		return Euclid(q, r);
	}
}

// Fibonacci sequence

int Fibonacci(int n) {

	if (n <= 1) {
		return n;
	}

	else {
		return Fibonacci(n-1) + Fibonacci(n-2);
	}
}

int Factorial(int n) {

	if (n == 0 | n == 1) {
		return 1;
	}

	else {
		return n * Factorial(n-1);
	}
}

bool test_function (int i, int j) { return (i < j); }

int BinarySearch() {

	int search_array[] = {1, 5, 2, 9, 3, 6, 4};
	std::vector<int> v(search_array, search_array+9);

	std::sort (v.begin(), v.end());

	std::cout << "Looking for a 5...";
	if (std::binary_search (v.begin(), v.end(), 5))
		std::cout << "Found.\n"; else std::cout << "Not found.\n";

	return 0;
}

int main() {
	BinarySearch();
	// int input1;
	// int input2;
	// cout << "Enter a number: ";
	// cin >> input1;
	// cout << "Now enter another: ";
	// cin >> input2;
	// cout << "Euclid's algorith: " << Euclid(input1, input2) << endl;
	// cout << "Fibonacci sequence: " << Fibonacci(input1) << endl;
	// cout << "Factorial: " << Factorial(input1) << endl;
	// return 0;
}
