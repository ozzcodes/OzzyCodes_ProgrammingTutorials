fn main() {
    let a = 1;
    let b = 3;
    let pair = (b, a);

    println!("Current value of pair: {:?}", pair);

    if a == pair.1 {
        println!("a and pair.1 are the same!");
    }
}
