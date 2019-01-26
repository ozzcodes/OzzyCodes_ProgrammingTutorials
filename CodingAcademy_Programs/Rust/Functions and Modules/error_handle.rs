use std::fs::File;
use std::env;
use std::error::Error;

fn main() {
    let filename = &env::args().nth(1).unwrap();
    println!("File to open: {}", filename);

    let file = match File::open(&filename) {
        Err(why) => panic!("couldn't open {}: {}", filename,
                           Error::description(&why)),
        Ok(file) => file,
    };
}