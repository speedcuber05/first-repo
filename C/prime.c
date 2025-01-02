#include <stdio.h>
void prime(n) {
    int i ;
    int c ;
    c=1;
    for (i=2;i<n;i++) {
        if (n%i==0){
            printf("this number is not prime \n");
            c=0;
            break;
        }  
    }
    if (c==1){
        printf("the number is prime");
    }

}
void main() {
    printf("enter a number \t");
    int n;
    scanf("%d",&n);
    prime(n);
}