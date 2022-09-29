import math
from datetime import date
from math import *
import time
acelerar=0
menu = int(input("¡BIENVENIDO!\n"
                 "Presione 1 para registrarse\n"
                 "Presione 2 para comenzar una carrera\n"
                 "* "))
if menu == 1:
    print(input("Ingrese nombre completo: "))
    print(input("Ingrese  rut: "))
    print(input("Ingrese correo electrónico: "))
    print(input("Ingrese número de teléfono: "))
    print(input("Ingrese patente del vehículo: "))
    time.sleep(2)
    print("Su registro ha sido exitoso\n"
          "Ya esta listo para realizar una carrera")
    time.sleep(1)
    menu = int(input("Presione 2 para comenzar una carrera\n"
                     "Presione 3 para salir\n"
                     "* "))
if menu == 2:
    lat1 = float(input("Ingrese ubicación GPS, LATITUD: "))
    lon1 = float(input("Ingrese ubicación GPS, LONGITUD: "))
    time.sleep(1)
    print("Encienda el vehículo")
    time.sleep(1)
    while True:
        print("Presione a cada vez que acelere\n"
              "Presione g cada vez que gire\n"
              "Presione d cuando haya llegado a su destino")
        opcion = input()
        if opcion == 'a':
            acelerar = acelerar + 10
            print("Usted esta viajando a: ",(acelerar), "km/h")
        if opcion == 'g':
            print("Usted giró")
        if opcion == 'd':
            break
    print("Apagar Vehículo")
    print("Usted ha llegado a su destino")
    time.sleep(1)
    lat2 = float(input("Ingrese ubicación GPS actual, LATITUD: "))
    lon2 = float(input("Ingrese ubicación GPS actual, LONGITUD: "))
    rad = float
    rad = math.pi / 180
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    R = 6371
    a = math.sin(rad * dlat / 2) ** 2 + math.cos(rad * lat1) * math.cos(rad * lat2) * math.sin(rad * dlon / 2) ** 2
    distancia = 2 * R * math.asin(math.sqrt(a))
    time.sleep(2)
    print("Carrera finalizada a: ", distancia, " km")
    precio = distancia * 650
    today = date.today()
    print("Con fecha",today)
    time.sleep(1)
    print("Con un total a pagar de: $", int(precio))
    time.sleep(3)
    print("¡Hasta pronto!")
if menu == 3:
    print("¡Hasta pronto!")