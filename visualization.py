import statistics as sts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#reads in the 3 arrays 
def vis() -> None:
    with open('data.txt') as f:
        tcpTimes = f.readline().strip('\n')
        timeToAck = f.readline().strip('\n')
        lengths = f.readline().strip('\n')

    #configures 1d array to a useable format 
    temp = tcpTimes.strip('[')
    temp = temp.strip(']')
    tcpTimes = temp.split(', ')
    tcpTimes = list(map(float, tcpTimes))

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
    plt.show()




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
    df = pd.DataFrame(timeToAck)
    df.plot(kind='box')
    df.plot(kind='kde')
    plt.show()

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
    print('Median packet byte size: ')
    print(sts.median(lengths))


    #visualizes data for 2 d array byte size per packet 
    print("\n")
    print("\n")
    print("NOW SHOWING BYTE SIZE PER PACKET, BOX PLOT AND DENSITY")
    print("              SAVE AND CLOSE TO CONTINUE              ")
    print("\n")
    print("\n")
    df = pd.DataFrame(lengths)
    df.plot(kind='box')
    df.plot(kind='kde')
    plt.show()