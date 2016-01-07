import random

# GEEN CAPS GEBRUIKEN!!!




"""
Rijst gerechten:
Rijs: 0.28 (12.50 / 45)

Vega Couscous:

couscous: 0.23
wortel: 0.18
Prei: 0.40


"""

food_opties = {

        #RECEPT
        "ultra bonen rijst": ["""
            1. Zet een pan op het vuur en breng het water aan de kook
            2. Verwarm de olie in de pan en bak de spekjes voor een paar minuten
            3. Snij de ui in blokjes en bak ze voor 3 minuten
            4. Snij de tomaat in blokjes en doe deze bij de ui
            5. Doe de rijst in het (hopelijk kokende) water en kook het gaar
            6. Voeg de kruiden toe en wacht todat het mengsel transformeert in een ranzig slijm
            7. Voeg de capucijners toe en roer alles door elkaar.
            8. Voeg de rijst erbij, roer door elkaar en bak nog even
            9. Test of het zout niveau chill is yo, en serveer.
            """,
            ["rijst", "tomaat", "ui", "capucijners", "spekreepjes"]],


        #RECEPT
        "vega couscous": ["""
            vega_couscous_recept,
            vega_couscous_recept,
            vega_couscous_recept,
            vega_couscous_recept,
        """,
           ["couscous", "wortel", "geroosterde paprika", "cashewnoten", "prei"]],


        #RECEPT
        "ultra linzen rijst": ["""

        ultra_linzen_rijst_recept
        ultra_linzen_rijst_recept
        ultra_linzen_rijst_recept
        ultra_linzen_rijst_recept
        """,
        ["rijst", "tomaat", "ui", "linzen", "spekreepjes"]],


        #RECEPT
        "libanese linzen": ["""

        libanese_linzen_recept
        libanese_linzen_recept
        libanese_linzen_recept
        libanese_linzen_recept
        """,
        ["rijst", "yoghurt", "linzen", "limoensap", "rode uien", "kruiden"]],


        #RECEPT
        "mocro couscous": ["""

        mocro_couscous_recept
        mocro_couscous_recept
        mocro_couscous_recept
        mocro_couscous_recept
        """,
        ["couscous", "linzen", "yoghurt", "limoensap", "ui"]],


        #RECEPT
        "standaard pasta": ["""

        1. Breng het water aan de kook
        2. Breng een pan met olie aan de kook
        3. Snij de ui en knoflook en bak deze 4 minuten in de olie
        4. Voeg de tomaat toe, zet het vuur zachter, dek het geheel af en laat 15 minuten doorkoken
        5. Kook de pasta
        6. Prik de tomaat kapot, voeg de azijn toe, roer tot je een joffele saus hebt
        7. Serveer, eet, ervaar, geniet.
        """,
        ["pasta", "ui", "1 blik gepelde tomaat", "kaas", "knoflook", "basalmico azijn" ]],


        }



ingredienten = {
    #MAAAK HEM ALFABETISCH

    # ^ staat hij volgens mij

    #MEESTE PRIJZEN ZIJN NEP
    "aardappel": 0.50, # !!!!!!!
    "basalmico azijn": 0.30, # !!!!!!!!!!!!
    "blik gepelde tomaat": 0.60, # !!!!!!!!
    "capucijners": 1.00, #!!!!!!
    "cashewnoten": 0.40, # !!!!!
    "couscous": 0.20, #!!!!!
    "geroosterde paprika": 0.80, #!!!!!
    "kaas": 0.20, # !!!!!!!!!!
    "knoflook": 0.10, # !!!!!!!!!!!!
    "kip": 4.00, # !!!!!!!
    "limoensap": 0.20, # !!!!!!
    "linzen": 0.30, # !!!!!!!
    "linzen blik": 0.80, # !!!!!!
    "pasta": 0.20, # !!!!!!!!!!
    "prei": 0.40,
    "rijst":0.20, # !!!!!!
    "rode ui": 0.24, #!!!!!!!
    "spekreepjes": 1.10, # !!!!!
    "tomaat": 0.19, # !!!!!
    "ui": 0.11, #!!!!!!!!!!
    "wortel": 0.18,
    "yoghurt": 0.80, # !!!!!

}
