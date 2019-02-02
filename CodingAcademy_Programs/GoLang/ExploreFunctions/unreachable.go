package main

import "fmt"

func main() {
	x := 0

	if x == 0 {
		fmt.Println("x equals 0!")
		return
	} else {
		fmt.Println("x is not equal to 0!")
		return
	}

	// The unreachable code piece
	fmt.Println("Reach me if you can!")
}
