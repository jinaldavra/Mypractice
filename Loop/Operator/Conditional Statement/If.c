#include<stdio.h>
#include<conio.h>
int main(){
       /*	int marks = 40;
		clrscr();
		if(marks <= 35)
			{
				printf("Sorry ! You are failed.");
			}*/

	int bal = 20000, w_bal = 10000;
	clrscr();
	if(w_bal <= bal)
	{
		bal -= w_bal;
		printf("Your balance is : %d",bal);
	}

	getch();
}