#include <stdio.h>
int main() {
    int i = 0;
    while (i < 5) {
        printf("%d\n", i);
        i++;
    }


    int j = 0;
    do {                    //another way for while loop
        printf("%d\n", j);
        j++;
    }
    while (j < 5);

}
// break and continue work as python