#include<iostream>
using namespace std;
inline int multiply(int a,int b){
    return a * b;
}
int main(){
    int x = 5, y = 10;
    cout<<"Multiplication of "<<x<<" and "<<y<<" is "<<multiply(x,y)<<endl;
    //cout<<x<<" * "<<y<<" = "<<multiply(x,y)<<endl;
    return 0;
}