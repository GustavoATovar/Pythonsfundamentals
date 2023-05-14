#Ejercicio para calcular el promedio de presupuesto en $MX de enero a marzo
enero_budget   = input("Cual es tu presupuesto de enero? ")
febrero_budget = input("Cual es tu presupuesto de febrero? ")
marzo_budget   = input("Cual es tu presupuesto de marzo? ")

enero_budget  = int(enero_budget)
febrero_budget  = int(febrero_budget)
marzo_budget  = int(marzo_budget)

budget         = (enero_budget + febrero_budget + marzo_budget)/3
print("El presupuesto de enero a marzo es ",budget)
