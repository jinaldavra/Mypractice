#include<stdio.h>
#include<string.h>
int main(){
    char name1[] = "Java";
    char name2[5];
    
    strcpy(name2,name1);
    printf("%s",name2);
    return 0;
}