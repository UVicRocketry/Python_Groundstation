#written by Khephren Gould for Uvic Rocketry June 25, 2025
import serial.tools.list_ports

portvar = ""
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portslist = []

for p in ports:
    portslist.append(str(p))
    print(str(p))

val = input("select Port: COM")

i = 0
while i < len(portslist):
    if portslist[i].startswith("COM" + str(val)):
        portvar = "COM" + str(val)
        print(portvar)
        i+=1
    elif i == len(portslist) - 1:
        print("Port not found.")
        val = input("Please enter another port:")
        i=0
    else:
        i+=1


serialInst.baudrate = 9600
serialInst.port = portvar

serialInst.open()

while True:
    if serialInst.in_waiting > 0:
        packet = serialInst.readline()
        print(packet.decode('utf').rstrip('\n'))

