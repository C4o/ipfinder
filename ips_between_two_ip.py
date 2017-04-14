#
#   author:Leviathan
#   date:2017/4/5
#
import struct
import socket
import sys
import os
def findIPs(start, end):
    if os.path.isfile("ips_from_"+start+"_to_"+end+".txt")==True:
    	os.remove("ips_from_"+start+"_to_"+end+".txt")
    ips=open("ips_from_"+start+"_to_"+end+".txt","a")
    ipstruct = struct.Struct('>I')
    start, = ipstruct.unpack(socket.inet_aton(start))
    end, = ipstruct.unpack(socket.inet_aton(end))
    print "[+]start to list each valid ip od your range."
    for i in range(start, end+1):
        ip=socket.inet_ntoa(ipstruct.pack(i))
        ip_array=ip.split('.')
        if int(ip_array[3])==0 or int(ip_array[3])==255:
            pass
        else:
            ips.write(ip+'\n')
    ips.close()

def check_legality(ips1,ips2):
    ips1_array=ips1.split('.')
    ips2_array=ips2.split('.')
    try:
        if len(ips1_array)==4 and len(ips2_array)==4:
            res_flag=0
            for i in range(0,4,1):
                if int(ips1_array[i])>=0 and int(ips2_array[i])>=0 and int(ips1_array[i])<255 and int(ips2_array[i])<255:
                    res_flag=1
                    continue
                else:
                    res_flag=0
                    break
            if res_flag==1:
                print "[+]ip is legal."
                findIPs(ips1,ips2)
            elif res_flag==0:
                print "[-]ip is ILLEGAL."
                return False
    except Exception,e:
        print "[-]ip is ILLEGAL:type."
        print "[-]"+e

try:
    ip1=sys.argv[1]
    ip2=sys.argv[2]
    check_legality(ip1,ip2)
except:
    if len(sys.argv)!=3:
        print "[-]Something's wrong with your input."
        print "[!]Example:python x.py 10.0.0.1 10.0.0.2"