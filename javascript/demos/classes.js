class User{
    constructor(name, email){
        this.name = name;
        this.email = email;
    }
}

var userOne = new User("josh", "josh@gmail.com")
var userTwo = new User("jim", "jim@gmail.com")


console.log(userOne.name)
console.log(userTwo.name)