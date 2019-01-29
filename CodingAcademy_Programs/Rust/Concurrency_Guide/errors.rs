use std::thread;

fn main() {
    let my_array = [1, 2, 3, 4, 5];
    let join_handle = thread::spawn( move || {
        println!("The array is {:?}", my_array);
    });

    join_handle.join();
}