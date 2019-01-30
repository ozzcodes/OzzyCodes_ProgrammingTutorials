package main

import (
	"fmt"
)

// Switch statement expressions and cases should match:
// else you will receive an error with the following code
/*
func main1() {
	var x = 1
	switch x {
	case true:
		fmt.Println("True")
	case false:
		fmt.Println("False")
	default:
		fmt.Println("Neither True or False!")
	}
}
*/

//# command-line-arguments
//./If_For.go:10:2: invalid case true in switch on x (mismatched types bool and int)
//./If_For.go:12:2: invalid case false in switch on x (mismatched types bool and int)

// Correct Example, where x is not defined in the switch statement
func main2() {
	var x = 1
	switch {
	case x < 0:
		fmt.Println("Negative integer")
	case x > 0:
		fmt.Println("Positive integer")
	default:
		fmt.Println("0!")

	}
}

// Switch statement to determine a variable type or function
func main() {
	var t interface{}
	t = "123"

	switch t := t.(type) {
	case bool:
		fmt.Println("Boolean:", t)
	case int:
		fmt.Println("Integer:", t)
	case float64:
		fmt.Println("Float:", t)
	default:
		fmt.Println("Unknown type!")

	}
}


// Go for loops are similar to C's but without parenthesis
/*
for i := 20; i < 30: i++ {
	... Do Something ...
}
 */

 // For loops can also be used for iterating strings:
 /*
 var aString = "Linux User & Developer"

 for _, r := range aString {
 	fmt.Println(string(r))
 }
  */