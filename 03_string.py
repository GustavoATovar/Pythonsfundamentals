name = "Gustavo"
last_name = 'Tovar Garcia'
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "I'm Gustavo"
print(quote)

quote2 = 'He said "Hello"  '
print(quote2)

# format
#Se pueden utilizar estas 3 variantes para imprimir cadenas de caracteres
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1 ', template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)

print('v2', template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3', template)
