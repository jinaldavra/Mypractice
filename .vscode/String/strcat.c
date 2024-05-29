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

#include<stdio.h>
#include<string.h>
int main(){
    char name1[10] = "I";
    char s[] = " ";
    char name2[] = "am";
    char name3[] = "a";                       // print sentence using string
    char name4[] = "girl";
    strcat(name1,s);
    strcat(name1,name2);
    strcat(name1,s);
    strcat(name1,name3);
    strcat(name1,s);
    strcat(name1,name4);
    printf("%s",name1);
}