#Ejercicio de piedra papel o tijera 

import random 

rounds = 1
computer = 0
user = 0
options = ("piedra", "papel", "tijera")

while rounds:
 print('***'*10)
 print('ROUND ', rounds)
 print('***'*10)
 rounds +=1
 print('MARCADOR: ') 
 print('Computadora => ',computer)
 print('Usuario => ',user)

 user_option = input("Elige piedra, papel o tijera: ")
 user_option  = user_option.lower()

 if not user_option in options:
   print("La opcion no es valida, vuelva a intentarlo")
   continue

 computer_option = random.choice(options)
 print("Computer option: ", computer_option)

 if user_option == computer_option:
   print("Empate entre el usuario y la computadora")
 elif user_option == "piedra":
   if computer_option == "tijera":
     print("El usuario GANO, piedra vence tijera")
     user += 1
   else: 
     print("La computadora GANO, papel vence piedra")
     computer += 1
 elif user_option == "papel":
   if computer_option == "piedra":
     print("El usuario GANO, papel vence piedra")
     user += 1
   else: 
     print("La computadora GANO, tijera vence papel")
     computer += 1
 elif user_option == "tijera":
   if computer_option == "papel":
     print("El usuario GANO, tijera vence papel")
     user += 1
   else:
     print("La computadora GANO, piedra vence tijera")
     computer += 1
 if user == 2:
     print('***'*10)
     print('GAME OVER')
     print('EL USUARIO GANO EL JUEGO')
     print('***'*10)
     break
 if computer == 2:
     print('***'*10)
     print('GAME OVER')
     print('LA COMPUTADORA GANO EL JUEGO')
     print('***'*10)
     break
 print(' ')
