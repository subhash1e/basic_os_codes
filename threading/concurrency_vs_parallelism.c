/*
parallelism vs concurrency

term used interchangibly but they are not same

-> parallel doesn't interfere with others 
-> use diff memory for each thread, so work is efficiently done


->,but concurrency can interfare 


-> all threads are concurrent and uses same memory


more parallelism more efficient
more concurrent less efficient
*/

#define THREAD_NUM 2

int primes[10] = {2,3,5,7,11,13,17,19,23,29};


int mails=0;
ptread_mutex_t mutex;
void* routine(void* _arg){
  for(int i=0; i< 10; i++){
    phread_mutex_lock(&mutex);
    mails++;
    printf("Processing...  MAIL #%d\n",mails);
    sleep(1);
    pthread_mutex_unlock(&mutex);
  }
}

int main(){
// creae pthread


}

