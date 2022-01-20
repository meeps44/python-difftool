import subprocess
#import time #for sleep(n) if necessary
#import threading #TODO: implement multithreading - https://www.programiz.com/python-programming/time/sleep

hostnames = [
	"google.com",
	"youtube.com"
	]
#ip_addresses = [] #hostnames vs IP-addresses


for i in hostnames:
    print("Running Paris-Traceroute subprocess towards URL %s\n", i)
    subprocess.Popen([])
    subprocess.run(['./paris-traceroute', 'T', i], shell=True) 
    #subprocess.run(['./paris-traceroute', 'T', i], shell=True, capture_output=True) 

#for i in ip_addresses:
#    print("Launching subprocess\n")
#    subprocess.run(['./paris-traceroute-2', 'T', i])