import speedtest
import subprocess
from time import sleep

subprocess.call('clear', shell=True)

st=speedtest.Speedtest()

def main():
    scan()

def scan():
    option = int(input('''COOSE OPTION TO MEASURE:
    
    [1] FULL TEST
    [2] DOWNLOAD
    [3] UPLOAD
    [4] PING
        
    [0] EXIT
    
    

    : '''))

    print('\n\n')

    if option == 0:
        subprocess.call('clear', shell=True)
        quit()

    if option == 1:
        servernames = []
        st.get_best_server(servernames)
        print("DOWNLOAD: ", st.download()/(1024*1024), "mbps")
        print("UPLOAD:   ", st.upload()/(1024*1024), "mbps")
        print("PING:     ", st.results.ping)

    elif option == 2:
        print(st.download()/(1024*1024), "mbps")
    elif option == 3:
        print(st.upload()/(1024*1024), "mbps")
    elif option == 4:
        servernames = []
        st.get_best_server(servernames)
        print("PING: ", st.results.ping, "ms")
    else:
        print("Please enter a correct option!")
        scan()

    sleep(10)
    main()

    






main()
