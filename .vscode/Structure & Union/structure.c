#include<stdio.h>
#include<string.h>
struct book{
    char name[10];
    int page;
    float price;
};
int main(){
    struct book b1,b2;
    strcpy(b1.name,"Python");
    b1.page = 600;
    b1.price = 300.24;
    
    printf("Book name : %s\n",b1.name);
    printf("Book page : %d\n",b1.page);
    printf("Book price : %.2f\n",b1.price);
    
    strcpy(b2.name,"Java");
    b2.page = 700;
    b2.price = 400.30;
    
    printf("Book name : %s\n",b2.name);
    printf("Book page : %d\n",b2.page);
    printf("Book price : %.2f\n",b2.price);
    return 0;
}