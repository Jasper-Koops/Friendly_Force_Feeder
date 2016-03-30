import random #Is dit nodig?

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

        #RECEPT 1 - TIME DEZE NOG
        "ultra bonen rijst": ["""

Tijd: 25 minuten

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
        ["rijst", "tomaat", "ui", "capucijners", "spekreepjes", "paprika poeder", "peper"]],


        #RECEPT 2
        "vega couscous": ["""
1. Snij de prei en doe deze in de pan
2. Snij de wortel en voeg deze vrij snel toe (om te voorkomen dat hij hard blijft)
3. Voeg het boullion blokje, de couscous en water toe en laat het staan.
4. Voeg tegen het einde de kruiden en de geroosterde paprika toe en roer goed.
5. Voeg de cashewnoten toe en server.
        """,
       ["groente boullion", "couscous", "wortel", "geroosterde paprika", "cashewnoten", "prei", "koriander poeder", "gemalen komijn"]],


        #RECEPT 3 - TIME DEZE NOG
        "ultra linzen rijst": ["""

Tijd: 25 minuten

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
        ["rijst", "tomaat", "ui", "linzen blik", "spekreepjes", "koriander poeder", "gemalen komijn"]],


        #RECEPT 4
        "libanese linzen": ["""

1. Snij de ui in blokjes en bak ze totdat ze karameliseren (of als dat niet kan, want ik ben dit recept vergeten.), ze de helft appart.
2. Voeg kruiden toe en bak 2 minuten.
3. Voeg de linzen + water toe en kook ze 10 minuten.
4. Voeg de rijst toe en kook 8 minugen.
5. Roeren, limoensap toevoegen en eventueel nog wat kruiden.
6. Serveer met wat yoghurt en de andere helft van de uien.
        """,
        ["rijst", "yoghurt", "linzen", "limoensap", "rode uien", "koriander poeder", "gemalen komijn"]],


        #RECEPT 5
        "mocro couscous": ["""

1. Verwarm olie in een pan.
2. Snijd ondertussen de ui en knoflook klein.
3. Rooster de groenten en voeg de helft van de kruiden toe. Roer goed en wacht tot de geur loskomt.
4. Voeg de couscous, linzen en een klein beetje water toe (KLEIN BEETJE, het moet geen soep worden - houd het droog) gooi de rest van de kruiden, limoensap en zout erbij en roer een paar minuten goed.
5. Serveer met yoghurt.
6. Probeer te genieten. Geen idee of ik dit chill vond toen ik dit maakte.
        """,
        ["couscous", "linzen blik", "yoghurt", "limoensap", "ui", "koriander poeder", "gemalen komijn"]],


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
        ["rijst", "ui", "paprika", "wortel", "nasi kruiden", "cashewnoten" ]],


        #RECEPT 7
        "standaard pasta": ["""

Tijd: 26 minuten

1. Breng het water aan de kook
2. Breng een pan met olie aan de kook
3. Snij de ui en knoflook en bak deze 4 minuten in de olie
4. Voeg de tomaat toe, zet het vuur zachter, dek het geheel af en laat 15 minuten doorkoken
5. Kook de pasta
6. Prik de tomaat kapot, voeg de azijn toe, roer tot je een joffele saus hebt
7. Meng de saus met de uitgegoten pasta.
8. Serveer - MET KAAS YO-  eet, ervaar, geniet.
        """,
        ["pasta", "ui", "1 blik gepelde tomaat", "kaas", "knoflook", "basalmico azijn", "italiaanse kruiden" ]],

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
9. Voeg de kruiden, gember en cashewnoten toe.
10. Serveer, eet, ervaar, geniet.
        """,
        ["rijst", "ui", "paprika", "brocolli", "cashewnoten", "woksaus", "gember", "koriander poeder"]],


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
        ["rijst", "linzen rood", "ui", "tomaat", "wortel", "kokosmelk mini", "koriander poeder", "kurkumma", "garam masala", "gemalen komijn", "limoensap", "amandelschijfjes"]],


        #RECEPT 11
        "Vega annas soep": ["""

1. Verhit de olie in een soep-pan en  bak de ui en peper een minuut of 3 totdat ze zacht zijn.
2. Voeg de kruiden (currie poeder en kurkumma) en kook 1 minuut.
3. Verkruimel het buollion blokje en voeg +/- 350 ml water en de annanas toe. Breng aan de kook en laat het 10 minuten simmeren
4. Voeg de slagroom toe en laat het nog
drie minuten koken
5. Serveer, eet, geniet en ervaar enzo.
        """,
        ["ui", "rode peper", "curry poeder", "kurkumma", "kippen boullion", "annanas", "room"]],


        #RECEPT 12
        "KIP CURRY II - I couldnt curry less": ["""

Tijd: 45 minuten.

1. Verhit de olie in een pan en water in de andere
2. Fruit de ui
3. Voeg na een paar minuten de knoflook, kruiden (BEHALVE de caynne peper) en suiker toe, blijf twee minuten roeren.
4. Voeg de kip, tomaten pasta, 70ml yoghurt en 50ml kokosmelk toe.
5. Breng de curry aan de koek en laat het zachtjes borrelen voor en minuut of 20
6. Time het zo dat je de rijst bijna gaar hebt, voeg limoensap in de curry toe samen met de cayenne peper. Kook nog een minuut of vijf.
7. Serveer, eet, ervaar, geniet.
        """,
        ["ui", "knoflook", "curry poeder", "gemalen kaneel", "paprika poeder", "gember", "suiker", "kip", "tomaten purree", "yoghurt", "kokosmelk mini", "limoen", "cayenne peper"]],


        #RECEPT 13
        "Linzen...taco's..? Ja. Linzen taco's": ["""

1. Mix de kruiden (inclusief de oregano maar niet de hotsauce) en zet ze in een bakje appart
2. Verwarm de olie in een pan en snijd de ui en knoflook
3. Fruit de olie en knoflook, met een klein beetje zout, in de pan totdat ze een klein beetje bruin worden. Klein beetje.
4. Voeg de kruiden toe en bak 30 seconden. ("Tot de geur vrijkomt")
5. Zet eht vuur wat lager en voeg de linzen, tomaten puree, hotsauce en wat water (1 vinger dikte boven de linzen uit) toe. Roer ze een beetje terwijl het kookt totdat het één massa wordt. Dit moet ongeveer 5 minuten duren.
6. Voeg eventueel zout, sauce of kruiden toe.
7. Doe de vulling in de taco's en serveer.
""",
        ["ui", "knoflook", "linzen groen", "tomaten pasta", "hot sauce", "oregano", "chillie poeder", "gemalen komijn", "koriander poeder"]],


        }
