#include <stdio.h>

int display() {
    printf("\n");
    printf("RUN A COMMAND:");
    printf("\n\n");

}


int main() {

    display();
    char name[100];

    printf("> ");
    fgets(name, 100, stdin);


    printf("\n");


    int system(const char *command);
    system(name);


    return 0;

}
