#include<stdio.h>
#include<string.h>
int main(){
    char name1[] = "Hello";
    char name2[] = "Hello";
    
    int res = strcmp(name1,name2);
    printf("%d",res);
    return 0;
}

/*#include<stdio.h>
#include<string.h>
int main(){
    char name1[] = "Hello";
    char name2[] = "hello";
    
    int res = strcmp(name1,name2);
    printf("%d",res);
    return 0;
}*/

/*#include<stdio.h>
#include<string.h>
int main(){
    char name1 [] = "Hello";
    char name2 [] = "Hello"; 
    
    int res = strcasecmp(name1,name2);
    if(res == 0){
        printf("The strings are equal.");
    }
    else{
        printf("The strings are not equal.");
    }
    return 0;
}*/
