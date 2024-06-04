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
            cout<<"I am from class B"<<endl;
        }
};
class C : public B{
    public :
        void c(){
            cout<<"I am from class C";
        }
};
int main(){
    C obj;
    obj.a();
    obj.b();
    obj.c();
    return 0;
}