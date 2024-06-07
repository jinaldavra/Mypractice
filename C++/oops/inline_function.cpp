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

// Example :

#include<iostream>
using namespace std;
inline int Add(int a,int b){
    return a + b;
}
int main(){
    int x = 10, y = 10;
    cout<<x<<" + "<<y<<" = "<<Add(x,y);
    return 0;
}

#include<iostream>
using namespace std;
inline int sub(int a,int b){
    return a - b;
}
int main(){
    int x = 10, y = 10;
    cout<<x<<" - "<<y<<" = "<<sub(x,y);
    return 0;
}

#include<iostream>
using namespace std;
inline int mod(int a,int b){
    return a % b;
}
int main(){
    int x = 10, y = 10;
    cout<<x<<" % "<<y<<" = "<<mod(x,y);
    return 0;
}