#include<stdio.h>
#include<conio.h>
int main(){
	int table = 10,start,end = 10;
	clrscr();

	for(start=1;start<=end;start++)
	{
		printf("%d * %d = %d\n",table,start,table*start);
	}
	getch();
}