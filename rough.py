import pyshark
cap = pyshark.LiveCapture(interface="eth0")
for packet in cap.sniff_continuously():
 print(packet)
# cap2 = pyshark.FileCapture(networklog)
# packet = cap2[0]
# # print(packet)
# protonums = {1: "ICMP",
#  6: "TCP",
#  17: "UDP",
#  58: "IPv6-ICMP"}
# ip_layer = packet.layers[1]
# protocol = None
# src_addr = ip_layer.src
# dst_addr = ip_layer.dst
# if ip_layer.version == "4":
#  protocol = ip_layer.proto
# elif ip_layer.version == "6":
#  protocol = ip_layer.nxt
#  print("src_addr:" ,src_addr,
#     "\ndst_addr:", dst_addr,
#     "\nprotocol:", protonums.get(int(protocol), protocol))