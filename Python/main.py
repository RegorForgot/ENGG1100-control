import atexit
import time

import serial
import serial.tools.list_ports as port_list
import websocket


class SerialReader:
    def __init__(self) -> None:
        ports = port_list.comports()
        if len(ports) > 0:
            self._ser = serial.Serial(
                port=ports[0].name,
                baudrate=115200,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
            )
        else:
            self._ser = None

    def get_serial(self) -> serial:
        return self._ser

    def serial_close(self) -> None:
        self._ser.close()
        print("Closing ports...")


def start_connection(ws):
    try:
        ws.connect("ws://192.168.4.1/")
    except TimeoutError:
        print("Please check you are on the right connection and try again.")
        raise Exception
    except OSError or ConnectionResetError:
        print("Please check your connection and try again.")
        raise ConnectionResetError


def main():
    ser = SerialReader()
    ws = websocket.WebSocket()
    try:
        start_connection(ws)
    except ConnectionResetError or TimeoutError:
        exit(1)

    if ser.get_serial() is None:
        print("No COM ports are available!")
        return

    atexit.register(ser.serial_close)
    atexit.register(ws.close)
    serial_port = ser.get_serial()
    print("Connected to {}".format(serial_port.portstr))
    while True:
        try:
            data = serial_port.readline().decode('utf-8')
            ws.send(data)
            time.sleep(0.03)
        except UnicodeDecodeError:
            print("Error! Continuing...")
        except ConnectionResetError:
            try:
                start_connection(ws)
            except ConnectionResetError:
                time.sleep(2)
        except serial.SerialException:
            print("Controller disconnected! Exiting...")
            exit(0)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exited!")
