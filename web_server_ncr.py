# from fastapi import FastAPI
# import serial
# import time
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# origins = ['*']

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.get("/{device_port}")
# async def root(device_port:str):
#     try:
#         ser = serial.Serial(
#             port = device_port,
#             timeout = 1,
#             baudrate=9600,
#             parity=serial.PARITY_EVEN,
#             stopbits=serial.STOPBITS_ONE,
#             bytesize=serial.SEVENBITS,
#         )
#         i = True

#         while i:
#             # if wt == 'S14\x0D':
#                 ser.write('S14\x0D'.encode('utf-8'))
#                 print("connected")
#                 # ser.write('\x05'.encode('utf-8'))
#                 # time.sleep(1)
#                 weight=None
#                 read_val = ser.read(size=64)
#                 read_val = str(read_val, 'UTF-8')  
#                 res = list(read_val)
#                 print(res)
#                 if '4' in res[3]:

#                                 # weight = read_val.split('S144')[1].split('\r')[0]
#                     weight = read_val[4:-1]
#                     print(weight)
#                             # weight ="Sacale Unsable"
#                 elif "S141" in read_val:
#                     weight ="unstable"
#                 elif "S142" in read_val:
#                     weight ="Overload"
#                 elif "S143" in read_val:
#                     weight ="Zero"
#                 elif "S145" in read_val:
#                     weight ="Underload"
#                 print(read_val)
#                     # else:
#                     #     print("else")
#                     #     weight ="Undefined Error. Please Check the Device connectivity"
#                     # weight= read_val[read_val.find("\r\n")+2:read_val.find("\r\n")+9]
#                     # print(type(read_val))
#                 ser.close()
#                 return {"weight": weight}
#     except:           
#             return {"message": "No Device Connected"}
    
# @app.get("/barcode/{device_port}")
# async def root(device_port:str):
#     try:
#         ser = serial.Serial(
#             port = device_port,
#             timeout = 1,
#             baudrate=9600,
#             parity=serial.PARITY_EVEN,
#             stopbits=serial.STOPBITS_ONE,
#             bytesize=serial.SEVENBITS,
#         )
#         i = True

#         while i:
#             # if wt == 'S14\x0D':
#                 ser.write('S01\x0D'.encode('utf-8'))
#                 print("connected")
#                 # ser.write('\x05'.encode('utf-8'))
#                 # time.sleep(1)
#                 barcode=None
#                 read_val = ser.read(size=64)
#                 read_val = str(read_val, 'UTF-8')  
#                 res = list(read_val)
#                 print(res)

#                 if len(res)>4:
#                     i=False
#                     # ["S","0","0","\r","S","0","8","F","F","5","0","3","1","2","6","1","\r"]
#                     # ["S","0","0","\r","S","0","8","A","0","1","1","4","3","3","1","5","3","6","8","\r"]
#                     barcode=res
#         ser.close()
#         return {"barcode": barcode}
                
#     except:           
#             return {"message": "No Barcode Device Connected"}
    

from fastapi import FastAPI
import serial
import time
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/{device_port}")
# async def root(device_port:str):
#     try:
#         ser = serial.Serial(
#             port = device_port,
#             timeout = 1,
#             baudrate=9600,
#             parity=serial.PARITY_EVEN,
#             stopbits=serial.STOPBITS_ONE,
#             bytesize=serial.SEVENBITS,
#         )
#         i = True

#         while i:
#             # ser.write('S14\x0D'.encode('utf-8'))
#             ser.write('\x05'.encode('utf-8'))
#             # time.sleep(1)
#             weight=None
#             read_val = ser.read(size=64)
#             if read_val != '':
#                 # print(read_val)
#                 # print(type(read_val))
#                 read_val = str(read_val, 'UTF-8')  
#                 # print(read_val)
#                 # print(type(read_val))
#                 if read_val.__contains__('S144'):
#                     weight = read_val.split('S144')[1].split('\r')[0]
#                     print(weight)
#                     # weight ="Sacale Unsable"
#                 elif read_val.__contains__('S142'):
#                     weight ="Overload"
#                 elif read_val.__contains__('S143'):
#                     weight ="Zero"
#                 elif read_val.__contains__('S145'):
#                     weight ="Underload"

#                 weight= read_val[read_val.find("\r\n")+2:read_val.find("\r\n")+9]
#                 # print(type(read_val))
#             ser.close()
#             return {"weight": weight}
#     except:
#         return {"message": "No Device Connected"}

@app.get("/{device_port}")
async def root(device_port:str):
    try:
        ser = serial.Serial(
            port = device_port,
            timeout = 1,
            baudrate=9600,
            parity=serial.PARITY_EVEN,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.SEVENBITS,
        )
        i = True

        while i:
            # if wt == 'S14\x0D':
                ser.write('S14\x0D'.encode('utf-8'))
                print("connected")
                # ser.write('\x05'.encode('utf-8'))
                # time.sleep(1)
                weight=None
                read_val = ser.read(size=64)
                print(read_val)
                read_val = str(read_val, 'UTF-8')  
                res = list(read_val)
                #print(res)
                if '4' in res[3]:

                                # weight = read_val.split('S144')[1].split('\r')[0]
                    weight = read_val[4:-1]
                    print(weight)
                            # weight ="Sacale Unsable"
                elif "S141" in read_val:
                    weight ="unstable"
                elif "S142" in read_val:
                    weight ="Overload"
                elif "S143" in read_val:
                    weight ="Zero"
                elif "S145" in read_val:
                    weight ="Underload"
                print(read_val)
                    # else:
                    #     print("else")
                    #     weight ="Undefined Error. Please Check the Device connectivity"
                    # weight= read_val[read_val.find("\r\n")+2:read_val.find("\r\n")+9]
                    # print(type(read_val))
                ser.close()
                return {"weight": weight}
    except:           
            return {"message": "No Device Connected"}
    
@app.get("/barcode/{device_port}")
async def getBarcode(device_port:str):
    try:
        print("Connecting device")
        ser = serial.Serial(
            port = device_port,
            timeout = 1,
            baudrate=9600,
            parity=serial.PARITY_EVEN,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.SEVENBITS,
        )
        # i = True

        # while i:
            # if wt == 'S14\x0D':
        ser.write('S01\x0D'.encode('utf-8'))
        print("connected")
        # ser.write('\x05'.encode('utf-8'))
        # time.sleep(1)
        #barcode=None
        read_val = ser.read(size=64)
        print(read_val)
        read_val = str(read_val, 'UTF-8')  
        res = list(read_val)
        #print(res)
        #['S', '0', '0', '\r', 'S', '0', '8', 'F', 'F', '5', '0', '3', '1', '2', '6', '1', '\r']
        # res = ["S","0","0","\r","S","0","8","A","0","1","1","4","3","3","1","5","3","6","8","\r"]
        res = res[4:-1]
        # if len(res)>0:
        #     i=False
        #     # ["S","0","0","\r","S","0","8","F","F","5","0","3","1","2","6","1","\r"]
        #     # ["S","0","0","\r","S","0","8","A","0","1","1","4","3","3","1","5","3","6","8","\r"]
        #     barcode=res
        print(''.join(res))
        ser.close()
        return {"barcode": ''.join(res)}
        # return {"barcode": barcode}
                
    except:
       
        return {"message": "No Barcode Device Connected"}
    
@app.get("/barcode/stop/{device_port}")
async def getBarcodeStop(device_port:str):
    try:
        print("Connecting device")
        ser = serial.Serial(
            port = device_port,
            timeout = 1,
            baudrate=9600,
            parity=serial.PARITY_EVEN,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.SEVENBITS,
        )
        ser.write('S02\x0D'.encode('utf-8'))
        ser.close()
        return {"message": "Barcode machine disabled"}
    except:
        return {"message": "something went wrong"}
