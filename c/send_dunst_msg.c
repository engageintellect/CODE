#include <stdio.h>
#include <string.h>

int main() {

    /* initialize system command */
    int system(const char *comand);
    char cmd[1000];

    system("clear");

    /* take user input */
    char input[1000];
    printf("ENTER SHELL COMMAND: ");
    fgets(input, 1000, stdin);

    /* format command */
    char notify[1000] = "notify-send $(";
    char notify2[1000] = ")";

    strcat(notify, input, notify2);

    
    /* exec command */
    system(notify);

    return 0;


}

