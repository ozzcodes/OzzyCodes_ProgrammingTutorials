use std::mem;

const LINESIZE: i8 = 1024;

fn main() {
    let a1 = -789;
    let a2: i16 = 2;
    let mut a3: u32 = 123;
    let mut a4: f32 = -123.321;

    println!("The size of a1 is {} bytes", mem::size_of_val(&a1));

    // An array
    let an_array = [3.5, 1.0, 2.0];
    println!("The an_array array has {} elements", an_array.len());

    let another_array: [f32; 5] = [1.0, 3.5, 1.0, 2.0, 2.0];

    for x in another_array.iter() {
        println!("{}", x);
    }

    for x in another_array.iter().skip(2).take(2) {
        println!("{}", x);
    }

    let init_array: [f32; 5] = [2.0; 5];
}