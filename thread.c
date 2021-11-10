#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <pthread.h>

void* routine(){
	int test = 0;
}
int main()
{
// this code is for recording time to create 100k child threads
	clock_t begin,end;
	double time_spent;
	begin = clock();
	
	//----------------------
  // creating 100,000 threads 
	pthread_t th[100000];

	for (int i = 0; i < 100000; ++i)
	{
		if(pthread_create(th+i, NULL , &routine, NULL)!=0){
			printf("Error creating thread\n");
			return 1;
		}
	
	}
	for (int i = 0; i < 100000; ++i)
	{
		if(pthread_join(th[i],NULL)!=0){
			printf("Error joining thread\n");
			return 2;	
		}
	}
	


	//-------------------------
	end = clock();
	time_spent = (double)(end-begin)/CLOCKS_PER_SEC;

	printf("time taken to create 100,000 child threads: %f\n",time_spent  );

	return 0;
}

// cmd for running : gcc -g -pthread thread.c 
