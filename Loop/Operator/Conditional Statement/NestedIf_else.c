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