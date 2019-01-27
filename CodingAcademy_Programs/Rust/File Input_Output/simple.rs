use std::env;
use std::fs::File;
use std::path::Path;
use std::error::Error;

// Uses two command line options (ex. ./simple simple.rs testMe)
fn main() {
    let args: Vec<_> = env::args().collect();
    let open = ::std::env::args().nth(1).unwrap();
    let write = ::std::env::args().nth(2).unwrap();

    let path = Path::new(&open);
    let display = path.display();

    let mut file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, Error::description(&why)),
        Ok(file) => file,
    };

    let write_path = Path::new(&write);
    let write_display = path.display();
    let write_file = match File::create(&write_path) {
        Err(why) => panic!("couldn't create {}: {}", write_display, Error::description(&why)),
        Ok(write_file) => write_file,
    };
}