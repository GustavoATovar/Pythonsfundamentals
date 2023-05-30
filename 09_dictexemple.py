#Exemple of a dictionary

person = {
        'name': 'Gustavo',
        'lastname': 'Tovar',
        'age': 26
        }

person['twiter']= "@nicobytes"
print(person)
person['name']= "Carlos"
print(person)
del person['age']
print(person)
print('Keys')
print(person.keys())
print('Values')
print(person.values())

"""
print(person)
person['name'] = 'Santi'
print(person)
person['langs'].append('rust')
print(person)
del person['lastname']
print(person)
person.pop('age')
print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())
"""
