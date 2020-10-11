#include <stdio.h>

int main() {
    char names[10][10]={"jessica", "james", "matt", "chris", "ted"};
    int loop;

    for(loop = 0; loop<10; loop++)
        printf("%s\n", names[loop]);



}
