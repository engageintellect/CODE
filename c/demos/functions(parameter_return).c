#include <stdio.h>



int square(int x){
    printf("%d Squared is ", x);
    int result = x*x;
    printf("%d\n", result);

}

int cube(int x){
    printf("%d Cubed is ", x);
    int result = x*x*x;
    return result;
}


int main(){
    square(4);
    printf("%d", cube(3));
}








