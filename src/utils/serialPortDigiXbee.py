from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import XBeeDevice
from digi.xbee.models.mode import APIOutputModeBit
from digi.xbee.models.protocol import XBeeProtocol

# TODO: Replace with the serial port where your local module is connected to.

# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 19200



EXPLICIT = APIOutputModeBit.calculate_api_output_mode_value(XBeeProtocol.ZIGBEE,
                                                            {APIOutputModeBit.EXPLICIT})
EXPLICIT_ZDO_PASSTHRU = APIOutputModeBit.calculate_api_output_mode_value(
    XBeeProtocol.ZIGBEE,
    {APIOutputModeBit.EXPLICIT, APIOutputModeBit.UNSUPPORTED_ZDO_PASSTHRU})

def send(PORT = "COM5", DATA_TO_SEND = "CMD,2030,CX,ON"):
    print(" +------------------------------------------------+")
    print(" | XBee Python Library Send Broadcast Data Sample |")
    print(" +------------------------------------------------+\n")

    device = XBeeDevice(PORT, BAUD_RATE)
    try:
        device.open()

        print("Sending broadcast data: %s..." % DATA_TO_SEND)

        device.send_data_broadcast(DATA_TO_SEND)
        device.close()
        print("Success")

    finally:
        if device is not None and device.is_open():
            device.close()


send()