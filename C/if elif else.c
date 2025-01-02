#include <stdio.h>
int main() {

    int a = 18;
    int b = 19;
    if (a>b){
        printf("20 better than 19");
    }
    else if (b>a){
        printf("maybe not");
    }
    else{
        printf("nope");
    }
    (a>b) ? printf("20 better than 19") : printf("nope");   // this is called short hand if. (condition) ? if satisfy : else
    return 0;
}