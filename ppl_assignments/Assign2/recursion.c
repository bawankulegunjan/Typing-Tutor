#include<stdio.h>

int fact(int a){
	if(a == 1 || a == 0)
		return 1;
	else 
		return a*fact(a-1);
}

int main(){
	int n, res;
	printf("Enter the value of n:\n");
	scanf("%d",&n);
	res = fact(n);
	printf("Factorial is:%d\n",res);
	return 0;
}
