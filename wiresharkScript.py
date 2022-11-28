import pyshark
import time
import nest_asyncio
nest_asyncio.apply()

lengths = [] # 2d array of byte sizes per packet
time_to_ack = [] # 2d array of RTT to ACK segment per packet
total_transm_time = [] # 1d array of transmission time per TCP stream

def packet_loop(cap) -> None:
    '''Loops through packets in TCP stream until none remain, appends data to lists'''
    local_len = []
    local_ack = []
    local_transm_time = -1
    try: 
        i = 0
        while True:
            local_len.append(int(cap[i].length))
            local_transm_time = float(cap[i].tcp.time_delta)
            try:
                local_ack.append(float(cap[i].tcp.analysis_acks_frame))
            except:
                pass
            i+=1
    except:
        lengths.append(local_len)
        time_to_ack.append(local_ack)
        total_transm_time.append(local_transm_time)

def writ_loop(start) -> None:
    '''Prints data and runtime on terminal, and writes data to a file "data.txt"'''
    print(total_transm_time) #prints data to terminal
    print(time_to_ack)
    print(lengths)

    f = open("data.txt", "a") #writes data to file
    f.write(str(total_transm_time))
    f.write("\n~~\n")
    f.write(str(time_to_ack))
    f.write("\n~~\n")
    f.write(str(lengths))
    f.close()

    print('Runtime: ' + str(time.time() - start)) #prints runtime

def over_loop(rng: int, cap_location: str):
    '''Loops through n-1 TCP streams specified by rng in file at address cap_location'''
    for i in range(rng):
        #Reopening file per loop is most likely cause of slow runtime TODO: find way to refresh filter versus reopening file n-1 times?    
        cap = pyshark.FileCapture(cap_location, display_filter="tcp.stream eq " + str(i))
        packet_loop(cap)

def ws_main(cap_location) -> tuple:
    # need Frame Length (bytes), Time since First Frame, RTT to ACK segment
    start = time.time() #program starting time for measuring runtime

    rng = 19 # rng = n-1 number of TCP streams to loop through
    #cap_location = '' #Address for capture file, overwritten by function call for time being; TODO: add check for if a .pcapng is in directory

    over_loop(rng, cap_location)
    writ_loop(start)
    return (lengths, time_to_ack, total_transm_time)
