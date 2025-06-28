import serial.tools.list_ports
from serial.serialutil import SerialException
import os
import time
dirname = os.path.dirname(__file__)

class logger:
    activePort = None
    logfile = os.path.join(dirname, 'Anduril2Telemetry.txt')
    baudrate = 9600

    def __init__(self):
        self.init_serial_port()

    def init_serial_port(self):
        portvar = ""

        ports = serial.tools.list_ports.comports()
        self.activePort = serial.Serial()

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
                i += 1
            elif i == len(portslist) - 1:
                print("Port not found.")
                val = input("Please enter another port:")
                i = 0
            else:
                i += 1
        self.activePort.baudrate = self.baudrate
        self.activePort = serial.Serial(portvar)
        try:
            if self.activePort.is_open:
                self.activePort.close()
                time.sleep(1)
                self.activePort.open()
            else:
                self.activePort.open()
        except SerialException as e:
            print(f"Serial port failed to open. (" + str(e) + ") Try disconnecting / reconnecting the USB cable")
            exit(1)

    def run(self):
        print(f"opening file: {self.logfile} \n for writing. \n Enter 'Save' to exit the program safely")
        with open(self.logfile, encoding="utf-8", mode='a+') as f:
            while True:
                if self.activePort.in_waiting > 0:
                    packet = self.activePort.readline()
                    f.write(packet.decode('utf'))
