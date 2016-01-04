import random

food_opties = {
        "ultra bonen rijst": ["rijst", "tomaat", "ui", "capucijners", "spekreepjes"],
        "vega couscous": ["couscous", "wortel", "geroosterde paprika", "cashewnoten", "prei"],
        "ultra linzen rijst": ["rijst", "tomaat", "ui", "linzen", "spekreepjes"],
        "libanese linzen": ["rijst", "yoghurt", "linzen", "limoensap", "rode uien", "kruiden"],
        "mocro couscous": ["couscous", "linzen", "yoghurt", "limoensap", "ui"],
        }

test = {

        "couscous": ["couscous", "wortel", "prei"],
        "rijst met kip": ["rijst", "prei", "kip"]
        }



"""
Rijst gerechten:
Rijs: 0.28 (12.50 / 45)

Vega Couscous:

couscous: 0.23
wortel: 0.18
Prei: 0.40


"""

ingredienten = {
    #MAAAK HEM ALFABETISCH

    # ^ staat hij volgens mij

    #MEESTE PRIJZEN ZIJN NEP

    "capucijners": 1.00, #!!!!!!
    "cashewnoten": 0.40, # !!!!!
    "couscous": 0.20, #!!!!!
    "geroosterde paprika": 0.80, #!!!!!
    "kip": 4.00, # !!!!!!!
    "limoensap": 0.20, # !!!!!!
    "linzen": 0.30, # !!!!!!!
    "prei": 0.40,
    "rijst":0.20, # !!!!!!
    "rode ui": 0.24, #!!!!!!!
    "spekreepjes": 1.10, # !!!!!
    "tomaat": 0.19, # !!!!!
    "ui": 0.11, #!!!!!!!!!!
    "wortel": 0.18,
    "yoghurt": 0.80, # !!!!!



}


recepten = {

    "Mocro couscous" : ["couscous", "wortel", "prei"]
}

def prijs(recept):
    """Rekent de prijs uit van een recept """
    prijs = 0
    for gerecht in food_opties[recept]:
        for key, value in ingredienten.items():
            if key == gerecht:
                prijs += value
    return prijs

# ^zoiets?


def totale_prijs(week):
    """Berekent de totale kosten van de week"""
    totale_prijs = 0
    for gerecht in week:
        totale_prijs += prijs(gerecht[0])
    return totale_prijs


"""
week = []
for x in range(1,3):
    week.append(random.choice(food_opties.items()))

"""


#print prijs("ultra bonen rijst")
#print totale_prijs(week)
#print totale_prijs(week)

#print prijs("rijst met kip")
