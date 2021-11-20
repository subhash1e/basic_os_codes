'''
 SCAN algorithm
 for Disk scheduling operation.
'''
#ASSUME DISK SIZE = 400 [0...399]
#at starting head is at track no. 100
#requested queue contains track no.s

direction = 'right'#default
head, disk_size = 100, 400
arr = [200,300,100,50,90,80,95,150,55,120]
init_head = head
########################################
if disk_size - head > head : 
	direction = 'left'#as going to right first is costly
seek_count,cur_track = 0,0

left , right , seek_array = [], [], []
if direction == 'right':
	right.append(disk_size-1)
else:
	left.append(0)

for xx in arr:
	if xx < head:
		left.append(xx)
	if xx > head:
		right.append(xx)
left.sort(reverse = True) #sorted in reverse order
right.sort()
run = 2
while run:
	run -= 1
	if direction == 'left':
		for xx in left :
			cur_track = xx
			seek_array.append(cur_track)
			seek_count += abs(cur_track - head)
			head = cur_track
		direction = 'right'
	else :
		for xx in right:
			cur_track = xx
			seek_array.append(cur_track)
			seek_count += abs(cur_track - head)
			head = cur_track
		direction = 'left'
#############################################
print("Total seek operations = ", seek_count);

print("Initial head position was at :", init_head)
print("SCAN order seek sequence is ",*seek_array)
#########################################################

'''
Total seek operations =  400
Initial head position was at : 100
SCAN order seek sequence is  95 90 80 55 50 0 120 150 200 300
[Finished in 58ms]
'''
