import statistics as sts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#reads in the 3 arrays

def tcpTimesHelper(tcpTimes):
    temp = tcpTimes.strip('[')
    temp = temp.strip(']')
    tcpTimes = temp.split(', ')
    print(tcpTimes)
    return list(map(float, tcpTimes))
def timeToAckHelper(timeToAck):
    temp = timeToAck.strip('[')
    temp = temp.strip(']')
    temp = temp.replace('[', '')
    temp = temp.replace(']', '')
    timeToAck = temp.split(', ')
    x = timeToAck.count('')
    for i in range(x):
        timeToAck.remove('')
    return list(map(float, timeToAck))
def lengthsHelper(lengths): 
    temp = lengths.strip('[')
    temp = temp.strip(']')
    temp = temp.replace('[', '')
    temp = temp.replace(']', '')
    lengths = temp.split(', ')
    x = lengths.count('')
    for i in range(x):
        lengths.remove('')
    return list(map(float, lengths))

def vis() -> None:
    with open('data.txt') as f:
        tcpTimes = f.readline().strip('\n')
        timeToAck = f.readline().strip('\n')
        lengths = f.readline().strip('\n')

    #configures 1d array to a useable format 
    print(tcpTimes)
    tcpTimes = tcpTimesHelper(tcpTimes)

    #prints 3 imoprtant values for 1 d array  

    print('Minimum time for total TCP stream: ') 
    print(min(tcpTimes))                            
    print('Maximum time for total TCP stream: ')
    print(max(tcpTimes))
    print('Mean time for total TCP stream: ')
    print(sts.mean(tcpTimes))
    print('Median time for total TCP stream: ')
    print(sts.median(tcpTimes))



    print("\n")
    print("\n")
    print("NOW SHOWING TOTAL TCP STREAM TIME, BOX PLOT AND DENSITY")
    print("              SAVE AND CLOSE TO CONTINUE               ")
    print("\n")
    print("\n")

    #visualizes data for 1 d array, total tcp stream time: box plot and density
    s = pd.DataFrame(tcpTimes)
    s.plot(kind='box')
    s.plot(kind='kde')
    plt.xlim([0,.15])
    plt.show()




    #configures 2d array1 packet time to ack to a useable format 
    timeToAck = timeToAckHelper(timeToAck)

    #prints the 3 desired values for 2d array1 packet time to ack

    print('Minimum time for RTT to ACK segment per packet: ') 
    print(min(timeToAck))                           
    print('Maximum time for RTT to ACK segment per packet: ')
    print(max(timeToAck))
    print('Mean time for RTT to ACK segment per packet: ')
    print(sts.mean(timeToAck))
    print('Median time for RTT to ACK segment per packet: ')
    print(sts.median(timeToAck))

    #visualizes data for 2 d array packet rtt to ACK: box plot and density
    print("\n")
    print("\n")
    print("NOW SHOWING RTT TO ACK PER PACKET, BOX PLOT AND DENSITY")
    print("              SAVE AND CLOSE TO CONTINUE               ")
    print("\n")
    print("\n")
    plt.xlim([0,60000])
    df = pd.DataFrame(timeToAck)
    df.plot(kind='box')
    df.plot(kind='kde')
    plt.show()

    #configures 2d array2 packet byte size to a useable format
    lengths = lengthsHelper(lengths)

    #prints the 3 desired values for 2d array2 packet byte size

    print('Minimum packet byte size: ') 
    print(min(lengths))                            #prints the 3 desired values for 1 d array 
    print('Maximum packet byte size: ')
    print(max(lengths))
    print('Mean packet byte size: ')
    print(sts.mean(lengths))
    print('Median packet byte size: ')
    print(sts.median(lengths))


    #visualizes data for 2 d array byte size per packet 
    print("\n")
    print("\n")
    print("NOW SHOWING BYTE SIZE PER PACKET, BOX PLOT AND DENSITY")
    print("              SAVE AND CLOSE TO CONTINUE              ")
    print("\n")
    print("\n")
    plt.xlim([0,20000])
    df = pd.DataFrame(lengths)
    df.plot(kind='box')
    df.plot(kind='kde')
    plt.show()

def vis3() -> None:
    with open('data0.txt') as f:
        tcpTimes0 = tcpTimesHelper(f.readline().strip('\n'))
        timeToAck0 = timeToAckHelper(f.readline().strip('\n'))
        lengths0 = lengthsHelper( f.readline().strip('\n'))
    f.close()
    with open('data1.txt') as f:
        tcpTimes1 = tcpTimesHelper(f.readline().strip('\n'))
        timeToAck1 = timeToAckHelper(f.readline().strip('\n'))
        lengths1 = lengthsHelper(f.readline().strip('\n'))
    f.close()
    with open('data2.txt') as f:
        tcpTimes2 = tcpTimesHelper(f.readline().strip('\n'))
        timeToAck2 = timeToAckHelper(f.readline().strip('\n'))
        lengths2 = lengthsHelper(f.readline().strip('\n'))
    f.close()
    #prints 3 imoprtant values for 1 d array  
    print("\n")
    print("\n")
    print("NOW SHOWING TOTAL TCP STREAM TIME, BOX PLOT AND DENSITY")
    print("              SAVE AND CLOSE TO CONTINUE               ")
    print("\n")
    print("\n")
    #visualizes data for 1 d array, total tcp stream time: box plot and density

    s = pd.DataFrame(tcpTimes0)
    s1 = pd.DataFrame(tcpTimes1)
    s2 = pd.DataFrame(tcpTimes2)

    ax = s.plot(kind="kde")
    ax = s1.plot(ax=ax,kind="kde")
    s2.plot(ax =ax, kind="kde")
    plt.xlim([0,.15])
    plt.ylim([0,25])
    plt.show()




    #configures 2d array1 packet time to ack to a useable format 

    #prints the 3 desired values for 2d array1 packet time to ack

    #visualizes data for 2 d array packet rtt to ACK: box plot and density
    print("\n")
    print("\n")
    print("NOW SHOWING RTT TO ACK PER PACKET, BOX PLOT AND DENSITY")
    print("              SAVE AND CLOSE TO CONTINUE               ")
    print("\n")
    print("\n")
    s = pd.DataFrame(timeToAck0)
    s1 = pd.DataFrame(timeToAck1)
    s2 = pd.DataFrame(timeToAck2)

    ax = s.plot(kind="kde")
    ax = s1.plot(ax=ax,kind="kde")
    s2.plot(ax =ax, kind="kde")
    plt.xlim([0,60000])
    plt.ylim([0,0.00008])
    plt.show()
    #configures 2d array2 packet byte size to a useable format

    #prints the 3 desired values for 2d array2 packet byte size


    #visualizes data for 2 d array byte size per packet 
    print("\n")
    print("\n")
    print("NOW SHOWING BYTE SIZE PER PACKET, BOX PLOT AND DENSITY")
    print("              SAVE AND CLOSE TO CONTINUE              ")
    print("\n")
    print("\n")

    s = pd.DataFrame(lengths0)
    s1 = pd.DataFrame(lengths1)
    s2 = pd.DataFrame(lengths2)

    ax = s.plot(kind="kde")
    ax = s1.plot(ax=ax,kind="kde")
    s2.plot(ax =ax, kind="kde")
    plt.xlim([0,10000])
    plt.ylim([0,.0006])
    plt.show()
    
    df = pd.DataFrame({'Total Throughput in bytes/second':['Cap1', 'Cap2', 'Cap3'], 'bytes/s':[sum(lengths0)/sum(tcpTimes0), sum(lengths1)/sum(tcpTimes1), sum(lengths2)/sum(tcpTimes2)]})
    ax = df.plot.bar(x='Total Throughput in bytes/second', y='bytes/s', rot=0,color="red")
    plt.ylim([0,30000000])
    plt.show()
if __name__ == "__main__":
    vis3()