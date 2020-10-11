#include <stdio.h>



// FUNCTIONS
int add(int x, int y) {
    int result = x + y;
    printf("%d\n", result);
}

int subtract(int x, int y) {
    int result = x - y;
    printf("%d\n", result);
}

int multiply(int x, int y) {
    int result = x * y;
    printf("%d\n", result);
}


// MAIN
int main() {
    add(5,5);
    multiply(10,44);
    subtract(44,7);
}
