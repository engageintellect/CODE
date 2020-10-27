// HELLO WORLD IN GO!

// ALL FILES NEED A PACKAGE (default main)
package main

// import different packages ('fmt', 'math', 'etc')
import ("fmt")


// main function
func main() {
    var x int = 5
    var y int = 7
    var sum int = x + y

    fmt.Println(sum)

}


// execute file using "go run <name of program>"
// build executable using "go build <name of program>"
// install executable using "go install <name of program>"
