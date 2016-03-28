import random

"""
Dit is een dictionary met als value de recepten namen en als waarden een grot elijst met daarin een string (het recept) en een lijst van ingredienten

food_opties[0] =


"""

# GEEN CAPS GEBRUIKEN!!!

#PULAO! (of hoe dat ook heet)
#Pasta recepten
#Bami varianten?
#Die ene BBC kokos annas soep
#BOvenstaande soep met kip



food_opties = {

        #RECEPT 1
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


        #RECEPT 2
        "vega couscous": ["""
        1. Snij de prei en doe deze in de pan
        2. Snij de wortel en voeg deze vrij snel toe (om te voorkomen dat hij hard blijft)
        3. Voeg het boullion blokje, de couscous en water toe en laat het staan.
        4. Voeg tegen het einde de kruiden en de geroosterde paprika toe en roer goed.
        5. Voeg de cashewnoten toe en server.
        """,
       ["Boullion blokje", "couscous", "wortel", "geroosterde paprika", "cashewnoten", "prei", "kruiden"]],


        #RECEPT 3
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


        #RECEPT 4
        "libanese linzen": ["""

        1. Snij de ui in blokjes en bak ze totdat ze karameliseren (of als dat niet kan, want ik ben dit recept vergeten.), ze de helft appart.
        2. Voeg kruiden toe en bak 2 minuten.
        3. Voeg de linzen + water toe en kook ze 10 minuten.
        4. Voeg de rijst toe en kook 8 minugen.
        5. Roeren, limoensap toevoegen en eventueel nog wat kruiden.
        6. Serveer met wat yoghurt en de andere helft van de uien.
        """,
        ["rijst", "yoghurt", "linzen", "limoensap", "rode uien", "kruiden"]],


        #RECEPT 5
        "mocro couscous": ["""

        1. Verwarm olie in een pan.
        2. Snijd ondertussen de ui en knoflook klein.
        3. Rooster de groenten en voeg de helft van de kruiden toe. Roer goed en wacht tot de geur loskomt.
        4. Voeg de couscous, linzen en een klein beetje water toe (KLEIN BEETJE, het moet geen soep worden - houd het droog) gooi de rest van de kruiden, limoensap en zout erbij en roer een paar minuten goed.
        5. Serveer met yoghurt.
        6. Probeer te genieten. Geen idee of ik dit chill vond toen ik dit maakte.
        """,
        ["couscous", "linzen blik", "yoghurt", "limoensap", "ui", "kruiden", "knoflook"]],


        #RECEPT 6
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


        #RECEPT 7
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

        #RECEPT 8
        "ULTRA WOK": ["""

        1. Breng in een pan water (met wat zout) aan de kook voor de rijst.
        2. Zet een grote wok op het hoogste vuur ooit, op max en VERDAMP de olie. Probeer temperaturen te bereiken waarin je de one ring zou kunnen smelten.
        3. Doe, als het water in pan 1 kookt, de rijst erin en kook deze.
        4. Snijd ondertussen alle groente (de brocolli, paprika en ui)
        5. Giet de rijst af en zet hem apart.
        6. Doe de groente in de wok en bak 1 minuut, GOED roeren. Shit brand aan yo
        7. Voeg de woksaus toe (niet teveel! In zakjes de helft doen)
        8. Voeg de rijst toe, goed roeren!
        9. Voeg de kruiden en cashewnoten toe.
        10. Serveer, eet, ervaar, geniet.
        """,
        ["rijst", "ui", "paprika", "brocolli", "cashewnoten", "woksaus", "kruiden"]],


        #RECEPT 9
        "BONKERS BURGER": ["""

        1. Verwarm olie in 2 pannen.
        2. Vermeng 1 eetlepel mayo, 1 eetlepel ketchup, een theelepel mosterd en een paar druppels azijn in een bakje. Dit is de saus.
        3. Doe de aardappelschijfjes in pan 1 en bak deze.
        4. Snijd ondertussen de ui in ringen.
        5. Snijd de broodjes open
        6. Bak de burgers in pan 2 - eventueel kruiden.
        7. Doe 1 minuut voordat de burgers gaar zijn de uien in de pan en bak deze kort mee.
        8. Leg ondertussen snel de plakjes kaas op de burgers zelf.
        9. Bak de broodjes kort mee in de vleespan.
        10. Smeer de bovenstte binnenkant van de broodjes in met saus. Leg de burger op de onderste binnenkant. Leg ui en augurk op de burger. Kruid eventueel.
        11. Serveer, eet, ervaar, geniet.
        """,
        ["broodjes", "hamburgers", "kaas", "ui", "augurk", "mayonaisse", "ketchup", "mosterd", "basalmico azijn", "aardappelschijfjes"]],


        #RECEPT 10
        "FANCY DAHL": ["""

        1. Breng een pan met water en zout aan de kook voor de rijst.
        2. Zet de sauspan, ZONDER OLIE, op het vuur en rooster daarin de amandelschijfjes. PAS OP: dit gaat op een gevenmoment motherfucking snel yo.
        3. Snijd ondertussen de wortel, ui en tomaten klein.
        4. Verwarm olie in een sauspan, en voeg als deze heet genoeg is de ui, tomaat en wortel toe.
        5. Kruid bij met wat koriander.
        6. Kook ondertussen de rijst en zet deze appart als hij klaar is.
        7. Ga ondertussen die hard door met de dahl, gooi de linzen bij de groenten als deze een prut is. Roer goed en bak 1 minuut
        8. Voeg de kokosmelk toe, het moet 1 vinger dikte boven de linzen uitkomen. 200Ml should do it, zo'n blik is overkill. Voeg eventueel wat water toe.
        9. Breng het geheel aan de kook en laat het zachtjes pruttelen, vergeet niet af en toe te roeren want anders bakt het aan.
        10. Als het een soort van pap wordt dan is dat chill. Voeg wat limoensap, zout, peper en de rest van de kruiden toe
        11. Roer goed.
        12. Serveer met rijst en strooi de geroosterde amandelschijfjes erover heen.
        13. Dit is als het goed is het beste wat je ooit hebt gegeten. Als het dat niet is dan ben je persoonlijk tekort geschoten.
        """,

        ["rijst", "linzen rood", "ui", "tomaat", "wortel", "kokosmelk mini", "kruiden", "limoensap", "amandelschijfjes"]],


        }
