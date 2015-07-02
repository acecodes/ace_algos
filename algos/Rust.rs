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

fn main() {
	println!("Fibonacci (5): {}", fibonacci(5));
    println!("Factorial (5): {}", factorial(5));
}