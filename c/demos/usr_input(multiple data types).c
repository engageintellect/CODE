#include <stdio.h>

int main() {
    char name[10];
    int age;
    printf("Enter your  name plz: ");
    fgets(name, 10, stdin);


    printf("Enter your  age plz: ");
    scanf("%d", &age);

    printf("\n");


    printf("My name is %s",name);
    printf("And I am %d", age);
    printf("\n");
    return 0;

}
