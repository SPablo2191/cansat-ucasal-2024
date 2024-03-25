import serial

# Configura el puerto serie
puerto_serie = serial.Serial('COM8', 19200)  # Ajusta el nombre del puerto según tu configuración

try:
    #puerto_serie.open()
    while True:
        if puerto_serie.in_waiting > 0:
            data = puerto_serie.read()
            print(f"Received data: {data}")
        else:
            # No data, you can choose to do something else here or just pass
            pass

except KeyboardInterrupt:
    # Maneja la interrupción del teclado (Ctrl+C)
    print("Programa terminado por el usuario.")

except Exception as e:
    # Captura cualquier otro error y muestra un mensaje
    print("Se ha producido un error:", e)

finally:
    # Cierra el puerto serie al finalizar
    puerto_serie.close()
