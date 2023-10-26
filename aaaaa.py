import random as rd
rd.seed()

contador = 0
i = 0
while i == 0:
    palavra = rd.randint(1,1000)
    print(f'a contagem inicial é {palavra}')
    i = i + 1

while contador < 1000:
    palavra += int(input('digita ae: '))
    if palavra == 1000:
        print ("naum pode patrao")
        contador = 0
    elif palavra == 666:
        print('glória a deux')
        break
    else:
        contador += palavra
        print(f'a contagem é {contador}')
        if contador == 1000:
            print ("PARABENS CHAT GPT!!")
        elif contador > 1000:
            print('perdeu mané')
            contador = 0