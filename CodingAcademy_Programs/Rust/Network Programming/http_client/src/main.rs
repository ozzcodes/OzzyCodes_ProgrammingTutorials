extern crate hyper;

use hyper::{Client, Uri};
use hyper::rt::{self, Future, Stream};

fn main() {
    let client = Client::new();
    let res = client.get(Uri::from_static("http://linuxformat.com"))
        .and_then(|res| {
                println!("Status: {}", res.status());

            res.into_body().concat2()
        })

        .and_then(|body| {
            let s = ::std::str::from_utf8(&body)
                .expect("httpbin sends utf-8 JSON");
            println!("body: {}", s);

            Ok(())
        })

        .map_err(|err| {
            println!("error: {}", err);

        });

    rt::spawn(res);
}