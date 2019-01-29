extern crate hyper;

use hyper::Server;
use hyper::Request;
use hyper::Response;

fn hello(_: Request, res: Response) {
    res.send(b"Hello World using Rust!").unwrap();
}

fn main() {
    let port = ::std::env::args().nth(1).unwrap();
    let ip_and_port = "127.0.0.1".to_string() + ":" + &port;
    let ip_port: &str = &ip_and_port;

    Server::http(ip_port).unwrap().handle(hello).unwrap();
}