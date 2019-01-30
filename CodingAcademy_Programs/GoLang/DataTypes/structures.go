package main

import (
	"fmt"
	"reflect"
)

func main() {

	// Create a structure data type
	// If any of the structure fields begin with a lowercase, an error will occur
	type point struct {
		X int
		Y int
		Label string
	}

	p1 := point{23, 12, "A Point"}
	p2 := point{}
	p2.Label = "Another Point"

	s1 := reflect.ValueOf(&p1).Elem()
	s2 := reflect.ValueOf(&p2).Elem()
	fmt.Println("S2 = ", s2)

	typeOfT := s1.Type()
	fmt.Println("P1 = ", p1)
	fmt.Println("P2 = ", p2)

	for i := 0; i < s1.NumField(); i++ {
		f := s1.Field(i)

		fmt.Printf("%d: %s %s = %v\n", i, typeOfT.Field(i).Name, f.Type(), f.Interface())
	}

	fmt.Println("P1 = ", p1)
	fmt.Println("P2 = ", p2)

	// An array of structures
	// manyPoints := [4]points{}
}
