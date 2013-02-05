# For

Go only has one looping construct: the `for` loop. It has no parentheses and curly braces are required.

``` go
func main() {
    sum := 0
    for i := 0, i < 10, i++ {
        sum += i
    }
    fmt.Println(sum)    // 45
}
```

The pre and post statements can be left empty, and the semi-colons can be dropped. Then, `for` is equivalent to C's `while`.

``` go
func main() {
    sum := 1
    for sum < 1000 {
        sum += sum
    }
    fmt.Println(sum)    // 1024
}
```

If you omit the loop condition, it loops forever.

``` go
func main() {
    for {
    }
}
```

## Range

The `range` form of the `for` loop iterates over a slice or map.

``` go
var pow = []int { 1, 2, 4, 8, 16, 32, 64, 128 }

func main() {
    for i, v := range pow {
        fmt.Printf("2**%d = %d\n", i, v)
    }
}
```

You can skip the index or value by asigning to `_`. Or, if you only want the index, drop the `value` variable entirely.

``` go
func main() {
    pow := make([]int, 10)
    for i := range pow {
        pow[i] = 1 << uint(i)
    }
    for _, value := range pow {
        fmt.Printf("%d\n", value)
    }
}
```
