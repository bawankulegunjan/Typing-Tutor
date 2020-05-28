#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

void *hello (void *arg){
	while(1)
	{
		sleep(1);
		printf("Hello world\n");
	}
	return NULL;
}

void goodbye(){
	while(1)
	{
		sleep(2);
		printf("Goodbye world\n");
	}
}

int main(){
	pthread_t newthread;
	int err = pthread_create(&newthread,NULL,hello,NULL);
	goodbye();
	err = pthread_join(&newthread,NULL);
	return 0;
}
