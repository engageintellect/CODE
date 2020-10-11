#include <stdio.h>

// import this...
#include <unistd.h>

int main () {

    printf("hello\n");

    // sleep
    sleep(4);

    int x;
    x = 0;
    for(x=x;x<1000000;) {
        x = x + 1;
        printf("%d", x);
    }

}
