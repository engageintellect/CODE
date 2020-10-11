// HELLO WORLD IN GO!

// ALL FILES NEED A PACKAGE (default main)
package main

// import different packages ('fmt', 'math', 'etc')
import ("fmt")


// main function
func main() {
    var x int
    var y int = 7
    var name = "josh"

    fmt.Println(x, y, name)

}


// execute file using "go run <name of program>"
// build executable using "go build <name of program>"
// install executable using "go install <name of program>"
