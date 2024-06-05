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


// Example

#include<iostream>
using namespace std;
class Account{
    public :
        float Salary = 60000;
};
class Programmer : public Account{
    public :
        float Bonus = 5000;
};
class Other : public Programmer{
    public :
        float Expense = 4000;
};
int main(){
    Other r1;
    cout<<"Salary   : "<<r1.Salary<<endl;
    cout<<"Bonus    : "<<r1.Bonus<<endl;
    cout<<"Expense  : "<<r1.Expense<<endl;
    return 0;
}
