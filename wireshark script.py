import pyshark
import time
import nest_asyncio
nest_asyncio.apply()

# need Frame Length (bytes), Time since First Frame, RTT to ACK segment
start = time.time()

lengths = [] # 2d array
time_to_ack = [] # 2d array
total_transm_time = [] # 1d array


def data(cap) -> None:
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

for i in range(19):    
    cap = pyshark.FileCapture('C:/Users/Z/Desktop/capture2.pcapng', display_filter="tcp.stream eq " + str(i))
    data(cap)

print(total_transm_time)
print(time_to_ack)
print(lengths)

f = open("data.txt", "a")
f.write(str(total_transm_time))
f.write("\n")
f.write(str(time_to_ack))
f.write("\n")
f.write(str(lengths))
f.close()

print(time.time()-start)


#cap1 = pyshark.FileCapture('C:/Users/Z/Desktop/capture2.pcapng', display_filter="tcp.stream eq 2")
#print(cap1[2].tcp.field_names) #analysis_acks_frame, time_delta, .length