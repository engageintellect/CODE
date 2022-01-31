class User{
    constructor(name, email){
        this.name = name;
        this.email = email;
        this.score = 0;
    }

    login(){
        console.log(this.email, 'just logged in');
        return this;
    }

    logout(){
        console.log(this.email, 'just logged out');
        return this;
    }
    
    update_score(){
        this.score++;
        console.log(this.email, `score is now ${this.score}`);
        return this;

    }   
}

var userOne = new User("josh", "josh@gmail.com")
var userTwo = new User("jim", "jim@gmail.com")

userOne.login().update_score().update_score().logout();