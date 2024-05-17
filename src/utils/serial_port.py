import serial as serial
from serial.tools import list_ports


from utils.csv_helper import write_in_csv

# GROUND STATION 16 BIT ADDRESS IS 0013
# PAYLOAD 16 BIT ADDRESS IS 0011
buffer = bytearray()
telemetry = []


def get_available_serial_ports():
    serial_ports = list_ports.comports()
    port_names = [serial_port.device for serial_port in serial_ports]
    return port_names


def serial_port_listen(serialPort="COM5", baudRate=19200):
    puerto_serie = serial.Serial(serialPort, baudRate)
    try:
        while True:
            byteReaded = puerto_serie.read(1)[0]
            if byteReaded == 0x7E:
                buffer.clear()
                telemetry.clear()
            buffer.append(byteReaded)

            if len(buffer) >= 9:
                buffer2 = buffer[2]
                aux = buffer[2] + 0x04
                if aux == len(
                    buffer
                ):  # pregunta si ya tenemos toda la trama dentro de buffer
                    message = ""
                    for i in range(8, len(buffer) - 1):
                        message += chr(buffer[i])

                    print(message.strip().replace("NAN", "0"))
                    # Split message and send to CsvHelper class to create or append
                    telemetry = message.split(",")
                    write_in_csv(message)
                    # Cansat2021.CsvHelper.writeCsvFromList(telemetry, export)  # escribe los datos en un CSV file
    except KeyboardInterrupt:
        # (Ctrl+C)
        print("Programa terminado por el usuario.")

    except Exception as e:

        print("Se ha producido un error:", e)
