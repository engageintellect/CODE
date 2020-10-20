import speedtest
import subprocess
from time import sleep


st=speedtest.Speedtest()


def clear():
    subprocess.call('clear', shell=True)

def scan():
    clear()
    
    print("STARTING SCAN...")
    sleep(1)
    servernames = []
    
    print("FINDING FASTEST SERVER...")
    st.get_best_server(servernames)
    
    print("MEASUING DOWNLOAD SPEED...")
    download = float(st.download()/(1024*1024))
   
    print("MEASUING UPLOAD SPEED...\n\n")
    upload = float(st.upload()/(1024*1024))

    print("MEASUING PING...")
    ping = float(st.results.ping)




    print("DOWNLOAD:  ", "%.2f" % download, "mbps")
    print("UPLOAD:    ", "%.2f" % upload, "mbps")
    print("PING:      ", "%.2f" % ping, "ms")



scan()
