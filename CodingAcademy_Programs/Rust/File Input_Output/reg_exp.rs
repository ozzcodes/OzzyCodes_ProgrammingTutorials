use std::env;
use std::fs::File;
use std::path::Path;
use std::error::Error;

fn how_old(an_age:i16) -> &'static str {
    match an_age {
        0 => "Too young!!",
        -1 | 2 => "at the age of cheating!",
        1...18 => "Still very young!",
        18...25 => "At the age of studying",
        ready_for_work @ 26...40 => "At the age of working!",

        _ if(an_age % 10 == 0) => "at a new decade!",
        _ => "Unknown age!"
    }
}

fn a_simple_example() {
    for age in 25..51 {
        println!("{}: you are {}", age, how_old(age));
    }
}

fn main() {
    a_simple_example();
}