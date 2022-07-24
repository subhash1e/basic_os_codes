/*
What fork does is create a child process and start processing after fork() is invoked
return integer -  id of child process | 0 for parent process

Wonder how it has been implemented. 

*/

#include <stdio.h>
#include<unistd.h>

int main(void) {
  
    int pid = fork();
    int id = fork();
 
    printf("\nPID : %d , and ID : %d \n",pid,id);
    printf("end of main()\n");
    
	return 0;
}
/*
Four process will run, p1, p1 -> p1,p2 then 2nd fork , p1->p1,p3 and , p2 -> p2, p3

p1,p2,p3 and p4

op // 

PID : 25598 , and ID : 25599 
end of main()

PID : 25598 , and ID : 0 
end of main()

PID : 0 , and ID : 25600 
end of main()

PID : 0 , and ID : 0 
end of main()

-- stay confused figuring this out ,
  
    pid!=0 -> p2 and pid==0 -> p1 ,
    id!=0 -> p3 and p4, id==0 -> p2

-- actually op is random order

*/
