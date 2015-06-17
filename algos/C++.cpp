#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// Typedefs to save space
typedef vector<int> vi;


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

int BinarySearch(int search_array[], int seek) {

	vi v(search_array, search_array+9);

	sort (v.begin(), v.end());

	cout << "Looking for a " << seek << "...";
	
	if (binary_search (v.begin(), v.end(), seek)) {
		cout << "Found.\n";
	}
	
	else { 
		cout << "Not found.\n";
	}

	return 0;
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

int main() {
	
	int test_array[] = {1, 5, 2, 9, 3, 6, 4};
	vi test_vector{1, 5, 6, 7, 9, 12, 19};

	BinarySearch(test_array, 6);
	BinarySearch(test_array, 12);
	cout << LinearSearch(test_vector, 5);
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
