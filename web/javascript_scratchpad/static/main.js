alert("WELCOME!");


let name = prompt("USERNAME");

if (name != "r3dux") {
    alert("WRONG USERNAME");
    var x = 0;
    while(x<1){
        alert("fuck off");
    }
}

else
    alert("Welcome " + name + "!");
    let pass = prompt("PASSWORD");
    if(pass == "pass"){
        let title = document.write("<h1>JAVASCRIPT SCRATCHPAD</h1>");

        let write = prompt("would you like to write something?", "yes / no");
        if (write == "yes"){
            let user_in = prompt("ENTER HEADER TITLE");
            let user_text = document.write("<h1>" + user_in + "</h1>");
            let usr1 = prompt("ENTER BODY");
            document.write("<h2>" + usr1 + "</h2>"); 
        }

}
    else{
        alert("WRONG PASSWORD!");
        var x = 0;
        while(x<1){
            alert("fuck off");
        }
    } 
