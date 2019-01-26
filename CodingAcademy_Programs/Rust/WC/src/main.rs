use std::io::{BufReader,BufRead};
use std::fs::File;
use std::env;

fn main() {
	let mut count = 0;
	let filename = &env::args().nth(1).unwrap();
	println!("File to open: {}", filename);

	// No Error Checking!!!
	let f = File::open(filename).unwrap();
	for line in BufReader::new(f).lines() {
		let l = line.unwrap();
	    for _ in l.chars() {
	        count += 1;
	    }
		// For each newline character
		count += 1;
	}	
	println!("Total number of characters: {}", count);
}
