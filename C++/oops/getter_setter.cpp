#include<iostream>
using namespace std;
class ATM{
    private :
        int pin;
    public :
        void setPin(int p){
            pin = p;
        }
        int getPin(){
            return pin;
        }
};
int main(){
    ATM a1;
    a1.setPin(1234);
    cout<<"PIN set to : "<<a1.getPin()<<endl;
    return 0;
}


#include<iostream>
using namespace std;
class car{
    private :
        string name;
    public :
        void setName(string n){
            name = n;
        }
        string getName(){
            return name;
        }
};
int main(){
    car c1;
    c1.setName("Bugatti");
    cout<<"Name set to : "<<c1.getName()<<endl;
    return 0;
}
