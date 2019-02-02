package main

import "fmt"

/*
Interfaces:
	- A set of methods
	- A Type
	- Used for defining behavior of sn object
*/

// Define the interface to be used by the myComplex type
type complexParts interface {
	real() int
	imaginary() int
}

type myComplex2 struct {
	X int
	Y int
}

func (s myComplex2) real() int {
	return s.X
}

func (s myComplex2) imaginary() int {
	return s.Y
}

// Function to print out the complex parts values
func findComplexParts(a complexParts) {
	fmt.Println("R:", a.real())
	fmt.Println("I:", a.imaginary())
}

// Using integer numbers as complex numbers with an imaginary part of 0
type myInt int

func (s myInt) real() int {
	return int(s)
}

func (s myInt) imaginary() int {
	return 0
}

func main() {
	x := myComplex2{X: 1, Y: 2}
	fmt.Println(x)
	findComplexParts(x)

	y := myInt(10)
	findComplexParts(y)
}
