print("bubblesort")
print("El algoritmo va a recibir los numeros ingresados y los va a ordenar en orden creciente \n "+
      "Ingrese el valor 0 para terminar de ingresar los valores y ejecutar el algoritmo")

numbers=[]
loop=True
while loop:
    new=int(input("ingrese un numero "))
    if new==0:
        break
    numbers.append(new)


swapped=True
while swapped:
    swapped=False
    for i in range(len(numbers)-1):
        if numbers[i]>numbers[i+1]:
            numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
            swapped=True


print("la lista ordenada en orden creciente es: ",numbers)

