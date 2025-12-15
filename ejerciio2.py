nota1=input("ingrese la primera nota ")
nota2=input("ingrese la segunda nota ")
nota3=input("ingrese la tercera nota ")
nota4=input("ingrese la cuarta nota ")
suma_notas= float(nota1) + float(nota2) + float(nota3) + float(nota4)
lista_notas= [float(nota1), float(nota2), float(nota3), float(nota4)]

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