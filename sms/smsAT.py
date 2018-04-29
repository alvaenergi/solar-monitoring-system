import serial
import time

recipient = "+6582760190" 
message = '{"id":"geranting","V":"1","I":"0"}'

modem = serial.Serial("/dev/ttyACM0", 115200, timeout=5)

modem.write('AT\r\n')
time.sleep(0.5)
modem.readline()
data = modem.readline().strip('\r\n')

# check if data is ok
modem.write('AT+CMGF=1\r\n')
time.sleep(0.5)
modem.readline()
data = modem.readline().strip('\r\n')

if(data=='OK'):
    modem.write('AT+CMGW=' + '\"' + recipient + '\"\r\n')
    modem.readline()
    modem.write(message + '\x1A\r\n')
    time.sleep(0.5)
    modem.readline()    
    data = modem.readline().strip('\r\n')
    
    #code

    code = data.split(" ")[1]

    modem.write('AT+CMSS=' + code + '\r\n')


