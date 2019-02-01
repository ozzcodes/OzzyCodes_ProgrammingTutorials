package main

import "fmt"

// Create multiple slices
func main() {
	aSlice := []int{1, 2, 3}
	aSliceNew := []int{-1, -2, -3, 4, 5}
	anotherSliceNew := []int{-1, -2}

	// Copy the new slice to an already existing slice
	copy(aSliceNew, aSlice)
	copy(anotherSliceNew, aSlice)

	// Print the slices
	fmt.Printf("aSlice: %d\n", aSlice)
	fmt.Printf("aSliceNew: %d\n", aSliceNew)
	fmt.Printf("anotherSliceNew: %d\n", anotherSliceNew)
}
