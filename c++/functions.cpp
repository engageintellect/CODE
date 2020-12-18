#include <iostream>


int say_hi(){
    std :: cout << "hello\n";
    return 0;
}

int say_bye(){
    std :: cout << "bye\n";
    return 0;
}


int add(int x, int y){
    return x * y;
}

int main(){
    say_hi();
    say_bye();
    std::cout << add(6,7);

}
