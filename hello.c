#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const char *source;
int pos;


void _eval(int (*getc)()) {
    int c;
    c = getc();
    while(c != EOF) {
        if(c == 'h') {
            c = getc();
            if(c == 'e') {
                c = getc();
                if(c == 'l') {
                    c = getc();
                    if(c == 'l') {
                        c = getc();
                        if(c == 'o') {
                            printf("Hello, world!\n");
                        }
                    }
                }
            }
        } else {
            c = getc();
        }
    }
}


int sgetc() {
    if (pos == EOF) {
        return EOF;
    }

    int c = (int)source[pos];
    if (c == 0) {
        pos = EOF;
    } else {
        pos += 1;
    }
    return c;
}


static void eval(const char* _source) {
    source = _source;
    pos = 0;
    _eval(sgetc);
}

void interpreter() {
    _eval(getc);
}

int main() {
    eval("hello\nhello\nno\n");
    return 0;
}


