#Valores fijos
valor_medicamentos = 60000
valor_despacho = 8000

#Datos de entrada
edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo, (A, B, C o D): ").upper()

#Variables
descuento_medicamentos = 0
descuento_despacho = 0
valor_final_medicamentos = 0
valor_final_despacho = 0

#Descuento en medicamentos
if edad <= 30:
    if tramo in ["A", "B"]:
        descuento_medicamentos = 0.18
    else:
        descuento_medicamentos = 0.12

elif edad <= 60:
    if tramo in ["A", "B"]:
        descuento_medicamentos = 0.12
    else:
        descuento_medicamentos = 0.08

else:
    descuento_medicamentos = 0

#Descuento de despacho
if tramo in ["A", "B"]:
    descuento_despacho += 0.10

if edad >= 55:
    descuento_despacho += 0.05

#Calculos
valor_final_medicamentos = valor_medicamentos - (valor_medicamentos * descuento_medicamentos)
valor_final_despacho = valor_despacho - (valor_despacho * descuento_despacho)

#Datos de salida
print("El valor de medicamentos es:", int(valor_final_medicamentos))
print("El valor del despacho es:", int(valor_final_despacho))