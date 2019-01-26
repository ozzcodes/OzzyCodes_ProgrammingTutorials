pub static AUTHOR: &'static str = "OzzyCodes";

pub mod issue211 {
	pub fn pages() {
		println!("Issue 211 has 100 pages!");
	}
}

pub fn message() {
	println!("Hello from LinuxFormat magazine!");
	println!("The author of this module is {}", AUTHOR);
}
