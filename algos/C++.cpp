#include <iostream>

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

int main() {
	int input1;
	int input2;
	cout << "Enter a number: ";
	cin >> input1;
	cout << "Now enter another: ";
	cin >> input2;
	cout << "Euclid's algorith: " << Euclid(input1, input2) << endl;
	cout << "Fibonacci sequence: " << Fibonacci(input1) << endl;
	cout << "Factorial: " << Factorial(input1) << endl;
	return 0;
}
