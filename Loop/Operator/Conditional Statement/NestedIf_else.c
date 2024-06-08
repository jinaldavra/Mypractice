#include<stdio.h>
#include<conio.h>
int main(){
	int age;
	float height;
	clrscr();

	printf("Enetr age :");
	scanf("%d",&age);

	if(age >= 18)
	{
		printf("Enter height :");
		scanf("%f",&height);
		if(height >= 155)
		{
			printf("You are eligible for Air hostess");
		}else
		{
			printf("You are not eligible for Air hostess");
		}
	}else
	{
		printf("YOu cannot apply for Air hostess");
	}
	getch();
}

// Example :

1] Checking leap year :

#include<stdio.h>
int main(){
    int year;
    printf("Enter the year : ",year);
    scanf("%d",&year);
    if(year % 4 == 0){
        if(year % 100 == 0){
            if(year % 400 == 0){
                printf("This year is leap year",year);
            }
            else{
                printf("This year is not leap year",year);
            }
    }
        else{
            printf("This year is leap year",year);
        }
    }
        else{
            printf("This year is not leap year",year);
        }
    return 0;
    }

2] Log in page :

#include<stdio.h>
#include<string.h>
int main(){
    char Username[20],Password[20];
    printf("Enter Username : ",Username);
    scanf("%s",&Username);
    if(strcmp(Username,"admin") == 0){
         printf("Enter Password : ",Password);
         scanf("%s",&Password);
         if(strcmp(Password,"1234") == 0){
            printf("Login successfull");
        }else{
        printf("Your password is incorrect");
    }
    }
    else{
        printf("Your Username is incorrct");
    }
    
    return 0;
}

3] check vowel and consonant :

#include<stdio.h>
int main(){
    char alphabet;
    printf("Enter the alphabet : ",alphabet);
    scanf("%e",&alphabet);
    if(alphabet == 'a'|| alphabet == 'e' || alphabet == 'i' || alphabet == 'o' || alphabet == 'u' || alphabet == 'A' || alphabet == 'E' || alphabet == 'I' || alphabet == 'O' || alphabet == 'U'){
        printf("This is vowel");
    }
    else{
        printf("This is consonant");
    }
    return 0;
}

4] Large number among three numbers :

#include<stdio.h>
int main(){
    int num1,num2,num3;
    printf("Enter the num1 : ",num1);
    scanf("%d",&num1);
    printf("Enter the num2 : ",num2);
    scanf("%d",&num2);
    printf("Enter the num3 : ",num3);
    scanf("%d",&num3);
    if(num1 > num2 && num1 > num3){
        printf("num1 is big");
    }
    else if(num2 > num1 && num2 > num3){
         printf("num2 is big");
    }
    else{
         printf("num3 is big");
    }
    return 0;
}

5] Check even and odd number :

#include<stdio.h>
int main(){
    int num;
    printf("Enter the number : ",num);
    scanf("%d",&num);
    if(num % 2 == 0){
        printf("This is Even number");
    }
    else{
        printf("This is odd number");
    }
    return 0;
}

6] Check the number is positive,negative or zero :

#include<stdio.h>
int main(){
    int num;
    printf("Enter the number : ",num);
    scanf("%d",&num);
    if(num > 0){
        printf("This is positive number");
    }
    else if(num < 0){
        printf("This is negative number");
    }
    else{
        printf("This is Zero");
    }
    return 0;
}
