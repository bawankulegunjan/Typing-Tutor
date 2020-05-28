#include<stdio.h>
#include<string.h>
void cpy_str(char *a){
	char str[20];
	strcpy(str,a);	
}

int main(){
	char a[51];
	int i;
	for(i = 0; i<50; i++){
		a[i] = 'A';
	}
	cpy_str(a);
	return 0;
}
