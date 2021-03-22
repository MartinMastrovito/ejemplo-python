import random
numero_aleatorio = random.randrange(5)
gane=false
print("tenes 3 intentos para adivinar un numero entre 0 y 99")
intento=1
while intento < 4 and not gane:
  numero_ingresado=int(input('ingresa tu numero: '))
  if numero_ingresado == numero_aleatorio:
    print('ganaste! y necesitaste {} intentos'.format(intento))
    gane=true
  else:
    print('mmm ese no es el numero')
    intento +=1
if not gane:
  print('\n perdiste el numero real era: {}'.format(numero_aleatorio))
  
