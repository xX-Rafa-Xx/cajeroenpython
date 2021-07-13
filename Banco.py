# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 13:35:20 2021

@author: Rafa
"""

'''
Realizar un programa que simule un cajero automático 
con cinco billetes para cada denominación. El 
usuario debe poder hacer retiros haciendo uso de
los billetes en existencia con cantidades exactas
'''
veinte = 5              # $100
cincuenta = 5           # $250
cien = 5                # $500
doscientos = 5          # $1,000
quinientos = 5          # $2,500
mil = 5                 # $5,000
total = 9350           #Total = $9,350

print("Bienvenido a nuestro sistema")
user = input("por introdusca su Usario ")
passw = input("Ahora su Password ")
if(user == passw):
    print("Bienvenido sr",user)

while(total != 0):
    cantidad = int(input("Por favor introdusca la cantidad que desea retirar "))
    sale = cantidad
    if (cantidad <= 9350 and cantidad > 19 and sale <= total): #evalua la cantidad a retirar
        print("¿Seguro que quiere retirar ",cantidad," pesos?")
        respuesta = input(" ")
        if(respuesta == "si" or "s"):
            if(cantidad >= 1000 and mil != 0):
                billete = cantidad // 1000
                if(billete <= 5 and billete <= mil):
                    mil = mil - billete
                    cantidad = cantidad % 1000
                    total = total - (billete* 1000)
                    print(billete, "de Mil pesos")
                else:
                    data = billete - mil
                    dado = data * 1000
                    cantidad = (cantidad % 1000)+dado
                    print(mil, "billetes de Mil pesos")
                    total = total - (mil*1000)
                    mil = 0
                
            if(cantidad >= 500 and quinientos != 0):
                billete = cantidad //500   
                if (billete <= 5):
                    quinientos = quinientos - billete
                    cantidad = cantidad % 500
                    total = total - (billete * 500)
                    print(billete," billetes de Quinientos pesos")
                else:
                    data = billete - quinientos
                    dado = data * 500
                    cantidad = (cantidad % 500)+dado
                    print(quinientos, "billetes de Quinientos pesos")
                    total = total - (quinientos * 500)
                    quinientos = 0 
            if(cantidad >= 200 and doscientos != 0):
                billete = cantidad // 200
                if(billete <= 5):
                    doscientos = doscientos - billete
                    cantidad = cantidad % 200
                    total = total - (billete * 200)
                    print(billete," billetes de Doscientos pesos")
                else:
                    data = billete - doscientos
                    dado = data * 200
                    cantidad = (cantidad % 200)+dado
                    print(doscientos, "billetes de Doscientos pesos")
                    total = total - (doscientos * 200)
                    doscientos = 0
            if(cantidad >= 100 and cien != 0):
                billete = cantidad // 100
                if(billete <= 5):
                    cien = cien - billete
                    cantidad = cantidad % 100
                    total = total - (billete * 100)
                    print(billete," billetes de Cien pesos")
                else:
                    data = billete - cien
                    dado = data * 100
                    cantidad = (cantidad % 100)+dado
                    print(cien, "billetes de Cien pesos")
                    total = total - (cien * 100)
                    cien = 0
            if (cantidad >= 50 and cincuenta != 0): #arreglar bug
                billete = cantidad // 50
                if(billete <= 5):
                    cincuenta = cincuenta - billete
                    cantidad = cantidad % 50
                    total = total - (billete * 50)
                    print(billete," billetes de Cincuenta pesos")
                else:
                    data = billete - cincuenta
                    dado = data * 50
                    cantidad = (cantidad % 50)+dado
                    print(cincuenta, "billetes de Cincuenta pesos")
                    total = total - (cincuenta * 50)
                    cincuenta = 0
            if (cantidad >= 20 and veinte != 0):
                billete = cantidad // 20
                if(billete <= 5):
                    veinte = veinte - billete
                    cantidad = cantidad % 20
                    total = total - (billete * 20)
                    print(billete, "billetes de Veinte pesos")     
                
            #total = total - sale
        else:
            break

    else:
        print("Usted no cuenta con ese efectivo en su cuenta para retirar esa cantidad")


print("Usted ha agotado su saldo")