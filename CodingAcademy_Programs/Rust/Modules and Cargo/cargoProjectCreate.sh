#!/usr/bin/env bash

# Create a new project with cargo binary
waldorna@waldorna-ThinkPad-E570 ~$ cargo new helloWorld --bin
     Created binary (application) `helloWorld` project

# Change directory
waldorna@waldorna-ThinkPad-E570 ~$ cd helloWorld

waldorna@waldorna-ThinkPad-E570 ~/helloWorld $ cat Cargo.toml
[package]
name = "helloWorld"
version = "0.1.0"
authors = ["ajwaldro878 <email>"]

[dependencies]
