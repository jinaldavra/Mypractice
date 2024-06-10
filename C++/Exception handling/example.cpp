#include<iostream>
using namespace std;
int main(){
    cout<<"Start"<<endl;
    cout<<"End"<<endl;
    return 0;
}

// Example :

#include<iostream>
using namespace std;
int main(){
    cout<<"start"<<endl;
    try{
        int numerator = 10;
        int denominator = 0;
        if(denominator == 0){
            throw "Division by zero error";
        }
        int result = numerator/denominator;
        cout<<"Result : "<<result<<endl;
    }
    catch(...){
        cerr<<"Unknown error occured"<<endl;
    }
    cout<<"End"<<endl;
    return 0;
}