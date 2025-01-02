#include <stdio.h>
int main() {
    int num;
    char ch[40];
    int nu;
    printf("enter a number  ");
    scanf("%d",&num);
    printf("%d",num);
    printf("enter a char then a number  ");
    scanf("%s %d", &ch, &nu);
    printf("%s \n",ch);
    printf("%d \n",nu);
    char fullName[30];
    printf("Type your full name: \n");
    fgets(fullName, sizeof(fullName), stdin);
    printf("Hello %s", fullName);
}