package main

import (
	"fmt"
	"strings"
)

func main() {

	// Define a string
	var aString = "Linux User and Developer"
	// Declare a constant string
	const anotherString = "OzzyCodes"

	for i := 0; i < len(aString); i++ {
		fmt.Printf("%x ", aString[i])
	}
	fmt.Print("\n")

	// Using binary output
	for i := 0; i < len(aString); i++ {
		fmt.Printf("%b ", aString[i])
	}
	fmt.Print("\n")

	// Use the string package
	fmt.Println(strings.Contains(aString, "Linux"))
	fmt.Println(strings.Contains(aString, "linux"))

	fmt.Println(strings.Contains(anotherString, "a"))
	fmt.Println(strings.Contains(anotherString, "w"))

	// A string array
	var aStringArray = []string{"Linux", "User", "and Developer"}
	fmt.Println(strings.Join(aStringArray, "_"))

}
