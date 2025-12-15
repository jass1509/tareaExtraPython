nota1=input("ingrese la primera nota ")
nota2=input("ingrese la segunda nota ")
nota3=input("ingrese la tercera nota ")
nota4=input("ingrese la cuarta nota ")
suma_notas= float(nota1) + float(nota2) + float(nota3) + float(nota4)
lista_notas= [float(nota1), float(nota2), float(nota3), float(nota4)]

for elementos in lista_notas:
    minimo=lista_notas[0]
    if elementos<minimo:
        minimo=elementos
for elementos in lista_notas:
    maximo=lista_notas[0]
    if elementos>maximo:
        maximo=elementos
nota_final= (suma_notas - minimo + maximo) / 4
print("la nota final es"+ nota_final)