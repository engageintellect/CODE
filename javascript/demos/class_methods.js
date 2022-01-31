class User{
    constructor(name, email){
        this.name = name;
        this.email = email;
    }

    login(){
        console.log(this.email, 'just logged in')
    }

    logout(){
        console.log(this.email, 'just logged out')
    }   
}

var userOne = new User("josh", "jc9361@gmail.com")
var userTwo = new User("jim", "jim@gmail.com")


console.log(userOne.name)
console.log(userTwo.name)


userOne.login();
userTwo.logout();