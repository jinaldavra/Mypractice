#include<iostream>
using namespace std;
int main(){
    string name = "Hello world !";
    cout<<name;                                          // print name using string
    return 0;
}

#include<iostream>
using namespace std;
int main(){
    string name = "Hello world !";
    cout<<name[6];                                       // print character  
    return 0;
}

#include<iostream>
using namespace std;
int main(){
    int words = 1;
    string str = "This is a string";
    int last_index = str.length() - 1;
    for(int start = 0; start <= last_index; start++){
        if(str[start] == ' '){
            words += 1;
        }                                                // print words
    }
    if(str[last_index] == ' '){
        words -= 1;
    }
    cout<<"Total words is : "<<words;
    return 0;
}

#include<iostream>
#include<sstream>
using namespace std;
int main(){
    string str = "This is a string";
    int word_count = 0;
    
    istringstream stream(str);
    string word;
    
    while(stream >> word){                               // print words using new header file
        word_count++;
    }
    cout<<"Total words are : "<<word_count<<endl;
    return 0;
}