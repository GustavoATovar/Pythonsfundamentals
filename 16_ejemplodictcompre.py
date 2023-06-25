#Exemple of how to use dictionary comprehension with countries and population
import random 

countries = ["Bol","Mex", "Per", "Col"]
population = {}
#Without dictionary comprehension
for country in countries:
    population[country] = random.randint(1,100)
print(population)

#With dictionary comprehension
dictionary_v2 = {country:random.randint(1,100) for country in countries}
print(dictionary_v2)

