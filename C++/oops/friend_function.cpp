#include<iostream>
using namespace std;
class MyATM{
    private :
        int pin;
    public :
        void setPin(int p){
            pin = p;
        }
        friend int myfriend(MyATM obj);
};
int myfriend(MyATM obj){
    return obj.pin;
}
int main(){
    MyATM m1;
    m1.setPin(1234);
    cout<<"My ATM pin is : "<<myfriend(m1);
    return 0;
}

// Example :

#include<iostream>
using namespace std;
class MY_NAME{
    private :
        string name;
    public :
        void setName(string n){
            name = n;
        }
        friend string myfriend(MY_NAME obj);
};
string myfriend(MY_NAME obj){
    return obj.name;
}
int main(){
    MY_NAME m1;
    m1.setName("JINAL");
    cout<<"MY NAME IS : "<<myfriend(m1);
    return 0;
}