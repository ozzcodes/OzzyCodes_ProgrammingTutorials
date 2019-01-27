fn main() {
    let mut a_vector = Vec::new();

    a_vector.push(2);
    a_vector.push(-2);

    for x in a_vector.iter() {
        println!("{}", x);
    }
    for i in 0..a_vector.len() {
        println!("{}", a_vector[i]);
    }

    // Prevents an error from occurring if the index is larger than the vector size
    match a_vector.get(5) {
        Some(x) => println!("The value of a_vector[5] is: {}", x),
        None => println!("a_vector[5] is not defined!")
    }

    // Using the 'pop' method allows you to remove an element from a vector
    match a_vector.pop() {
        Some(x) => println!("x is {:?}", x),
        None => println!("It is not defined!")
    }
}