#include<stdio.h>
#include<conio.h>
int main(){
       /*	int marks = 23;
		clrscr();

		if(marks >= 35)
		{
		printf("You are pass !");

		}else
		{
		printf("Sorry ! You are failed");

	   }*/

	   int bal = 10000,w_bal = 11000;
	   clrscr();

	   if(w_bal <= bal)
	   {
		bal -= w_bal;
		printf("Your balance is :%d\n",bal);
	   }else
	   {
		printf("Balance is insufficient\n");
	   }



	getch();
}