package main

import "fmt"

// Naming a function and the return values
func minMax(x, y int) (min, max int) {
	if x > y {
		min = y
		max = x

	} else {
		min = x
		max = y

	}
	return min, max
}

// Another example of the above
func namedMinMax(x, y int) (min, max int) {
	if x > y {
		min = y
		max = x

	} else {
		min = x
		max = y

	}

	return
}

func main() {

	fmt.Println(minMax(15, 6))
	fmt.Println(namedMinMax(15, 6))

	min, max := namedMinMax(12, -1)
	fmt.Println(min, max)

}
