

lista=[]
for i in range(0,5):
    num=int(input("Ingrese un numero"))
    lista.append(num)
for i in lista:
    cont=0
    for x in range(1,i+1):
        if i%x==0:
            cont+=1
    if cont==2:
        print(f"{i}: es primo")
    else:
        print(f"{i}: No es primo")