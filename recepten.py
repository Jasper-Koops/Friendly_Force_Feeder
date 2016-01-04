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

    "capucijners": 0.00, #!!!!!!
    "cashewnoten": 0.00, # !!!!!
    "couscous": 0.00, #!!!!!
    "geroosterde paprika": 0.00, #!!!!!
    "kip": 0.00, # !!!!!!!
    "limoensap": 0.00, # !!!!!!
    "linzen": 0.00, # !!!!!!!
    "prei": 0.40,
    "rijst":0.00, # !!!!!!
    "rode ui": 0.00, #!!!!!!!
    "spekreepjes": 0.00, # !!!!!
    "tomaat": 0.00, # !!!!!
    "ui": 0.00, #!!!!!!!!!!
    "wortel": 0.18,
    "yoghurt": 0.00, # !!!!!



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



print prijs("couscous")

print prijs("rijst met kip")
