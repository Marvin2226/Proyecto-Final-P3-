import re
import os
import time
os.system('cls')

print("             Punto de venta gasolinera            ")
print("**************************************************")
print("**************************************************")
print("*****                                         ****")
print("*****        PLEASE, ENTER USER ID            ****")
print("*****                                         ****")
print("**************************************************")
print("**************************************************")
print("**************************************************")
User = str(input ("User ID: "))
Password = int(input ("Password: "))
defaultpass = 123123
userid = 0
#adminpass = 456456
if Password == defaultpass: 
    print("revisando datos.....")
    ruta = 'C:\\Users\\Marvin\\Dropbox\\1-trabajos\\IV cuatrimestre\\Programacion III\\final\\Empleados.txt'
    archivo = open (ruta, 'r')
    Users = archivo.readlines()
    #print ( Users)
    for line in Users: 
        if User.lower() in line:
            #for User in archivo:
            print("User is valid")
            archivo.close()
            userid = User
    if userid == User:
        def MENU():
            print("**************************************************")
            print("**************************************************")
            print("*****                 MENU                    ****")
            print("*****   1. COMBUSTIBLE                        ****")
            print("*****   2. ACEITE                             ****")
            print("*****   3. salir                              ****")
            print("*****                                         ****")
            print("**************************************************")
            print("**************************************************")
        while True:
            MENU()
            opcion= input ("Elige una opcion: ")
            if opcion =="1":
                def MENUCOMBU():
                    print("**************************************************")
                    print("**************************************************")
                    print("*****                 MENU                    ****")
                    print("*****   1. Gas 91                             ****")
                    print("*****   2. Gas 95                             ****")
                    print("*****   3. Diesel                             ****")
                    print("*****   4. Salir                              ****")
                    print("*****                                         ****")
                    print("**************************************************")
                    print("**************************************************")
                while True:
                    MENUCOMBU()
                    combu = input("Elige una opcion: ")
                    if combu == "1":
                        gas = "Gas_91"
                        l91 = float
                        combucantidad91 = float(input("Porfavor, ingresar cantidad de dinero: "))
                        ruta = 'C:\\Users\\Marvin\\Dropbox\\1-trabajos\\IV cuatrimestre\\Programacion III\\final\\precios.txt'
                        archivop = open(ruta, 'r')
                        precios = (archivop.readlines())
                        archivop.close()
                        for precio in precios:
                            if  gas in precio:
                                l91 = float(precio.split(",")[1])
                                l91total =  l91 * combucantidad91
                                print(" El total de litros comprados: "+ str(l91total))
                                fpagos = 'C:\\Users\\Marvin\\Dropbox\\1-trabajos\\IV cuatrimestre\\Programacion III\\Final\\transacciones.txt'
                                archivo2 = open(fpagos, 'a')
                                archivo2.write("\n La compra total fue de: "+str(l91total) +time.strftime("%c"))
                                archivo2.close()
                        break
                    elif combu == "2":
                        gas = "Gas_95"
                        l95 = float
                        combucantidad95 = float(input("Porfavor, ingresar cantidad de dinero: "))
                        ruta = 'C:\\Users\\Marvin\\Dropbox\\1-trabajos\\IV cuatrimestre\\Programacion III\\final\\precios.txt'
                        archivop = open(ruta, 'r')
                        precios = (archivop.readlines())
                        archivop.close()
                        for precio in precios:
                            if  gas in precio:
                                l95 = float(precio.split(",")[1])
                                l95total =  l95 * combucantidad95
                                print("El total de litros comprados: "+ str(l95total))
                                fpagos = 'C:\\Users\\Marvin\\Dropbox\\1-trabajos\\IV cuatrimestre\\Programacion III\\Final\\transacciones.txt'
                                archivo2 = open(fpagos, 'a')
                                archivo2.write("\n La compra total fue de: "+str(l95total) +time.strftime("%c"))
                                archivo2.close()
                        break
                    elif combu == "3":
                        gas = "Diesel"
                        ld = float
                        combucantidadd = float(input("Porfavor, ingresar cantidad de dinero: "))
                        ruta = 'C:\\Users\\Marvin\\Dropbox\\1-trabajos\\IV cuatrimestre\\Programacion III\\final\\precios.txt'
                        archivop = open(ruta, 'r')
                        precios = (archivop.readlines())
                        archivop.close()
                        for precio in precios:
                            if  gas in precio:
                                ld = float(precio.split(",")[1])
                                ldtotal =  ld * combucantidadd
                                print("El total de litros comprados: "+ str(ldtotal))
                                fpagos = 'C:\\Users\\Marvin\\Dropbox\\1-trabajos\\IV cuatrimestre\\Programacion III\\Final\\transacciones.txt'
                                archivo2 = open(fpagos, 'a')
                                archivo2.write("\n La compra total fue de: "+str(ldtotal) +time.strftime("%c"))
                                archivo2.close()
                        break
                    elif combu == "4":
                        print("ALways at your service xD")
                        break
                    else:
                        print("Opcion no valida, por favor intente de nuevo")
                        break
            if opcion =="2":
                def MENUACEITE():
                    print("**************************************************")
                    print("**************************************************")
                    print("*****                 MENU                    ****")
                    print("*****   1. Castrol                            ****")
                    print("*****   2. Shell                              ****")
                    print("*****   3. Mobil                              ****")
                    print("*****   4. Salir                              ****")
                    print("*****                                         ****")
                    print("**************************************************")
                    print("**************************************************")
                while True:
                    MENUACEITE()
                    ACEITE = input("Elige una opcion: ")
                    if ACEITE == "1":
                        gas = "Castrol"
                        aceitecastrol = float
                        combucantidadac = float(input("Porfavor, ingresar cuntas botellas de 1/4: "))
                        ruta = 'C:\\Users\\Marvin\\Dropbox\\1-trabajos\\IV cuatrimestre\\Programacion III\\final\\precios.txt'
                        archivop = open(ruta, 'r')
                        precios = (archivop.readlines())
                        archivop.close()
                        for precio in precios:
                            if  gas in precio:
                                aceitecastrol = float(precio.split(",")[1])
                                aceitecastroltotal =  aceitecastrol * combucantidadac
                                print(" El precio total a pagar es de $ "+ str(aceitecastroltotal))
                                fpagos = 'C:\\Users\\Marvin\\Dropbox\\1-trabajos\\IV cuatrimestre\\Programacion III\\Final\\transacciones.txt'
                                archivo2 = open(fpagos, 'a')
                                archivo2.write("\n La compra total fue de: "+str(aceitecastroltotal) +time.strftime("%c"))
                                archivo2.close()
                        break
                    if ACEITE == "2":
                        gas = "Shell"
                        aceiteshell = float
                        combucantidadas = float(input("Porfavor, ingresar cuntas botellas de 1/4: "))
                        ruta = 'C:\\Users\\Marvin\\Dropbox\\1-trabajos\\IV cuatrimestre\\Programacion III\\final\\precios.txt'
                        archivop = open(ruta, 'r')
                        precios = (archivop.readlines())
                        archivop.close()
                        for precio in precios:
                            if  gas in precio:
                                aceiteshell = float(precio.split(",")[1])
                                aceiteshelltotal =  aceiteshell * combucantidadas
                                print(" El precio total a pagar es de $ "+ str(aceiteshelltotal))
                                fpagos = 'C:\\Users\\Marvin\\Dropbox\\1-trabajos\\IV cuatrimestre\\Programacion III\\Final\\transacciones.txt'
                                archivo2 = open(fpagos, 'a')
                                archivo2.write("\n La compra total fue de: "+str(aceiteshelltotal) +time.strftime("%c"))
                                archivo2.close()
                        break
                    if ACEITE == "3":
                        gas = "Mobil"
                        aceiteMobil = float
                        combucantidadam = float(input("Porfavor, ingresar cuntas botellas de 1/4: "))
                        ruta = 'C:\\Users\\Marvin\\Dropbox\\1-trabajos\\IV cuatrimestre\\Programacion III\\final\\precios.txt'
                        archivop = open(ruta, 'r')
                        precios = (archivop.readlines())
                        archivop.close()
                        for precio in precios:
                            if  gas in precio:
                                aceiteMobil = float(precio.split(",")[1])
                                aceiteMobiltotal =  aceiteMobil * combucantidadam
                                print(" El precio total a pagar es de $ "+ str(aceiteMobiltotal))
                                fpagos = 'C:\\Users\\Marvin\\Dropbox\\1-trabajos\\IV cuatrimestre\\Programacion III\\Final\\transacciones.txt'
                                archivo2 = open(fpagos, 'a')
                                archivo2.write("\n La compra total fue de: "+str(aceiteMobiltotal) +time.strftime("%c"))
                                archivo2.close()
                        break
                    if combu == "4":
                        print("ALways at your service xD")
                        break
                    else:
                        print("Opcion no valida, por  favor intentar denuevo")
            if opcion =="3":
                break
    else:
        print("**************************************************")
        print("*****  USER OR PASSWORD IS INCORRECT; PLEASE, TRY AGAIN   ****")
        print("**************************************************")
else:
        print("**************************************************")
        print("*****  USER OR PASSWORD IS INCORRECT; PLEASE, TRY AGAIN   ****")
        print("**************************************************")