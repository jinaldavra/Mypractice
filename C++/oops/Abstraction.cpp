#include<iostream>
using namespace std;
class Shape{
    public :
        virtual void area() = 0;
};
class Circle : public Shape{
    public :
        void area() override{
            int r = 10;
            int area_ = 3.14 * r * r;
            cout<<"Area of Circle : "<<area_<<endl;
        }
};
class Triangle : public Shape{
    public :
        void area() override{
            int base = 10;
            int height = 10;
            int area_ = 0.5 * base * height;
            cout<<"Area of Triangle : "<<area_<<endl;
        }
};
int main(){
    Circle c1;
    c1.area();
    
    Triangle t1;
    t1.area();

    
    return 0;
}

// Example :

#include<iostream>
using namespace std;
class Shape{
    public :
        virtual void area() = 0;
};
class Circle : public Shape{
    public :
        void area() override{
            int r = 10;
            int area_ = 3.14 * r * r;
            cout<<"Area of Circle : "<<area_<<endl;
        }
};
class Triangle : public Shape{
    public :
        void area() override{
            int base = 10;
            int height = 10;
            int area_ = 0.5 * base * height;
            cout<<"Area of Triangle : "<<area_<<endl;
        }
};
class Square: public Shape{
    public :
        void area() override{
            int size = 10;
            int area_ = size * size;
            cout<<"Area of Square : "<<area_<<endl;
        }
};
int main(){
    Circle c1;
    c1.area();
    
    Triangle t1;
    t1.area();
    
    Square s1;
    s1.area();
    
    return 0;
}