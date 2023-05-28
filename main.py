#Ejercicio de piedra papel o tijera 

import random 

options = ("piedra", "papel", "tijera")

user_option = input("Elige piedra, papel o tijera: ")
user_option  = user_option.lower()

if not user_option in options:
  print("La opcion no es valida, vuelva a intentarlo")

computer_option = random.choice(options)
print("Computer option: ", computer_option)

if user_option == computer_option:
  print("Empate entre el usuario y la computadora")
elif user_option == "piedra":
  if computer_option == "tijera":
    print("El usuario GANO, piedra vence tijera")
  else: 
    print("La computadora GANO, papel vence piedra")
elif user_option == "papel":
  if computer_option == "piedra":
    print("El usuario GANO, papel vence piedra")
  else: 
    print("La computadora GANO, tijera vence papel")
elif user_option == "tijera":
  if computer_option == "papel":
    print("El usuario GANO, tijera vence papel")
  else:
    print("La computadora GANO, piedra vence tijera")
