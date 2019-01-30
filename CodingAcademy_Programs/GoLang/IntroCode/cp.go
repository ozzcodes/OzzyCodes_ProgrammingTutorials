package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

// Create a text file with some text for this program to copy to another file
// Terminal commands example (go run cp.go myFile.txt cpFile.txt)
func main() {
	if len(os.Args) != 3 {
		fmt.Println("Please use two command line arguments!")
		os.Exit(-1)
	}

	in := os.Args[1]
	out := os.Args[2]

	input, err := ioutil.ReadFile(in)

	if err != nil {
		fmt.Println("Error reading the input!")
	}

	err = ioutil.WriteFile(out, input, 0644)

	if err != nil {
		fmt.Println("Error creating the destination file!")
	}
}
