package main

import (
	"fmt"
	"strconv"
)

func main() {
	myArray := [4]int{1, 2, 4, -4}
	aMap := make(map[string]int)

	length := len(myArray)

	for i := 0; i < length; i++ {
		fmt.Printf("%s ", strconv.Itoa(i))
		aMap[strconv.Itoa(i)] = myArray[1]
	}
	fmt.Printf("\n")

	for key, value := range aMap {
		fmt.Printf("%s: %d\n", key, value)
	}
}
