"""
Auteur : fcaval@student.42lehavre.fr
Date : 05/01/26
Pour m'entraîner et comprendre Python
"""

for chiffre in [1, 2, 3, 4]:
    print(chiffre)

fruits = ["pomme", "banane", "cerise"]
for fruit in fruits:
    print(fruit)

dimensions = (10, 20, 30)
for dimension in dimensions:
    print(dimension)

for i in range(5):
    print(i)

for i in range(2, 10):
    print(i)

for i in range(0, 10, 2):
    print(i)

mon_dictionnaire = {"nom": "Alice", "âge": 25, "ville": "Paris"}
for clé in mon_dictionnaire:
    print(clé)

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for ligne in matrice:
    for élément in ligne:
        print(élément)