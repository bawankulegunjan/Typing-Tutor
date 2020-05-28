#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<unistd.h>

void *hello (void *arg){
	while(1){
		sleep(1);
		printf("Hello world\n");
	}
	return NULL;
}


int main(){
	pthread_t *thread_id;
	pthread_create(&thread_id,NULL,hello,NULL);
	
 	pthread_join(thread_id,NULL);
	return 0;
}
