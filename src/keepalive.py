# -*- coding: utf-8 -*-
"""
Created on 2018/5/15

@author: Simba
"""

import websocket
import thread
import time
import json
import os


def on_message(ws, message):
    #print message
    # print json.loads(message)
    # if json.loads(message)["Type"] == "UPDATE":
    #     print message
    resDic = json.loads(message)
    print resDic
    # filePath = os.path.join(r"F:\testMessage",resDic["PersonId"])
    filePath = os.path.join(r"/simba_monitor", resDic["PersonId"])
    with open(filePath, 'a') as f:
        # timeStr = str(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime()))
        timeStr = str(int(round(time.time() * 1000)))
        line = timeStr + "    " + message + "\n"
        f.write(line)




def on_error(ws, error):
    print error


def on_close(ws):
    print "### closed ###"


def on_open(ws):
    def run(*args):
        for i in range(30000):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print "thread terminating..."

    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://118.89.213.123:8008/wsconnect?appkey=AK-StressTest&appsecret=SK-StressTest&debug=true",
                                on_message=on_message,
                                # on_error=on_error,
                                # on_close=on_close
                                )
    #ws.on_open = on_open

    ws.run_forever()
