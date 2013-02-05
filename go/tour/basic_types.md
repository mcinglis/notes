# Basic types

* `bool`
* `string`
* `int`, `int8`, `int16`, `int32`, `int64`
* `uint`, `uint8`, `uint16`, `uint32`, `uint64`, `uintptr`
* `byte` is an alias for `uint8`
* `rune` is an alias for `int32`; it represents a Unicode code point
* `float32`, `float64`
* `complex64`, `complex128`

``` go
import (
    "fmt"
    "math/cmplx"
)

var (
    ToBe bool = false
    MaxInt uint64 = (1 << 64) - 1
    z complex128 = cmplx.Sqrt(-5 + 12i)
)

func main() {
    const f = "%T(%v)\n"
    fmt.Printf(f, ToBe, ToBe)           // bool(false)
    fmt.Printf(f, MaxInt, MaxInt)       // uint64(18446744...)
    fmt.Printf(f, z, z)                 // complex128((2+3i))
}
```
