#include<iostream>
using namespace std;
class car{
    // data member
    public :
    string name = "Bugatti";
    string model;
    // member function
    /*void info(){
        cout<<"Car information : "<<endl;
        cout<<"Name : "<<name<<endl;
        cout<<"Model : "<<model<<endl;
    }*/
    // constructor
    car(string m){
        model = m;
        cout<<"Car information : "<<endl;
        cout<<"Name : "<<name<<endl;
        cout<<"Model : "<<model<<endl;
    }
    // destructor
    ~car(){
        cout<<"I am a distructor"<<endl;
    }
};
int main(){
    car c1("x1");
    c1.model = "x1";
    // c1.info();
    car c2("x2");
    c2.model = "x2";
    // c2.info();
    return 0;
}


#include<iostream>
using namespace std;
class Student{
    // data member
    public :
        string Name;
        string Course;
        int Marks;
    // Constructor
    Student(string n,string c,int m){
        Name = n;
        Course = c;
        Marks = m;
        cout<<"Name   : "<<Name<<endl;
        cout<<"Course : "<<Course<<endl;
        cout<<"Marks  : "<<Marks<<endl;
    }
};
int main(){
    Student s1("Ninja Coder","DSA in C++",99);
    return 0;
}

#include<iostream>
using namespace std;
class Student{
    // data member
    public :
        string Name;
        string Course;
    // constructor
    Student(string n,string c){
        Name = n;
        Course = c;
        cout<<"Name   : "<<Name<<endl;
        cout<<"Course : "<<Course<<endl;
    }
    // destructor
    ~Student(){
        cout<<"I am a destructor"<<endl;
    }
};
int main(){
    Student info("Dhruv Rawat","Information Technology");
    return 0;
}