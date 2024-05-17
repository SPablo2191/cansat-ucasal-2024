# CANSAT - UCASAL 2024 🚀
# GROUND STATION 16 BIT ADDRESS IS 0013
# PAYLOAD 16 BIT ADDRESS IS 0011 
## Project Overview

The CANSAT-UCASAL-2024 project is developed using the FLET framework, combining Python and Flutter technologies. This project utilizes the Pandas library for data manipulation, and the Digi XBee Python library for communication with XBee modules. The goal of this project is to create an interface to show the data obtained from the xbee component.

## Getting Started

### Prerequisites

Make sure you have the following prerequisites installed on your system:

![Python](https://img.shields.io/badge/Python-3.10.12-brightgreen.svg) ![Virtualenv](https://img.shields.io/badge/Virtualenv-20.25.0-brightgreen.svg)
 ![Flet](https://img.shields.io/badge/Flet-0.16.0-blue.svg) ![digi-xbee](https://img.shields.io/badge/DigiXbee-1.4.1-lightblue.svg) ![Pandas](https://img.shields.io/badge/pandas-2.1.4-gold.svg) 

### Entornos Compatibles
![Linux](https://img.shields.io/badge/Linux-compatible-green)
![Windows](https://img.shields.io/badge/Windows-compatible-green)

### Setting up the Virtual Environment

1. Open a terminal and navigate to the project directory.

2. Create a virtual environment using `venv`. Run the following commands based on your operating system:

   #### For Linux

   ```bash
   python3 -m venv venv
   ```

   #### For Windows

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   #### For Linux

   ```bash
   source venv/bin/activate
   ```

   #### For Windows

   ```bash
   .\venv\Scripts\activate
   ```

   You should see the virtual environment's name in your terminal prompt.

### Installing Dependencies

Install the required dependencies using the following command:

```bash
pip install -r requirements/dev.txt
```

This will install all the necessary packages for development.

## Running the Application

you can run the code manually using python execution style:
```bash
python src/main.py
```
or use the flet CLI (you can use hotreload):
```bash
flet run --directory src/main.py
```
or go to src directory:
```bash
cd src && flet run
```
also if you want to run the project on the web, you have to execute the following command:
```bash
flet run --directory src/main.py --w
```
## Contributing

- [Pablo Sandoval](https://github.com/SPablo2191)

## Acknowledgments

- Special thanks to the Faculty of Computer Engineering at the Universidad Católica de Salta for their support.
