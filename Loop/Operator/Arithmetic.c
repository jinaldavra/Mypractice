#include<stdio.h>
#include<conio.h>
void main(){
	int a = 30,b = 40,c;
	clrscr();

	c = a + b;
	printf("sum = %d\n",c);

	c = a - b;
	printf("sub = %d\n",c);

	c = a * b;
	printf("multi = %d\n",c);

	c = a / b;
	printf("div = %d\n",c);

	c = a % b;
	printf("mod = %d\n",c);

	getch();
}