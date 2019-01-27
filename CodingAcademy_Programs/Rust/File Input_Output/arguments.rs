use std::env;

fn main() {
    let mut counter = 0;

    for argument in env::args() {
        counter = counter + 1;
        println!("{}: {}", counter, argument);
    }
}