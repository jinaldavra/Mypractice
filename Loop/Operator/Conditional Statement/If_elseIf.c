#include<stdio.h>
#include<conio.h>
int main(){
       /*	int marks = 25;
	clrscr();

	if(marks >= 80){
		printf("Firstclass\n");
	}else if(marks >= 60){
		printf("Secondclass\n");
	}else if(marks >= 40){
		printf("Thirdclass\n");
	}else{
		printf("You are failed\n");
	}*/

	int marks = -16;
	clrscr();

	if(marks >= 0 && marks <= 100){
		if(marks >= 80){
			printf("Firstclass\n");
		}else if(marks >= 60){
			printf("Secondclass\n");
		}else if(marks >= 40){
			printf("Thirdclass\n");
		}else{
			printf("You are failed\n");
	}}else{
		printf("Invalid marks");
	}

	getch();
}
