pub fn fibonacci(n: i32) -> i32 {
	if n <= 1 {
		return 1;
	} else {
		return fibonacci(n-1) + fibonacci(n-2);
	}
}

pub fn factorial(n: i32) -> i32 {
    if n <= 1 {
        return 1;
    }

    return n * factorial(n-1);
}

pub fn summer(n: i32) -> i32 {
    if n > 0 {
        return n + summer(n - 1);
    } else {
        return 0;
    }
}

pub fn powers(n: i32, power: i32) -> i32 {
    if power == 1 {
        return n;
    } else {
        return n * powers(n, power-1);
    }
}

fn main() {
	println!("Fibonacci (5): {}", fibonacci(5));
    println!("Factorial (5): {}", factorial(5));
    println!("Summing up to 5: {}", summer(5));
    println!("Five to the third power: {}", powers(5, 3));
}