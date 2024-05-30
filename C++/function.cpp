// With return_type with parameters

#include<iostream>
using namespace std;
int sum(int a,int b){
    return a + b;
}
int main(){
    cout<<"Total : "<<sum(10,20);
    return 0;
}

// with_out return_type with parameters

#include<iostream>
using namespace std;
void sum(int a, int b){
    cout<<"Total : "<<a + b<<endl;
}
int main(){
    sum(10,20);
    sum(100,200);
    return 0;
}

// with return_type with_out parameters

#include<iostream>
using namespace std;
int sum(){
    int a = 10, b = 20;
    return a + b;
}
int main(){
    cout<<"Total : "<<sum();
    return 0;
}

// with_out return_type with_out parameters

#include<iostream>
using namespace std;
void sum(){
    int a = 10, b = 20;
    cout<<"Total : "<<a + b; 
}
int main(){
    sum();
    return 0;
}

// 1 + 2 + 3 + 4 + 5.......+ n using recursion function

#include<iostream>
using namespace std;
int sum_of_n(int num){
    if(num == 1){
        return 1;
    }
    else{
        return num + sum_of_n(num-1);
    }
}
int main(){
    cout<<"Total : "<<sum_of_n(5);
    return 0;
}

// Factorial number using recursion function

#include<iostream>
using namespace std;
int fact(int num){
    if(num == 1){
        return 1;
    }
    else{
        return num * fact(num-1);
    }
}
int main(){
    cout<<"Total : "<<fact(5);
    return 0;
}

// Fibonacci series using recursion function

#include<iostream>
using namespace std;
int fibo(int num){
    if(num <= 0){
        return 0;
    }
    else if(num == 1){
        return 1;
    }
    else{
        return fibo(num-1) + fibo(num-2);
    }
}
int main(){
    int n;
    cout<<"Enter number : ";
    cin>>n;
    cout<<"Fibonacci number at position n is "<<fibo(n);
    return 0;
}