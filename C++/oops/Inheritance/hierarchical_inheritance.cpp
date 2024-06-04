#include<iostream>
using namespace std;
class Shape{
    public :
        void shape(){
            cout<<"I am shape"<<endl;
        }
};
class Shape2d : public Shape{
    public :
        void shape2d(){
            cout<<"I am from shape2d"<<endl;
        }
};
class Square : public Shape2d{
    public :
        void square(){
            cout<<"I am from shape square"<<endl;
        }
};
class Circle : public Shape2d{
    public :
        void circle(){
            cout<<"I am from shape cirlce"<<endl;
        }
};
class Shape3d : public Shape{
    public :
        void shape3d(){
            cout<<"I am from shape3d"<<endl;
        }
};
class Cube : public Shape3d{
    public :
        void cube(){
            cout<<"I am from cube"<<endl;
        }
};
int main(){
    Cube c3d;
    c3d.cube();
    c3d.shape3d();
    c3d.shape();
    return 0;
}