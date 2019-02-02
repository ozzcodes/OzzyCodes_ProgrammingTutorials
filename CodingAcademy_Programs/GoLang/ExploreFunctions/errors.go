package main

import "errors"

func division(x, y int) (int, error) {
	if y == 0 {
		return 0, errors.New("Cannot divide by zero!")
	}

	return x / y, nil
}