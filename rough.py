import pyshark
import time
import psutil
import openpyxl
addrs = psutil.net_if_addrs() 
wb = openpyxl.Workbook() 
sheet = wb.active
def cellEntry(row, column, attribute):
    new_cell = sheet.cell(row, column)
    new_cell.value = str(attribute)

networkInterfaces = list(addrs.keys())
print(networkInterfaces)
networkInterface="Wi-Fi"
capture = pyshark.LiveCapture(interface=networkInterface)
print("listening on %s" % networkInterface)


cellEntry(1,1,"Localtime")
cellEntry(1,2,"Source IP")
cellEntry(1,3,"Source Port")
cellEntry(1,4,"Destination IP")
cellEntry(1,5,"Destination Port")
cellEntry(1,6,"Protocol")

row1 = 2
live=capture.sniff(timeout=10)
for packet in live:
    # time.sleep(1)
    try:
        
        localtime = time.asctime(time.localtime(time.time()))
        cellEntry(row1,1,localtime)
        protocol = packet.transport_layer
        cellEntry(row1,6,protocol)
        src_addr = packet.ip.src 
        cellEntry(row1,2,src_addr)           
        src_port = packet[protocol].srcport   
        cellEntry(row1,3,src_port)
        dst_addr = packet.ip.dst
        cellEntry(row1,4,dst_addr)     
        dst_port = packet[protocol].dstport 
        cellEntry(row1,5,dst_port)
        wb.save("log.csv")
        row1=row1+1
        print ("%s IP %s:%s <-> %s:%s (%s)" % (localtime, src_addr, src_port, dst_addr, dst_port, protocol))
    except AttributeError as e:
        pass
    print (" ")