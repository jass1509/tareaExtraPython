lista_notas=[]
while True:
    entrada = input("Ingrese una nota (o 'q' para terminar): ")

    if entrada == "q":
        break

    nota = float(entrada)
    lista_notas.append(nota)

suma_notas=0
for elementos in lista_notas:
    suma_notas+=elementos


minimo=lista_notas[0]
maximo=lista_notas[0]

for elementos in lista_notas:
    if elementos<minimo:
        minimo=elementos
for elementos in lista_notas:
    if elementos>maximo:
        maximo=elementos
nota_final= (suma_notas - minimo + maximo) / 4
print("la nota final es", nota_final)