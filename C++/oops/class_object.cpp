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


#include<iostream>
using namespace std;
class car{
    public :
    string Brand = "Bugatti";
    string Model = "ZHMY";
    int Year = 1909;
};
class cars{
    public : 
    string Brand = "BMW";
    string Model = "x5";
    int Year = 1999;
};
int main(){
    car info;
    cout<<"Brand : "<<info.Brand<<endl;
    cout<<"Model : "<<info.Model<<endl;
    cout<<"Year  : "<<info.Year<<endl;
    
    cars infos;
    cout<<"Brand : "<<infos.Brand<<endl;
    cout<<"Model : "<<infos.Model<<endl;
    cout<<"Year  : "<<infos.Year<<endl;
    
    return 0;
}

#include<iostream>
using namespace std;
class Employ{
    public :
    int Id = 101;
    string Name = "Zen";
    float Salary = 100000;
};
int main(){
    Employ info;
    cout<<"Id     : "<<info.Id<<endl;
    cout<<"Name   : "<<info.Name<<endl;
    cout<<"Salary : "<<info.Salary<<endl;
    
    return 0;
} 

#include<iostream>
using namespace std;
class Employ{
    public :
    int Id;
    string Name;
    float Salary;
};
int main(){
    Employ info1;
    info1.Id = 101;
    info1.Name = "Zen";
    info1.Salary = 100000;
    cout<<"Id     : "<<info1.Id<<endl;
    cout<<"Name   : "<<info1.Name<<endl;
    cout<<"Salary : "<<info1.Salary<<endl<<endl;
    
    Employ info2;
    info2.Id = 102;
    info2.Name = "Sen";
    info2.Salary = 200000;
    cout<<"Id     : "<<info2.Id<<endl;
    cout<<"Name   : "<<info2.Name<<endl;
    cout<<"Salary : "<<info2.Salary<<endl;

    return 0;
} 

