package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	next := func(z float64) float64 {
		return z - (z*z-x)/(z*2)
	}

	lastZ, z := x, 1.0
	for math.Abs(z-lastZ) > 1e-10 {
		lastZ, z = z, next(z)
	}
	return z
}

func main() {
	fmt.Println("My Sqrt(2): ", Sqrt(2))
	fmt.Println("math.Sqrt(2): ", math.Sqrt(2))
}
