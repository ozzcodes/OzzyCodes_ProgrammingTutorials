extern crate hyper;

use hyper::{Body, Response, Server};
use hyper::service::service_fn_ok;

fn main() {
    // Construct our SocketAddr to listen on...
    let addr = ([127, 0, 0, 1], 1234).into();

    // And a MakeService to handle each connection...
    let make_service = || {
        service_fn_ok(|_req| {
            Response::new(Body::from("Hello World from Rust!"))
        })
    };

    // Then bind and serve...
    let server = Server::bind(&addr)
        .serve(make_service);
}