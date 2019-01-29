use std::net::TcpStream;
use std::time::Duration;
use std::io::Write;
use std::io::Read;


/// Uses a terminal command argument (the port number) when executing
fn main() {
    let one_second = Duration::new(1, 0);
    let port = ::std::env::args().nth(1).unwrap();
    let ip = "127.0.0.1";
    let my_bind = ip.to_string() + ":" + &port;
    let my_bind_final: &str = &my_bind;

    let mut buf: [u8; 20] = [0; 20];
    let stream = TcpStream::connect(my_bind_final);

    std::thread::sleep(one_second);
    println!("stream info: {:?}", stream);

    let mut my_stream = stream.unwrap();
    my_stream.write(b"Hello, world for OzzyCodes\r\n").unwrap();

    let _ = match my_stream.read(&mut buf) {
        Err(e) => panic!("Error: {}", e),
        Ok(m) => {
            if m == 0 {
                println!("Failed to Read!");
            }

            println!("Read: {} chars", m);
            m
        }
    };

    println!("{:?}", &buf);
}