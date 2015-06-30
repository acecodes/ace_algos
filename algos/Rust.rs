pub fn fibonacci(n: i32) -> i32 {
	if n <= 1 {
		return 1;
	} else {
		return fibonacci(n-1) + fibonacci(n-2);
	}
}

fn main() {
	println!("Fibonacci (5): {}", fibonacci(5));
}