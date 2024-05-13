#include<stdio.h>
#include<conio.h>
int main(){
	int table = 10,start = 1,end = 10;
	clrscr();

	do{
		printf("%d * %d = %d\n",table,start,table*start);
		start+=1;
	}while(start<=10);
	getch();
}