* - - - * 
* - - - * 
* - - - * 
* - - - * 
* - - - * 

#include<iostream>
using namespace std;
int main(){
    int num = 5;
    for(int row = 1; row <= num; row ++){
        for(int col = 1; col <= num; col++){
            if(col == 1 || col == num){
                cout<<"*"<<" ";
            }
            else{
                cout<<"-"<<" ";
            }
        }
        cout<<endl;
    }
    return 0;