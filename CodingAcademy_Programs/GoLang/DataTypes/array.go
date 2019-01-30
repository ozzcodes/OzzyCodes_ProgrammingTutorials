package main

import "fmt"

func main() {

	// An array
	myArray := [4]int{1, 2, 3, 4}

	length := len(myArray)

	for i := 0; i < length; i++ {
		fmt.Printf("%d ", myArray[i])
	}
	fmt.Printf("\n")

	// Another array
	anotherArray := [...]int{2, 4, 5, 6, 7, 8}

	for _, number := range anotherArray {
		fmt.Printf("%d ", number)
	}
	fmt.Printf("\n")

	// Printing a two-dimensional array
	twoD := [3][3]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	twoD[1][2] = 13

	for _, number := range twoD {
		for _, other := range number {
			fmt.Printf("%d ", other)
		}
	}
	fmt.Printf("\n")

	// Printing a three dimensional array
	threeD := [2][2][2]int{{{1, 2}, {3, 4}}, {{5, 6}, {7, 8}}}
	threeD[0][1][1] = 14

	for _, number := range threeD {
		fmt.Printf("%d ", number)
	}
	fmt.Printf("\n")
}
