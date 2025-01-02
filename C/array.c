#include <stdio.h>
int main() {
    int arr[] = {1,2,3,4};    //you can also specify the number elements by putting a number in the sq brackets
    printf("%d \n", arr[1]);
    arr[3]=9;        //array edit kar diya
    printf("%d \n",arr[3]);
    printf("%lu", sizeof(arr)/4);    //lu is used for size. sizeof tells the no. of bytes, since each int is 4 bytes we divide accordingly


}