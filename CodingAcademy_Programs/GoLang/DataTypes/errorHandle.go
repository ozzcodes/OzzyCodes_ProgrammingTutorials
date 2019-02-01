package main

import (
	"fmt"
	"os"
)

// Run with various inputs for testing
/* Example:
$ go build errorHandle.go
$ ./errorHandle convert.go
File is open!

$ chmod 000 convert.go
$ ./errorHandle convert.go
open convert.go: permission denied

$./errorHandle convert1.go
open convert1.go: no such file or directory
 */

func main() {
	filename := os.Args[1]
	_, err := os.Open(filename)

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	} else {
		fmt.Println("File is open!")
	}
}
