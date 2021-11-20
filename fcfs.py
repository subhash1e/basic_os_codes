'''

FCFS algorithm for Disk scheduling operation

'''

#requested queue contains track no.s
arr = [200,300,100,50,90,80,95,150,55,120]
#at starting head is at track no. 100
head = 100
seek_count = 0
init_head = head
#########################################
for xx in arr:
	cur_track = xx;
	seek_count += abs(cur_track - head)
	head = cur_track

#######################################
print("Total seek operations = ", seek_count);
print("Initial head position was at :", init_head)
print("fcfs order seek sequence is ",*arr)


##########################
'''
Total seek operations =  730
Initial head position was at : 100
fcfs order seek sequence is  200 300 100 50 90 80 95 150 55 120
[Finished in 60ms]
'''
