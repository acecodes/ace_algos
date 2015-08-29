package main

import "fmt"

func factorial(n uint) uint {
	// Factorial - n!
	if n <= 1 {
		return n
	}

	return n * factorial(n-1)
}

func summer(n uint) uint {
	if n <= 1 {
		return n
	} else {
		return n + summer(n-1)
	}
}

func powers(n uint, power uint) uint {
	if power > 0 {
		return n * powers(n, power-1)
	} else {
		return 1
	}
}

func main() {
	fmt.Println(factorial(7)) // 5040
	fmt.Println(summer(5))    // 15
	fmt.Println(powers(5, 2)) // 25
}
