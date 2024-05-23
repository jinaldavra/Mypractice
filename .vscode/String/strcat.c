#include<stdio.h>
#include<string.h>
int main(){
    char name1[10] = "Hello";
    char s [] = " ";
    char name2[10] = "World";
    
    strcat(name1,s);
    strcat(name1,name2);
    
    printf("%s",name1);
    return 0;
}