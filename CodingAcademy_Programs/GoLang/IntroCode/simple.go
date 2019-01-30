package main

import (
	"fmt"
)

func myFibo(x int) int {
	if x == 0 || x == 1 {
		return x
	}
	return myFibo(x - 1) + myFibo(x - 2)
}

func main() {

	for i := 20; i < 30; i++ {
		fmt.Println(i, "-->", myFibo(i))
	}
}
