#include<stdio.h>
#include<conio.h>
int main(){
	int table = 10,start = 1,end = 10;
	clrscr();

	while(start<=end)
	{
		printf("%d * %d = %d\n",table,start,table*start);
		start+=1;
	}
	getch();
}