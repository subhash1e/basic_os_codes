'''
b)
 Write a python program to simulate
 CSCAN algorithm
 for Disk scheduling operation.
'''
#ASSUME DISK SIZE = 400 [0...399]
#at starting head is at track no. 100
#requested queue contains track no.s


head, disk_size = 100, 400
arr = [200,300,100,50,90,80,95,150,55,120]
seek_count,cur_track = 0,0
init_head = head
########################################

left , right , seek_array = [], [], []
right.append(disk_size-1)
left.append(0)

for xx in arr:
	if xx < head:
		left.append(xx)
	if xx > head:
		right.append(xx)
left.sort() #sorted in reverse order
right.sort()
for xx in right:
	cur_track = xx
	seek_array.append(cur_track)
	seek_count += abs(cur_track - head)
	head = cur_track
head = 0
for xx in left :
	cur_track = xx
	seek_array.append(cur_track)
	seek_count += abs(cur_track - head)
	head = cur_track

#############################################
print("Total seek operations = ", seek_count);
print("Initial head position was at :", init_head)
print("SSTF order seek sequence is ",*seek_array)