// HELLO WORLD IN GO!

// ALL FILES NEED A PACKAGE (default main)
package main

// import different packages ('fmt', 'math', 'etc')
import ("fmt")


// main function
func main() {
    x := 5
    y := 7
    name := "josh"
    var sum int = x + y

    fmt.Println(sum, name)

}


// execute file using "go run <name of program>"
// build executable using "go build <name of program>"
// install executable using "go install <name of program>"
