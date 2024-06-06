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