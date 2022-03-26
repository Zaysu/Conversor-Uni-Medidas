from func import *

print("1 - Milha")
print("2 - Polegada")
print("3 - Pés")
print("4 - Centimetros")
print("5 - Metros")
print("6 - Quilometros")
valMedida = int(input("Digite unidade Medida: "))

valor = int(input("Digite quantidade: "))

if valMedida == 1:
    convertValores = Medidas(valor, valMedida, valor, 663360, 5280, 160934, 1609, 1.609)
    convertValores.milha()  

if valMedida == 2:
    convertValores = Medidas(valor, valMedida, 63360, valor, 12, 2.54, 39.37, 39370)
    convertValores.polegada()

if valMedida == 3:
    convertValores = Medidas(valor, valMedida, 5280, 12, valor, 30.58, 3.281, 3281)
    convertValores.pe()

if valMedida == 4:
    convertValores = Medidas(valor, valMedida, 160934, 2.54, 30.48, valor, 100, 100000)
    convertValores.centimetro()

if valMedida == 5:
    convertValores = Medidas(valor, valMedida, 1609, 39.37, 3.281, 100, valor, 1000)
    convertValores.metro()
    
if valMedida == 6:
    convertValores = Medidas(valor, valMedida, 1.609, 39370, 3280, 100000, 1000, valor)
    convertValores.quilometro()