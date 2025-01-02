#include <stdio.h>

int main() {
    int num=20;
    const float flo=4.55;   //with const the value can't be changed now and this is read-only now
    float ex=45e4;  // 45 x 10^4
    char ch='L';    //only single characters are allowed in char
    char word[]="hello";
    float sum = (float) 10/3;

    printf("this is a number %d",num);
    printf("\n");
    printf("this is a character %c", ch);
    printf("\n");
    printf("this is float tho %f", flo);
    printf("\n");
    printf("this is exponent %f", ex);
    printf("\n");
    printf("this is word %s", word);
    printf("\n");
    printf("hello %f",sum);
    printf("\n");
    num=15;    //overwrite ho jayega aur kuch nhi 
    int onum;
    onum=num;    //this is a copy function, in python it is a asign function so it works differently in both languages
    printf("%d",onum);
    printf("\n");
    num=54;
    printf("%d",onum);
    printf("\n");
    printf("%d", num);
    printf("\n");
    float floa=6.12345;
    printf("%.1f",floa);
    printf("\n");
    printf("%.3f",floa);
    return 0;
    }