import sys
import random
import socketio
import time
from datetime import datetime, timezone
#idVemec = sys.argv[1]
vemec = {
    "data_historial": {}
}

import socketio
time.sleep(5)

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('connection established')

sio.connect('http://middleware:8088')

async def message(vemec):
    await sio.emit('messages', vemec)

 
while True:
    vemec["vemec_id"] = 1#idVemec
    vemec["data_historial"]["presionMin"] = random.randrange(0,50)
    vemec["data_historial"]["presionMax"] = random.randrange(0,50)
    vemec["data_historial"]["volGas"] = random.randrange(0,50)
    vemec["data_historial"]["freqAporte"] = random.randrange(0,50)
    vemec["data_historial"]["porcenMezclaO2"] = random.randrange(0,50)
    vemec["data_historial"]["humedadAire"] = random.randrange(0,50)
    vemec["data_historial"]["tempSalidaAire"] = random.randrange(0,50)
    vemec["data_historial"]["tempEntradaAire"] = random.randrange(0,50)
    vemec["data_historial"]["presionEntradaAire"] = random.randrange(0,50)
    vemec["data_historial"]["presionSalidaAire"] = random.randrange(0,50)
    vemec["data_historial"]["timestamp"] = str(datetime.now().today().strftime('%Y-%m-%d %H:%M:%S')) 
    sio.emit('messages', vemec)    
    time.sleep(1)
 
