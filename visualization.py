import statistics as sts

#reads in the 3 arrays 
with open('data.txt') as f:
    tcpTimes = f.readline().strip('\n')
    timeToAck = f.readline().strip('\n')
    lengths = f.readline().strip('\n')

#configures 1d array to a useable format 
temp = tcpTimes.strip('[')
temp = temp.strip(']')
tcpTimes = temp.split(', ')
tcpTimes = list(map(float, tcpTimes))

 #prints the 3 desired values for 1 d array 

print('Minimum time for total TCP stream: ') 
print(min(tcpTimes))                            #prints the 3 desired values for 1 d array 
print('Maximum time for total TCP stream: ')
print(max(tcpTimes))
print('Mean time for total TCP stream: ')
print(sts.mean(tcpTimes))

#configures 2d array1 packet time to ack to a useable format 

temp = timeToAck.strip('[')
temp = temp.strip(']')
temp = temp.replace('[', '')
temp = temp.replace(']', '')
timeToAck = temp.split(', ')
x = timeToAck.count('')
for i in range(x):
    timeToAck.remove('')
timeToAck = list(map(float, timeToAck))

#prints the 3 desired values for 2d array1 packet time to ack

print('Minimum time for RTT to ACK segment per packet: ') 
print(min(timeToAck))                            #prints the 3 desired values for 1 d array 
print('Maximum time for RTT to ACK segment per packet: ')
print(max(timeToAck))
print('Mean time for RTT to ACK segment per packet: ')
print(sts.mean(timeToAck))

#configures 2d array2 packet byte size to a useable format

temp = lengths.strip('[')
temp = temp.strip(']')
temp = temp.replace('[', '')
temp = temp.replace(']', '')
lengths = temp.split(', ')
x = lengths.count('')
for i in range(x):
    lengths.remove('')
lengths = list(map(float, lengths))

#prints the 3 desired values for 2d array2 packet byte size

print('Minimum packet byte size: ') 
print(min(lengths))                            #prints the 3 desired values for 1 d array 
print('Maximum packet byte size: ')
print(max(lengths))
print('Mean packet byte size: ')
print(sts.mean(lengths))