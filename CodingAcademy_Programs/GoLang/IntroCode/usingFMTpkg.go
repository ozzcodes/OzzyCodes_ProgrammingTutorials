package main

import "fmt"

func main() {

	// Read a number
	fmt.Print("Give me a number: ")
	var aNumber int
	_, _ = fmt.Scanln(&aNumber)
	fmt.Println("Your number is: ", aNumber)

	// Read a String
	fmt.Print("Enter your name: ")
	var name string
	_, _ = fmt.Scanln(&name)
	fmt.Println("Your name is: ", name)

	// Print its type
	fmt.Printf("The type of variable name is %T\n", name)

	// Define the decimal points of the output
	fmt.Printf("%.4f\n", 123.123123123)

}
