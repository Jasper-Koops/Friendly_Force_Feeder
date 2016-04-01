import random
import datetime
from recepten import food_opties
from ingredients import ingredienten

#WORKING TITLE

#Give the number of days
#recipe list
#^ or at least find a convenient way to display the information

def prijs(recept):
    """Rekent de prijs uit van een recept """
    prijs = 0
    for gerecht in food_opties[recept][1]:
        for key, value in ingredienten.items():
            if key == gerecht:
                prijs += value
    return prijs


def totale_prijs(lijst):
    """Berekent de totale kosten van de week"""
    totale_prijs = 0
    for gerecht in lijst:
        totale_prijs += prijs(gerecht[0])
    return totale_prijs


def double_checker(keuze, lijst):
    """Checkt dat er geen dubbele recepten in de week komen."""
    while keuze in lijst:
        keuze = random.choice(food_opties.items())
    return keuze


def gerechten_kiezer(food_opties, dagen):
    """Genereert lijst met recepten voor het aantal opgegeven dagen"""
    lijst = []

    if dagen > len(food_opties):
        print("Not enough recipes for a unique dish every.single.day.\nPlease "
        "enter a lower number or add more recipes")
    elif dagen <= len(food_opties):
        for x in range(1, (dagen + 1)):
            x = random.choice(food_opties.items())
            lijst.append(double_checker(x, lijst))
        #for x in lijst: #DEZE KAN LATER WEG, IS ALLEEN OM TE CHECKEN WAT ER IN DIE LIJST Staat
            #print x[0]

    return lijst  #<------ WAT HIJ UITEINDELIJK GAAT DOEN.


def boodschappenlijst_generator(lijst):
    """Maakt een booschappenlijst basic, zonder formatting"""
    boodschappenlijst = []
    for dag in lijst:
        for x in list(dag[1][1:]):
            for y in x:
                boodschappenlijst.append(y)
    boodschappenlijst.sort()

    return boodschappenlijst



def formatter(lijst):
    """Maakt een weergave van alle info"""
    boodschappenlijst = boodschappenlijst_generator(lijst)
    bericht = "Boodschappenlijst: \n\n"
    #Code hieronder zorgt ervoor dat er correcte nummers staan (dus '2 porties
    #rijst' en niet 'rijst rijst')
    for ing in boodschappenlijst:
        if ing in boodschappenlijst:
            if boodschappenlijst.count(ing) == 1: # we hoeven niet 1 XX op te schrijven
                bericht += ing
                bericht += " \n"
            elif boodschappenlijst.count(ing) > 1:
                bericht += str(boodschappenlijst.count(ing)) + " porties " + ing
                bericht += " \n"
                while boodschappenlijst.count(ing) > 1: # HIJ HAALDE HEM MAAR 1 KEER WEG. Nu een while loop die doorgaat totdat ze allemaal zijn exterminated.
                    boodschappenlijst.remove(ing)
    bericht += "\nTOTALE PRIJS: "
    bericht += str(totale_prijs(lijst))
    bericht += "\n\n\n"
    bericht += "BEREIDINGSWIJZE:\n"
    dag = 1
    for x in lijst:

        bericht += "\n"
        bericht += "dag " + str(dag) + ": " + str(x[0]).upper()
        bericht += "\nPrijs: " + str(prijs(x[0]))

        for y in x[1]:
            bericht += str(y)
        bericht += "\n\n"
        dag += 1

    #return boodschappenlijst
    return bericht
    #HIERONDER VOOR DEBUG ONLY


dagen = int(raw_input("Yo G,voor hoeveel dagen wil je recepten?\n> "))

print(formatter(gerechten_kiezer(food_opties, dagen)))
