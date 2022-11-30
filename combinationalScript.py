import pyshark
import wiresharkScript
import visualization
if __name__ == '__main__':
    capture_ls = ["capture1.pcapng","capture2.pcapng","capture3.pcapng"]

    i = 0
    for cap in capture_ls:
        print('started')

        ls = wiresharkScript.ws_main(cap)

        f = open(f"data{str(i)}.txt", "a") #writes data to file
        f.write(str(ls[0]))
        f.write("\n")
        f.write(str(ls[1]))
        f.write("\n")
        f.write(str(ls[2]))
        f.close()

        print('looped')
        i+=1
    
    visualization.vis3()