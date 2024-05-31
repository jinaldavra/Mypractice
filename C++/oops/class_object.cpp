#include<iostream>
using namespace std;
class user{
    public :
    string Username = "jinal_12";
    string Email = "jinal63@gmail.com";
    string Password = "jinal@123";

    void display(){
    cout<<"Username : "<<Username<<endl;
    cout<<"Email : "<<Email<<endl;
    cout<<"Password : "<<Password<<endl;
    }
};
int main(){
    user b;
    cout<<"Username : "<<b.Username<<endl;
    cout<<"Email    : "<<b.Email<<endl;
    cout<<"Password : "<<b.Password<<endl;
    //b.display();
    return 0;
}