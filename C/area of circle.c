#include <stdio.h>
#define pi 3.1415926   //define means it is a constant now, ie the value cannot be changed now
void main() {
    float area;
    float radius;
    printf("enter the radius  ");
    scanf("%f", &radius);
    area=pi*radius*radius;
    printf("%3.3f",area);



}