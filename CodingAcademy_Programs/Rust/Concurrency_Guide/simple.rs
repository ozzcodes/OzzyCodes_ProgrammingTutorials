use std::thread;
use std::time::Duration;


// Compile example (time ./simple)
// Not such a useful concurrency as main() function doesn't wait for threads
// See synch.rs for updated version
fn main() {
    for _ in 0..5 {
        thread::spawn(|| {
            thread::sleep(Duration::from_millis(4000));
            println!("Hello from thread!");
        });
    }
}