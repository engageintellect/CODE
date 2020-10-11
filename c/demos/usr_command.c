#include <stdio.h>

int cmd(){
    char usr_in[1000];
    printf("> ");
    fgets(usr_in, 1000, stdin);

    int system(const char *command);

    system(usr_in);
}


int main() {
    // main loop
    int x;
    x = 0;
    if (x < 1){
        cmd();
    }
    main();

}



