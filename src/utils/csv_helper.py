import csv


def write_in_csv(telemetry_data: list[str]):
    nombre_archivo = r"src\data\Flight_2030.csv"
    elementos = telemetry_data.split(",")
    # Abrir el archivo CSV en modo escritura
    with open(nombre_archivo, mode="a", newline="") as file:
        # Crear un objeto escritor CSV
        escritor_csv = csv.writer(file)
        # Escribir cada elemento en una fila del archivo CSV
        escritor_csv.writerow(elementos)
