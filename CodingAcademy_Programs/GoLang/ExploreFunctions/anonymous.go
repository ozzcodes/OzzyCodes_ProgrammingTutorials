package main

import "fmt"

func main() {

	y := 5
	double := func(s int) int {
		return s + s
	}

	for i := 0; i < 5; i++ {
		myDouble := func(s int) int {
			return s + s
		}(i)
		fmt.Println("The double of", i, "is", myDouble)
	}

	fmt.Println("The double of", y, "is", double(y))
}
