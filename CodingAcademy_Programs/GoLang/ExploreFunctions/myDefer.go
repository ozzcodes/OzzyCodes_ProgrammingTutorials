package main

import "fmt"

func a() {
	for i := 0; i < 4; i++ {
		defer fmt.Print(i, " ")
	}
}

func b() {
	for i := 0; i < 4; i++ {
		defer func() { fmt.Print(i, " ") }()
	}
}

func c() {
	for i := 0; i < 4; i++ {
		defer func(n int) { fmt.Print(n, " ") }(i)
	}
}

func main() {
	a()
	fmt.Println()
	b()
	fmt.Println()
	c()
	fmt.Println()
}
