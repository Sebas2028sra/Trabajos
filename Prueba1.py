#Ejercicio 1


lista = []
for x in range(5):
    materias = input("Ingrese las materias del curso: ")
    lista.append(materias)

print("Yo estudio: ", lista)

print("----------------------------------------------------------------")

notas = []
for i in range(len(lista)):
    nota = int(input(f"Ingrese la nota de {lista[i]}: "))
    notas.append(nota)

print("----------------------------------------------------------------")

for i in range(len(lista)):
    print(f"En {lista[i]} has sacado {notas[i]}")

print("----------------------------------------------------------------")

for i in range(len(lista)):
    if notas[i] < 70:
        print("Debes repetir el siguiente curso:", lista[i])
    else:
        print("Felicidades, aprobaste el curso:", lista[i])

print("----------------------------------------------------------------")



#Ejercicio 2


lotto = []

for x in range(5):
    numeros = int(input("Ingrese los numeros ganadores del Lotto: "))
    lotto.append(numeros)

def orden(orden):
    orden_menor_mayor = sorted(orden)
    return orden_menor_mayor

print("----------------------------------------------------------------")

datos = orden(lotto)
print("Los numeros ganadores son: ",datos)



