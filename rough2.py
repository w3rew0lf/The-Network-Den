import pyshark
import time
networkInterface = "eth0"
capture = pyshark.LiveCapture(interface=networkInterface)
print("listening on %s" % networkInterface)
for packet in capture.sniff_continuously():
    try:
        localtime = time.asctime(time.localtime(time.time()))
        protocol = packet.transport_layer   
        src_addr = packet.ip.src            
        src_port = packet[protocol].srcport   
        dst_addr = packet.ip.dst            
        dst_port = packet[protocol].dstport   
        print ("%s IP %s:%s <-> %s:%s (%s)" % (localtime, src_addr, src_port, dst_addr, dst_port, protocol))
    except AttributeError as e:
        pass
    print (" ")