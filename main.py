import pyshark
import time
import psutil
from tkinter import *
from tkinter import messagebox

def capture_packet_wireshark():
    global Information
    Information = Tk()
    root.geometry("500x500+0+0")
    root.title(" Info ")

    networkInterface = clicked.get()
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

            labels = [localtime,protocol,src_addr,src_port,dst_addr,dst_port]
            # for i in labels:
            #     curr_label = "label" + str(i) 
            #     curr_label = Label(Information,text = curr_label[i])
            #     curr_label.grid(row = i , column = 0 , )

            print ("%s IP %s:%s <-> %s:%s (%s)" % (localtime, src_addr, src_port, dst_addr, dst_port, protocol))
        except AttributeError as e:
             pass
        print (" ")


def session():
    global root
    global clicked
    root=Tk()
    clicked = StringVar()
    addrs = psutil.net_if_addrs() 

    networkInterfaces = list(addrs.keys())

    root.geometry("500x500+0+0")
    root.title(" WELCOME ")
    clicked.set("Select One of the following Interfaces")
    OptionMenu(root,clicked,*networkInterfaces).pack()
    Button(root , text = "SCAN" , command = capture_packet_wireshark).pack()
    root.mainloop()

session()