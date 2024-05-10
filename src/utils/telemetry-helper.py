import serial as serial
#OPCION 1 Sale: b'~\x00\x15\x01\x01\x00\x10CMD,2030,CX,ON\x98'
#OPCIÓN 2 Sale: b'~\x00\x13\x01\x01\x00\x10\x00CMD,2030,CX,ON\x98'
#     bytearray(b'~\x00\x13\x01\x01\x00\x10\x00CMD,2030,CX,ON\x98')
import serial
command = "CMD,2030,CX,ON"

def telemetry_on(command):
    #OPCIÓN 2
    #bufferout = bytes([0x7E, 0x00, len(command) + 5, 0x01, 0x01, 0x00, 0x10, 0x00])
    bufferout = bytearray()
    bufferout.extend([0x7E, 0x00, len(command) + 5, 0x01, 0x01, 0x00, 0x10, 0x00])

    for char in command:
        bufferout.append(ord(char))

    chkaux = 0
    for i in range(3, len(command) + 8):
        chkaux += bufferout[i]

    chkaux = 0xFF - chkaux & 0xFF
    bufferout.append(chkaux)

    serial_port = serial.Serial()
    serial_port.port = 'COM5'  # Reemplaza 'COM1' con el puerto serial correcto
    serial_port.baudrate = 19200  # Ajusta la velocidad de baudios según sea necesario
    serial_port.timeout = 1

    if not serial_port.is_open:
        serial_port.open()
    
    print(bytes(bufferout))
    print(bufferout)
    serial_port.write(list(bufferout))



telemetry_on(command)

#OPCION 1
"""   # Iniciar Telemetria
    bufferout = bytearray()
    
    # Encabezado de trama
    bufferout.extend([0x7E, 0x00])
    
    # Longitud de la trama (incluyendo el checksum)
    length = len(command) + 7
    bufferout.append(length)
    
    # Comando específico para telemetría
    bufferout.extend([0x01, 0x01, 0x00, 0x10])
    
    # Agregar caracteres del comando
    for char in command:
        bufferout.append(ord(char))
    
    # Calcular checksum
    chkaux = sum(bufferout[3:])
    checksum = (0xFF - (chkaux & 0xFF)) & 0xFF
    bufferout.append(checksum)
    print(bufferout)
    print(bytes(bufferout))  
     # Configurar puerto serie
    serial_port = serial.Serial()
    serial_port.port = 'COM5'  # Reemplaza 'COM1' con el puerto serial correcto
    serial_port.baudrate = 19200  # Ajusta la velocidad de baudios según sea necesario
    serial_port.timeout = 1

    # Abrir puerto serie si no está abierto
    if not serial_port.is_open:
        serial_port.open()

    # Enviar trama de telemetría
    serial_port.write(bufferout) 
"""

    