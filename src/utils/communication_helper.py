
from serial import Serial
from digi.xbee.devices import XBeeDevice


class CommunicationHelper:
    def __init__(self) -> None:
        self.BAUD_RATE = 19200
        self.listener = None
        self.sender = None
        self.buffer = bytearray()
        self.telemetry = []
    def set_listener(self,port : str):
        self.listener = Serial(port=port, baudrate=self.BAUD_RATE)
    def set_sender(self,port : str):
        self.sender = XBeeDevice(port, self.BAUD_RATE)

    def listen(self):
        byte_readed = self.listener.read(1)[0]
        if byte_readed == 0x7E:
            self.buffer.clear()
            self.telemetry.clear()
        self.buffer.append(byte_readed)
        if len(self.buffer) >= 9:
            # buffer2 = self.buffer[2]
            aux = self.buffer[2] + 0x04
            if aux == len(
                self.buffer
            ):  # pregunta si ya tenemos toda la trama dentro de buffer
                message = ""
                for i in range(8, len(self.buffer) - 1):
                    message += chr(self.buffer[i])

                print(message.strip().replace("NAN", "0"))
                # Split message and send to CsvHelper class to create or append
                self.telemetry = message.split(",")
        return self.telemetry

    def send(self, DATA_TO_SEND="CMD,2030,CX,ON"):
        try:
            self.sender.open()

            print("Sending broadcast data: %s..." % DATA_TO_SEND)

            self.sender.send_data_broadcast(DATA_TO_SEND)
            self.sender.close()
            print("Success")

        finally:
            if self.sender is not None and self.sender.is_open():
                self.sender.close()
