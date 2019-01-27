//! This is a program that shows how to generate
//! Memory Mapped files in Rust
//!
//! # Example
//! ```
//! let a_var = 2
//! println!("The double of {} is {}", a_var, double_me(a_var))
//! ```
//!
//! ```c
//! printf("This is not Rust code!\n");
//! ```


use std::ptr;
use std::fs;
use std::io::{Write, SeekFrom, Seek};
use std::os::unix::prelude::AsRawFd;
use mmap::{MemoryMap, MapOption};
use std::env;

extern crate mmap;
extern crate libc;

/// This is a dummy function named `double_me()`.
pub fn double_me(x: i32) -> i32 {
    x * 2
}

/// Another dummy function called `another_double_me()`.
pub fn another_double_me(x: i32) -> i32 {
    x * 2
}

fn main() {
    let size: usize = 512 * 512;

    let args: Vec<_> = env::args().collect();
    if args.len() != 2 {
        panic!("Wrong number of arguments!");
    }

    let filename = ::std::env::args().nth(1).unwrap();
    let mut f = fs::OpenOptions::new().read(true)
        .write(true)
        .create(true)
        .open(filename)
        .unwrap();

    f.seek(SeekFrom::Start(size as u64)).unwrap();
    f.write_all(&[0]).unwrap();
    f.seek(SeekFrom::Start(0)).unwrap();

    let mmap_opts = &[
        MapOption::MapNonStandardFlags(libc::MAP_SHARED),
        MapOption::MapReadable,
        MapOption::MapWritable,
        MapOption::MapFd(f.as_raw_fd()),
    ];

    let mmap = MemoryMap::new(size, mmap_opts).unwrap();
    let data = mmap.data();

    if data.is_null() {
        panic!("Could not access data from memory mapped file")
    }

    let src = "Hello world, from OzzyCodes!\n";
    let src_data = src.as_bytes();

    unsafe {
        ptr::copy(src_data.as_ptr(), data, src_data.len());
    }
}

// Terminal command line arguments for memoryMapped project

//ozzycodes@ozzycodes-ML-LIQUID:~$ cargo run newFile
//   Compiling memoryMapped v0.1.0 (/home/ozzycodes/OzzyCodes_ProgrammingTutorials/CodingAcademy_Programs/Rust/File Input_Output/memoryMapped)
//warning: crate `memoryMapped` should have a snake case name such as `memory_mapped`
//  |
//  = note: #[warn(non_snake_case)] on by default
//
//    Finished dev [unoptimized + debuginfo] target(s) in 0.36s
//     Running `target/debug/memoryMapped newFile`

//ozzycodes@ozzycodes-ML-LIQUID:~$ ls -l newFile
//-rw-rw-r-- 1 ozzycodes ozzycodes 262145 Jan 27 16:54 newFile

//ozzycodes@ozzycodes-ML-LIQUID:~$ head -1 newFile
//Hello world, from OzzyCodes!

//ozzycodes@ozzycodes-ML-LIQUID:~$ file newFile
//newFile: ASCII text
