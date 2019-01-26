use std::env;

fn main() {
    let args = env::args();
    let args2 = env::args();

    for x in args {
        println!("{}", x);
    }

    let mut sum = 0;

    for x in args2.skip(1) {
        let number: u32 = x.parse().unwrap();
        println!("{}", number);
        sum += number;
    }

    println!("Sum: {}", sum);
}
