package main

import (
	"io/ioutil"
)

// Prints file out to the projects main directory, unless specified otherwise
func main() {
	aByteSlice := []byte("Hello, world!\n")
	_ = ioutil.WriteFile("aByteSlice", aByteSlice, 0644)

}
