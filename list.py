import random
from recepten import food_opties

#WORKING TITLE

#Give the number of days
#Generate a shoppinglist + recipe list
#^ or at least find a convenient way to display the information

def double_checker(keuze, lijst):
    """Checkt dat er geen dubbele recepten in de week komen."""
    while keuze in lijst:
        keuze = random.choice(food_opties.items())
    return keuze


def lijst_maker(food_opties, dagen):
    "Genereert lijst met recepten voor het aantal opgegeven dagen"
    lijst = []

    if dagen > len(food_opties):
        print("Not enough recipes for a unique dish every.single.day.\nPlease "
        "enter a lower number or add more recipes")
    elif dagen <= len(food_opties):
        for x in range(1, (dagen + 1)):
            x = random.choice(food_opties.items())
            lijst.append(double_checker(x, lijst))
        for x in lijst: #DEZE KAN LATER WEG, IS ALLEEN OM TE CHECKEN WAT ER IN DIE LIJST Staat
            print x[0]

    return lijst  #<------ WAT HIJ UITEINDELIJK GAAT DOEN.

dagen = int(raw_input("For how many days?\n> "))
lijst_maker(food_opties, dagen)
