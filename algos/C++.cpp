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

int Fibonacci(int n) {

	if (n == 0 | n == 1) {
		return 1;
	}

	else {
		return Fibonacci(n-1) + Fibonacci(n-2);
	}
}

int main() {

	cout << "Euclid's algorith with 15 and 5: " << Euclid(15, 5) << endl;
	cout << "Fibonacci sequence up to 10: " << Fibonacci(10) << endl;
	return 0;
}
