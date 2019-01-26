fn fibonacci(n: i32) -> i32 {
    if n == 0 {
        return 0;
    }

    if n <= 1 {
        return 1;
    }

    else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

fn main(){
    for x in 0..10 {
        println!("Fibonacci number {} is {}", x, fibonacci(x))
    }
}
