'''
b)
 Write a python program to simulate
 SSTF (Shortest seek time first) algorithm
 for Disk scheduling operation.
'''

#requested queue contains track no.s
arr = [200,300,100,50,90,80,95,150,55,120]
#at starting head is at track no. 100
head = 100
size = len(arr)
seek_count = 0
seek_array = []
diff = [0]*size
init_head = head
##################################
for i in range(size):
	diff[i] = [0,0]


for i in range(size):
	seek_array.append(head)

	for j in range(size) :
		diff[j][0] = abs(arr[j]-head)

	minimum = 999999
	index = -1
	for j in range(size):
		if diff[j][1] == 0 and minimum > diff[j][0]:
			minimum = diff[j][0]
			index = j
	diff[index][1] = 1
	seek_count += minimum
	head = arr[index]
	
seek_array.append(head)
########################################

print("Total seek operations = ", seek_count);
print("Initial head position was at :", init_head)
print("SSTF order seek sequence is ",*seek_array)