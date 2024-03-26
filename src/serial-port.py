import serial as serial

buffer = bytearray();
telemetry = [];

puerto_serie = serial.Serial('COM9', 19200)  
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
            if aux == len(buffer):  # pregunta si ya tenemos toda la trama dentro de buffer
                message = ""
                for i in range(8, len(buffer) - 1):
                    message += chr(buffer[i])

                print(message.strip().replace("NAN", "0"))
                # Split message and send to CsvHelper class to create or append 
                telemetry = message.split(',')
                print('telemetry:' , telemetry)
                # Cansat2021.CsvHelper.writeCsvFromList(telemetry, export)  # escribe los datos en un CSV file
             
        

except KeyboardInterrupt:
    # (Ctrl+C)
    print("Programa terminado por el usuario.")

except Exception as e:
    
    print("Se ha producido un error:", e)

finally:
    
    puerto_serie.close()
