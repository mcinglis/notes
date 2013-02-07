package main

import (
	"fmt"
	"math"
)

type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
	return fmt.Sprintf("cannot Sqrt negative number: %f", e)
}

func SqrtError(x float64) (float64, error) {
	if x < 0 {
		return 0, ErrNegativeSqrt(x)
	}

	next := func(z float64) float64 {
		return z - (z*z-x)/(z*2)
	}

	lastZ, z := x, 1.0
	for math.Abs(z-lastZ) > 1e-10 {
		lastZ, z = z, next(z)
	}
	return z, nil
}

func main() {
	fmt.Println(SqrtError(2))
	fmt.Println(SqrtError(-2))
}
