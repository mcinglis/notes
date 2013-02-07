package main

import "code.google.com/p/go-tour/pic"

func Pic(dx, dy int) [][]uint8 {
	ys := make([][]uint8, dy)
	for i := range ys {
		ys[i] = make([]uint8, dx)
		for j := range ys[i] {
			ys[i][j] = uint8(i * j)
		}
	}
	return ys
}

func main() {
	pic.Show(Pic)
}
