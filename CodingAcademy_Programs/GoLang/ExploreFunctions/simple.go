package main

import "fmt"

// Functions that takes in one argument
func oneArgument(x int) int {
	return x + x
}

// Function with two or more arguments that are the same
func sameArgType(x, y int) {
	fmt.Println(x + y)
}

// Function with multiple return values
func multipleReturn(x, y int) (int, int) {
	if x > y {
		return x, y
	} else {
		return y, x
	}
}

// Go's main function type
func main() {

	// Using the developers own functions
	sameArgType(2, 3)
	fmt.Println(oneArgument(3))
	x, y := multipleReturn(5, 6)
	fmt.Println(multipleReturn(5, 6))
	fmt.Println(x, y)
}
