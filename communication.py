import serial

class SerialCommunication:
    def __init__(self, port: str, baudrate: int=115200, timeout: int=10):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = serial.Serial(self.port,
                                 baudrate=self.baudrate,
                                 timeout=self.timeout)

    def write(self, command: str) -> str:
        if '\n' not in command:
            command += '\n'
        data_send = command.encode()

        self.ser.write(data_send)
        response = self.ser.read_until("nsh> ".encode())

        return response.decode()

    def close(self) -> None:
        self.ser.close()


if __name__ == "__main__":
    device = SerialCommunication("/dev/ttyUSB0")
    ans = device.write("uname -a")
    print(ans)
    device.close()
