#include<iostream>
using namespace std;
class A{
    public :
        void a(){
            cout<<"I am from class A"<<endl;
        }
};
class B : public A{
    public :
        void b(){
            cout<<"I am from class B";
        }
};
int main(){
    B obj;
    obj.a();
    obj.b();
    return 0;
}