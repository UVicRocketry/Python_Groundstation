import serial.tools.list_ports
from serial.serialutil import SerialException
import os
import time
import asyncio
import detectserial as detect

dirname = os.path.dirname(__file__)

class logger:
    activePort = None
    #look for / create logfile with path that is relative to script location
    logfile = os.path.join(dirname, 'Anduril2Telemetry.txt')
    baudrate = 9600 #todo ensure baudrate is correct based on what heltec transmits

    def __init__(self):
        self.init_serial_port()

    def init_serial_port(self):
        ports = detect.find_serial_ports()
        self.activePort = serial.Serial()

        portslist = []

        for p in ports:
            portslist.append(str(p))
            print(str(p))
        while True:
            portvar = input("select Port: ")
            if portslist.count(portvar) == 0:
                print("port not found. enter one of the ports from the list")
            else:
                break
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

    async def read_line_from_port(self):
        return await asyncio.to_thread(self.activePort.readline)

    async def run_logger(self):
        print(f"opening file: {self.logfile} \n for writing. \n Enter 'Save' to exit the program safely")
        with open(self.logfile, encoding="utf-8", mode='a+') as f:
            while True:
                user_input = await asyncio.to_thread(input)
                if self.activePort.in_waiting > 0:
                    packet = self.activePort.readline()
                    f.write(packet.decode('utf'))

                if user_input.lower() == "save":
                    exit(0)
