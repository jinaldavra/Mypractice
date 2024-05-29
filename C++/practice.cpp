1] if :

#include<iostream>
using namespace std;
int main(){
    int score = 45;
    if(score >= 35){
        cout<<"You are pass.";
    }
    return 0;
}

#include<iostream>
using namespace std;
int main(){
    int balance = 10000,w_bal = 2000;
    if(w_bal <= balance){
        balance -= w_bal;
        cout<<"Your current balance is : "<<balance;
    }
    return 0;
}

2] if_else :

#include<iostream>
using namespace std;
int main(){
    int score;
    cout<<"Enter score :";
    cin>>score;
    if(score >= 35){
        cout<<"You are pass.";
    }
    else{
        cout<<"You are fail.";
    }
    return 0;
}

#include<iostream>
using namespace std;
int main(){
    int balance,w_bal;
    cout<<"Enter balance : ";
    cin>>balance;
    cout<<"Enter w/d balance : ";
    cin>>w_bal;
    if(w_bal <= balance){
        balance -= w_bal;
        cout<<"Your current balance is : "<<balance;
    }
    else{
        cout<<"balance is insufficient";
    }
    return 0;
}

3]if_else if_ladder :

#include<iostream>
using namespace std;
int main(){
    int score;
    cout<<"Enter score : ";
    cin>>score;
    if(score >= 80){
        cout<<"First class";
    }
    else if(score >= 60){
        cout<<"Second class";
    }
    else if(score >= 40){
        cout<<"Third class";
    }
    else{
        cout<<"You are fail";
    }
    return 0;
}

#include<iostream>
using namespace std;
int main(){
    int score;
    cout<<"Enter score : ";
    cin>>score;
    if(score >= 0 && score <= 100){
        if(score >= 80){
            cout<<"First class";
        }
        else if(score >= 60){
            cout<<"Second class";
        }
        else if(score >= 40){
            cout<<"Third class";
        }
        else{
            cout<<"You are fail.";
        }
    }
    else{
        cout<<"Invalid score.";
    }
    return 0;
}

4] Nested_if_if_else :

#include<iostream>
using namespace std;
int main(){
    int age;
    int weight;
    cout<<"Enter your age : ";
    cin>>age;
    if(age >= 18){
        cout<<"Enter your weight : ";
        cin>>weight;
        if(weight >= 50){
            cout<<"You can donate.";
        }
        else{
            cout<<"You can not donate.";
        }
    }
    else{
        cout<<"You are not able to donate your blood.";
    }
    return 0;
}

5] Switch :

#include<iostream>
using namespace std;
int main(){
    int month;
    cout<<"Enter number of month : ";
    cin>>month;
    
    switch(month){
        case 0 :
            cout<<"January";
            break;
        case 1 :
            cout<<"February";
            break;
        case 2 :
            cout<<"March";
            break;
        case 3 :
            cout<<"April";
            break;
        case 4 :
            cout<<"May";
            break;
        case 5 : 
            cout<<"June";
            break;
        case 6 :
            cout<<"July";
            break;
        case 7 :
            cout<<"August";
            break;
        case 8 :
            cout<<"September";
            break;
        case 9 :
            cout<<"October";
            break;
        case 10 :
            cout<<"November";
            break;
        case 11 :
            cout<<"December";
            break;
        default :
            cout<<"Invalid month";
    }
    return 0;
}