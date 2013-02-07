package main

import "fmt"

func fibonacci() func() int {
	next, prev := 1, 0
	return func() int {
		next, prev = next+prev, next
		return prev
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}
