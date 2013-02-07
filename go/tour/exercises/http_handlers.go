package main

import (
	"fmt"
	"net/http"
)

type String string

func (s String) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, s)
}

type Banana struct {
	Foo string
	Bar string
	Baz string
}

func (b *Banana) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, fmt.Sprint(b.Foo, b.Bar, b.Baz))
}

func main() {
	http.Handle("/string", String("I'm a frayed knot."))
	http.Handle("/banana", &Banana{"Hello", "you", "Gophers!"})
	http.ListenAndServe("localhost:4000", nil)
}
