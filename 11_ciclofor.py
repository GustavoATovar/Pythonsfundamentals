# CICLO FOR 
"""
for element in  range(5,20):
 print(element)
"""
my_list = [25,43,26]
for element in my_list:
    print(element)
my_tuple = ('tavo','esme','charly')
for element in my_tuple:
    print(element)
dictionary = {
        'name': 'tavo',
        'age': 26
        } 
for element in dictionary:
    print(dictionary[element])
for atributo in dictionary:
    print(atributo,'==>',dictionary[atributo])
for key,value in dictionary.items():
    print(key,'=>',value)
people = [
        {
            'name': 'Gustavo',
            'age': 26
        },
        {
            'name': 'Esmeralda',
            'age': 26
        }
        ]
for person in people:
    print(person)
