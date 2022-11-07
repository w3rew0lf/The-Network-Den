from threading import local
from flask import Flask,jsonify,redirect,request,Response
import pyshark
import time
import nest_asyncio
nest_asyncio.apply()


app = Flask(__name__)


@app.route("/saveascsv",methods = ["POST"])
async def saveascsv():
    global capture
    networkI = request.get_json()
    networkInterface = str(networkI["networkInterface"])
    print(networkInterface)
    
    capture = pyshark.LiveCapture(interface = networkInterface)
    
    print(capture)
    for packet in capture.sniff_continuously():
        try:
            localtime = time.asctime(time.localtime(time.time()))
            protocol = packet.transport_layer   
            src_addr = packet.ip.src            
            src_port = packet[protocol].srcport   
            dst_addr = packet.ip.dst            
            dst_port = packet[protocol].dstport   
            print ("%s IP %s:%s <-> %s:%s (%s)" % (localtime, src_addr, src_port, dst_addr, dst_port, protocol))
            time.sleep(3)
        except AttributeError as e:
            pass
            print (" ")
        

if __name__ == "__main__":
    app.run(debug=True)