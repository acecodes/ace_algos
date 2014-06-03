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

	cout << "Euclid's algorith with 15 and 5: " << Euclid(15, 5) << endl;
	cout << "Fibonacci sequence up to 10: " << Fibonacci(10) << endl;
	cout << "7 Factorial: " << Factorial(7) << endl;
	return 0;
}
