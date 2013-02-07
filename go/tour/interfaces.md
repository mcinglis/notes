# Interfaces

An interface type is defined by a set of methods.

A value of an interface type can hold any value that implements those methods.

``` go
type Abser interface {
    Abs() float64
}

type MyFloat float64

func (f MyFloat) Abs() float64 {
    if f < 0 {
        return float64(-f)
    }
    return float64(f)
}

type Vertex struct {
    X, Y float64
}

func (v *Vertex) Abs() float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
    var a Abser
    f := MyFloat(-math.Sqrt2)
    v := Vertex {3, 4}

    a = f
    fmt.Println(a.Abs())        // 1.41..

    a = &v
    fmt.Println(a.Abs())        // 5
}
```

## Implicit interface satisfaction

A type implements an interface by implementing the methods. *There is no explicit declaration of intent.*

Implicit interfaces decouple implementation packages from the packages that define the interfaces; neither depends on the other.

It also encourages the definition of precise interfaces, because you don't have to find every implementation and tag it with the new interface name.

The [`io` package](http://golang.org/pkg/io/) defines `Reader` and `Writer`; you don't have to.

``` go
type Reader interface {
    Read(b []byte) (n int, err error)
}

type Writer interface {
    Write(b []byte) (n int, err error)
}

type ReadWriter interface {
    Reader
    Writer
}

func main() {
    var w Writer

    // os.Stdout implements Writer
    w = os.Stdout

    fmt.Fprintf(w, "hello, writer\n")
}
```
