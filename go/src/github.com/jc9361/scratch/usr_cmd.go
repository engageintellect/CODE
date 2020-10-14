package main


import (
    "os/exec"
    "fmt"
)




func main() {
    user_input()

}


func user_input() {
    fmt.Println("Run a command...")
    var usr_in string

    fmt.Scan(&usr_in)

    cmd := exec.Command(usr_in)
    stdout, err := cmd.Output()

    if err != nil {
        fmt.Println(err.Error())
        fmt.Println("ERROR")
        main()

    }

    fmt.Print(string(stdout))
    fmt.Print("\n")

    main()


}


