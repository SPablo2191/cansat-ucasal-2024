import csv

def escribir_en_csv(string_comas):
    nombre_archivo = 'C:\cansat 2023\Flight_2030.csv'
    elementos = string_comas.split(',')
    # Abrir el archivo CSV en modo escritura
    with open(nombre_archivo, mode='a', newline='') as file:
        # Crear un objeto escritor CSV
        escritor_csv = csv.writer(file)

        # Escribir cada elemento en una fila del archivo CSV
        escritor_csv.writerow(elementos)
        file.close()