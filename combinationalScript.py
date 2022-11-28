import pyshark
import wiresharkScript
import visualization
if __name__ == '__main__':
    capture_ls = ["/capture1.pcapng","/capture2.pcapng","/capture3.pcapng"]

    lengths = []
    time_to_ack = []
    total_transm_time = []

    data_tuple = (lengths,time_to_ack,total_transm_time)
    for cap in capture_ls:
        print('started')
        ls = wiresharkScript.ws_main(cap)
        data_tuple[0].append(ls[0])
        data_tuple[1].append(ls[1])
        data_tuple[2].append(ls[2])
        print('looped')
    
    f = open("data.txt", "a") #writes data to file
    f.write(str(data_tuple[0]))
    f.write("\n~~\n")
    f.write(str(data_tuple[1]))
    f.write("\n~~\n")
    f.write(str(data_tuple[2]))
    f.close()

    visualization.vis()