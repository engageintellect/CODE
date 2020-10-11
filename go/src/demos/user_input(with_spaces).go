package main

import(
"os/exec"
"bufio"
"os"
"fmt"
)



func main(){
    fmt.Print("INTPUT CMD")
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan() // use `for scanner.Scan()` to keep reading
    line := scanner.Text()
    fmt.Println("captured:",line)

}


