#include <stdio.h>


// This function works...
int func1() {
    int num;
    char name[100];
    
    printf("enter your name: ");
    fgets(name, 20, stdin);
    
    printf("enter a number: ");
    scanf("%d", &num);

    printf("%s", name);
    printf("%d", num);
}

/* This function doesnt work... it's exactly the same except 
its asking for the number before the string. */
int func2() {
    int num;
    char name[100];
    
    printf("\nenter a number: ");
    scanf("%d", &num);

   // notice that this never runs... 
    printf("enter your name: ");
    fgets(name, 20, stdin);

    printf("%s", name);
    printf("%d", num);
}


int main() {
    func1();
    func2();
}

