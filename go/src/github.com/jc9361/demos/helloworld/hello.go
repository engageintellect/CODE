// HELLO WORLD IN GO!

// ALL FILES NEED A PACKAGE (default main)
package main

// import different packages ('fmt', 'math', 'etc')
import ("fmt")


// main function
func main() {
    x := 7
    y := 10

    if x == y {
        fmt.Println("EQUAL")
    } else if x > y {
        fmt.Println(x, "is more than", y)
    } else {
        fmt.Println(x, "is less than", y)
    }



}


// execute file using "go run <name of program>"
// build executable using "go build <name of program>"
// install executable using "go install <name of program>"
