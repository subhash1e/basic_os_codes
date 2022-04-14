#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

//thread executes a function whatever assigned to it

void* routine(){
    printf("||Front|||\n");
    sleep(3);
    printf("||Back |||\n");
}
int main(){

    //info about thread is stored in t1 variable
    pthread_t t1,t2;

    //to check thread is created succssfully
    //sometimes resources scarcity or permission leads to failure

    
    if(pthread_create(&t1, NULL, &routine, NULL)!=0){
        perror("thread creation failed\n");
        return 1;
    };
    if(pthread_create(&t2, NULL, &routine, NULL)!=0){
        perror("thread creation failed\n");
        return 1;
    };

    //waits till thread ends its processing
    pthread_join(t1, NULL);
    return 0;

}
