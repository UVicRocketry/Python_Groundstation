import sys
import platform
import os
import glob
import serial.tools.list_ports

def detect_os():
    """Returns the name of the operating system."""
    os_name = platform.system()
    if os_name == "Linux":
        # Try to detect WSL
        if "microsoft" in platform.release().lower():
            return "WSL"
    return os_name

def find_serial_ports():
    os_type = detect_os()
    ports = []

    if os_type == "Windows":
        # Use pyserial to list COM ports
        ports = [port.device for port in serial.tools.list_ports.comports()]

    elif os_type == "Linux" or os_type == "WSL":
        # Look for ttyS*, ttyUSB*, ttyACM*
        for pattern in ("/dev/ttyUSB*", "/dev/ttyACM*", "/dev/ttyS*"):
            ports.extend(glob.glob(pattern))

    elif os_type == "Darwin":  # macOS
        ports = glob.glob("/dev/tty.*")

    else:
        print(f"Unsupported OS: {os_type}")

    return ports
