#include <stdio.h>


int main() {
    int c;

    c = getchar();
    while(c != EOF) {
        if(c == 'h') {
            c = getchar();
            if(c == 'e') {
                c = getchar();
                if(c == 'l') {
                    c = getchar();
                    if(c == 'l') {
                        c = getchar();
                        if(c == 'o') {
                            printf("Hello, world!\n");
                        }
                    }
                }
            }
        } else {
            c = getchar();
        }
    }

    return 0;
}


