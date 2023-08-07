from threading import local
from flask import Flask,jsonify,redirect,request,Response
import pyshark
import time
import asyncio
import json

app = Flask(__name__)


@app.route("/saveascsv",methods = ["POST"])
async def saveascsv():
    networkI = request.get_json()
    print(networkI)

    capture = pyshark.LiveCapture(interface = networkI)

    for packet in capture.sniff(1):
        try:
            localtime = time.asctime(time.localtime(time.time()))
            protocol = packet.transport_layer
            src_addr = packet.ip.src
            src_port = packet[protocol].srcport
            dst_addr = packet.ip.dst
            dst_port = packet[protocol].dstport
            data = {
                "loacltime" : localtime,
                "protocol" : protocol,
                "src_addr" : src_addr,
                "src_port" : src_port,
                "dst_addr" : dst_addr,
                "dst_port" : dst_port
            }
        except AttributeError as e:
            print (" ")
    return data


if __name__ == "__main__":
    app.run(debug=True)