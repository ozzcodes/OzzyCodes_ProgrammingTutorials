package main

import "fmt"

func changeOne(x []int) {
	x[3] = -2

}

func printSlice(x []int) {
	for _, number := range x {
		fmt.Printf("%d ", number)
	}
	fmt.Printf("\n")

}

func main() {

	// This is a slice
	aSlice := []int{2, 4, 5, 6, 7, 8}
	fmt.Printf("Before changeOne\n")
	printSlice(aSlice)
	changeOne(aSlice)
	fmt.Printf("After changeOne\n")
	printSlice(aSlice)

	// Before
	fmt.Printf("Before. Cap: %d, length: %d\n", cap(aSlice), len(aSlice))
	// Add an element to it
	aSlice = append(aSlice, -100)
	// After
	fmt.Printf("After. Cap: %d, length: %d\n", cap(aSlice), len(aSlice))

	// This is another slice
	anotherSlice := make([]int, 3)
	printSlice(anotherSlice)

	// This will not work
	// otherArray := [...]int{2,4,5,6,7,8}
	// printSlice(otherArray)
}
