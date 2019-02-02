package main

import "fmt"

// Pointer, pointing to function
func withPointer(x *int) {
	*x = *x * *x
}

// Type struct for the myComplex function pointer
type myComplex struct {
	x, y int
}

// Function using the myComplex type structure
func newComplex(x, y int) *myComplex {
	return &myComplex{x, y}
}

// Main function to run the Go program
func main() {
	x := 4
	withPointer(&x)
	fmt.Println(x)

	w := newComplex(4, 5)
	fmt.Println(*w)
}
