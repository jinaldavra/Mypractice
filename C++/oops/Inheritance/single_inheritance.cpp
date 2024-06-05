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

// Example :

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
int main(){
    Programmer p1;
    cout<<"Salary : "<<p1.Salary<<endl;
    cout<<"Bonus  : "<<p1.Bonus<<endl;
    return 0;
}
