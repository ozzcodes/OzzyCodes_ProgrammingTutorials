use std::thread;
use std::sync::Arc; // Arc = Atomic Reference Counting

static NTHREADS: i32 = 5;

fn main() {
    let my_array = Arc::new([-1, -2, -3, -4, -5]);
    let mut my_threads = vec![];

    for i in 0..NTHREADS as usize {
        let ar = my_array.clone();
        let join_handle = thread::spawn(move || {
            println!("The {} element of the array is {}", i, ar[i]);
        });
        my_threads.push(join_handle);
    }
    for join_handle in my_threads {
        let _ = join_handle.join();
    }
}