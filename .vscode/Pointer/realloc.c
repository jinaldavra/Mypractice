#include<stdio.h>
#include<stdlib.h>
int main(){
    int* ptr;
    int n = 5,i;
    printf("given number of elements ; %d\n",n);
    ptr = (int*)calloc(n, sizeof(int));
    if(ptr == NULL){
        printf("Memory is not alloacted\n");
        exit(0);
    }
    else{
        printf("Memory successfully allocated using calloc.\n");
        for(i = 0; i < n; i++){
            ptr[i] = i+1;
        }
        printf("The elements of the array are :");
        for(i = 0; i < n; ++i){
            printf("%d, " ,ptr[i]);
        }
        n = 12;
        printf("\n\nEnter the new size of the array : %d\n",n);
        ptr = (int*)realloc(ptr,n*sizeof(int));                  //realloc()
        printf("Memory successfully re-allocated using realloc.\n");
        for(i = 5; i < n; ++i){
            ptr[i] = i + 1;
        }
        printf("The elements of the array are :");
        for(i = 0; i < n; ++i){
            printf("%d, ",ptr[i]);
        }
        free(ptr);
    }
    return 0;
}