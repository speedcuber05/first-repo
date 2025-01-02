#include <stdio.h>
#include <string.h>
 
int main() {
    char alphabet[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char alphabet2[50] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    printf("Length is: %d\n", strlen(alphabet));     //this tells actual length of the string, like python len() funciton
    printf("Size is: %d\n", sizeof(alphabet));
    printf("Size is: %d\n", sizeof(alphabet2));
    strcat(alphabet,alphabet2);   //doesn't terminate alphabet2
    printf("%s \n",alphabet);  
    char st[20];
    strcpy(st,alphabet);
    printf("%s \n",st);
    char str1[] = "Hello";
    char str2[] = "Hello";
    char str3[] = "Hi";
    printf("%d\n", strcmp(str1, str2));
    printf("%d\n", strcmp(str1, str3));
}


