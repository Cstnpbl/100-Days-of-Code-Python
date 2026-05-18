
i=0
pista1="Es una fruta"
pista2="Es de color rojo"
pista3="Empieza por M"
pistas=[pista1,pista2,pista3]
palabra="manzana"

pista2="Empieza con M"
print("Bienvenido a WordGuesser! Estoy pensando en una palabra y tu la tienes que adivinar! \n A ver si aciertas la palabra que tengo en mente")
for i in range(0,4):
    word = input(str.lower("Intenta adivinar la palabra: "))
    if word.lower()==palabra:
        print("Adivinaste!")
        break
    else:
        if word != palabra and i<4:
            print("EQUIVOCADO, TE DEJO UNA PISTA: " + pistas[i])
            i+=1
            if i==3:
                print("Ultimo intento! Tienes que adivinar la palabra YAAAA")
        else:
            print("Te has quedado sin intentos! La palabra era manzana!")