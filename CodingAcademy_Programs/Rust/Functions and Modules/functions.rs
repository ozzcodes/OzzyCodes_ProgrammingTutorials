fn distance_2_d(x1: i32, x2: i32, y1: i32, y2: i32) -> f64 {
    let distance: f64 = (((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) as f64).sqrt();

    return distance;
}

fn distance_2D(x1: i32, x2: i32, y1: i32, y2: i32) -> f64 {
    let distance: f64 = (((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) as f64).sqrt();

    return distance;
}

// This function returns () which is nothing :)
fn do_nothing() {
    println!("Does nothing!");
}

fn min_max(pair: (i32, i32)) -> (i32, i32) {
    let (a, b) = pair;
    if a > b {
        return (b, a);
    }
    return pair;
}

fn sum_ab(numbers: (i32, i32)) -> i32 {
    return numbers.0 + numbers.1;
}

fn main() {
    let a = 1;
    let b = 3;
    let pair = (b, a);
    println!("Current value of pair: {:?}", pair);
    println!("Min Max returns: {:?}", min_max(pair));
    println!("The sum is: {}", sum_ab(pair));

    if do_nothing() == () {
        println!("do_nothing returns nothing!");
    }

    let x1 = 2;
    let x2 = 3;
    let y1 = -3;
    let y2 = -4;
    println!("The distance is {:.5}", distance_2_d(x1, x2, y1, y2));

    // A simple function declaration
    fn double_int(x: i32) -> (i32) { x + x }
    // A Function pointer
    let x: fn(i32) -> i32 = double_int;
    // Now use it!
    for i in 0..10 {
        println!("{} * 2 = {}", i, x(i));
    }
}
