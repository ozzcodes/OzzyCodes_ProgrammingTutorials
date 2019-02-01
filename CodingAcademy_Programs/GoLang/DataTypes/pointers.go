package main

import "fmt"

func main() {

	type point struct {
		X     int
		Y     int
		Label string
	}

	aStruct := point{23, 12, "A Point"}
	aPointer := &aStruct
	aPointer.X = -1

	fmt.Printf("The X field is %d.\n", aStruct.X)

	i := 10
	anotherPointer := &i
	*anotherPointer = -10

	fmt.Printf("The value of i is %d.\n", i)

	fmt.Printf("The memory address of anotherPointer is ", anotherPointer)

}
