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
        1. Snij de prei en doe deze in de pan
        2. Snij de wortel en voeg deze vrij snel toe (om te voorkomen dat hij hard blijft)
        3. Voeg het boullion blokje, de couscous en water toe en laat het staan.
        4. Voeg tegen het einde de kruiden en de geroosterde paprika toe en roer goed.
        5. Voeg de cashewnoten toe en server.
        """,
       ["Boullion blokje, couscous", "wortel", "geroosterde paprika", "cashewnoten", "prei", "kruiden"]],


        #RECEPT
        "ultra linzen rijst": ["""

        1. Zet een pan op het vuur en breng het water aan de kook
        2. Verwarm de olie in de pan en bak de spekjes voor een paar minuten
        3. Snij de ui in blokjes en bak ze voor 3 minuten
        4. Snij de tomaat in blokjes en doe deze bij de ui
        5. Doe de rijst in het (hopelijk kokende) water en kook het gaar
        6. Voeg de kruiden toe en wacht todat het mengsel transformeert in een ranzig slijm
        7. Voeg de linzen toe en roer alles door elkaar.
        8. Voeg de rijst erbij, roer door elkaar en bak nog even
        9. Test of het zout niveau chill is yo, en serveer.
        """,
        ["rijst", "tomaat", "ui", "linzen blik", "spekreepjes"]],


        #RECEPT
        "libanese linzen": ["""

        1. Snij de ui in blokjes en bak ze totdat ze karameliseren (of als dat niet kan, want ik ben dit recept vergeten.), ze de helft appart.
        2. Voeg kruiden toe en bak 2 minuten.
        3. Voeg de linzen + water toe en kook ze 10 minuten.
        4. Voeg de rijst toe en kook 8 minugen.
        5. Roeren, limoensap toevoegen en eventueel nog wat kruiden.
        6. Serveer met wat yoghurt en de andere helft van de uien.
        """,
        ["rijst", "yoghurt", "linzen", "limoensap", "rode uien", "kruiden"]],


        #RECEPT
        "mocro couscous": ["""

        mocro_couscous_recept
        mocro_couscous_recept
        mocro_couscous_recept
        mocro_couscous_recept
        """,
        ["couscous", "linzen blik", "yoghurt", "limoensap", "ui", "kruiden"]],


        #RECEPT
        "nice nasi": ["""

        1. Breng het water aan de kook
        2. Zet de wok op het vuur en warm de olie op
        3. Kook de rijst
        4. Snij ondetussen de ui, wortel en de paprika en voeg deze toe in de pan
        5. Voeg de kruiden toe en bak deze mee
        6. Giet de rijst af en voeg deze toe aan de pan, laat de rijst wat bakken maar schep regelmatig
        7. Voeg de cashewnoten toe.
        8. Serveer, eet, wees, geniet.
        """,
        ["rijst", "ui", "paprika", "wortel", "kruiden", "cashewnoten" ]],


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

        #RECEPT
        "ULTRA WOK": ["""

        1. Zet een grote wok op het hoogste vuur ooit, op max en VERDAMP de olie.

        1. Snijd alle groente, de broccoli, de paprika en de ui.
        2. Kook de rijst en giet deze af.




        ]


        }









        ]





ingredienten = {
    #MAAAK HEM ALFABETISCH

    # ^ staat hij volgens mij

    #MEESTE PRIJZEN ZIJN NEP
    "aardappel": 0.50, # !!!!!!!
    "basalmico azijn": 0.30, # !!!!!!!!!!!!
    "blik gepelde tomaat": 0.52,
    "broccoli": 0.70,
    "capucijners": 0.83,
    "cashewnoten": 0.51, #!!!!!!!!!!!!!!!!!
    "couscous": 0.20, #!!!!!
    "geroosterde paprika": 0.80, #!!!!!
    "kaas": 0.20, # !!!!!!!!!!
    "kip": 4.00, # !!!!!!!
    "knoflook": 0.10, # !!!!!!!!!!!!
    "kroepoek": 0.43,
    "limoensap": 0.20, # !!!!!!
    "linzen": 0.30, # !!!!!!!
    "linzen blik": 0.80, # !!!!!!
    "paprika":0.46,
    "pasta": 0.20, # !!!!!!!!!!
    "prei": 0.60,
    "rijst":0.20, # !!!!!!
    "rode ui": 0.24, #!!!!!!!
    "spekreepjes": 0.85, # !!!!!
    "tomaat": 0.50,
    "ui": 0.11, #!!!!!!!!!!
    "wortel": 0.16,
    "yoghurt": 0.80, # !!!!!

}
