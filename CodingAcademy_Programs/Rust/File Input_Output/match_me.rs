use std::env;
use std::fs::File;
use std::io::{BufReader,BufRead};
use std::io::Write;

// Requires command line arguments to compile correctly:
// (ex. ./match_me match_me.rs outputFile total_lines)
fn main() {
    let mut total_lines = 0;
    let args: Vec<_> = env::args().collect();

    if args.len() != 4 {
        panic!("Usage: name input output string.");
    }

    // Iterate over the lines of the log file
    let input_path = ::std::env::args().nth(1).unwrap();
    // Output filename
    let output_file = ::std::env::args().nth(2).unwrap();
    let string_to_match = ::std::env::args().nth(3).unwrap();

    let mut f = File::create(output_file).unwrap();
    let mut file = BufReader::new(File::open(&input_path).unwrap());

    for line in file.lines() {

        total_lines = total_lines + 1;
        // Store line text to a new string variable
        let my_line = line.unwrap();
        //println!("{}", my_line);

        if my_line.contains(&string_to_match) {

            f.write_all(my_line.as_bytes());
            f.write_all(b"\n");
        }
    }

    println!("Lines processed: {}", total_lines);
}


//ozzycodes@ozzycodes-ML-LIQUID:~$ cat outputFile
//    let mut total_lines = 0;
//        total_lines = total_lines + 1;
//    println!("Lines processed: {}", total_lines);
