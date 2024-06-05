// Function overloading :

#include<iostream>
using namespace std;
class Print{
    public :
        void display(int i){
            cout<<"Integer : "<<i<<endl;
        }
        void display(double f){
            cout<<"Float   : "<<f<<endl;
        }
        void display(string s){
            cout<<"String  : "<<s<<endl;
        }
};
int main(){
    Print p1;
    p1.display(5);
    p1.display(3.14);
    p1.display("Hello world");
    return 0;
}

// Operator overloading

#include<iostream>
using namespace std;
class Complex{
    private :
        float real;
        float imag;
    public :
        Complex() : real(0),imag(0){}
        Complex(float r,float i) : real(r),imag(i){}
        Complex operator + (const Complex &obj){
            Complex temp;
            temp.real = real + obj.real;
            temp.imag = imag + obj.imag;
            return temp;
        }
    void display(){
        cout<<real<<"+"<<imag<<"i"<<endl;
    }
};
int main(){
    Complex c1(3.3,4.4),c2(1.1,2.2);
    Complex c3 = c1 + c2;
    c3.display();
    return 0;
}