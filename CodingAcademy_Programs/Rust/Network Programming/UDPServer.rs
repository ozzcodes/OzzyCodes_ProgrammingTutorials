use std::str;
use std::thread;
use std::net::UdpSocket;

fn main() {
    let port = ::std::env::args().nth(1).unwrap();
    let ip = "0.0.0.0";
    let my_bind = ip.to_string() + ":" + &port;
    let my_bind_final: &str = &my_bind;

    let socket = match UdpSocket::bind(my_bind_final) {
        Ok(s) => s,
        Err(e) => panic!("Could not bind socket: {}", e)
    };

    let mut buf = [0; 2048];

    loop {
        match socket.recv_from(&mut buf) {
            Ok((amt, src)) => {
                thread::spawn(move || {
                    println!("Got {} bytes from {}.", amt, src);
                    println!("{}", str::from_utf8(&buf).unwrap_or(""));
                });
            },

            Err(e) => {
            println!("Failed to receive data: {}", e);
            }
        }
    }
}