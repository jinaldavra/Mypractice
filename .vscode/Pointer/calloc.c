#include<stdio.h>
#include<stdlib.h>
int main(){
    int* ptr;
    int n = 5,i;
    printf("given number of elements ; %d\n",n);
    ptr = (int*)calloc(n, sizeof(int));           //calloc()
    if(ptr == NULL){
        printf("Memory is not alloacted\n");
        exit(0);
    }
    else{
        printf("Memory successfully allocated using calloc\n");
        for(i = 0; i < n; i++){
            ptr[i] = i*2;
        }
        printf("The elements of the array are :");
        for(i = 0; i < n; ++i){
            printf("%d, " ,ptr[i]);
        }
    }
    return 0;
}