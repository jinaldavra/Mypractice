#include<stdio.h>
int main(){
    int start=1,end=15;
    lable :
        if(start %2 == 0){
            printf("%d Even\n",start);
        }else{
            printf("%d Odd\n",start);
        }
        start++;
        if(start<=end)
            goto lable;
            
            return 0;
}