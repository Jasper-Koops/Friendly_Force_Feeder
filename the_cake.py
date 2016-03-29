import random
import time
import smtplib
import sys
from recepten import food_opties
from ingredients import ingredienten

#nohup python the_cake.py MAX_BUDGET USER PASSWORD TARGETS


DEBUG = False  #< Yo wat doet dit? Dit zet de pauzes op hele kleine tijden zodat ik dat niet telkens vergeet te fixen.


"""
:::TODO (v1):::
- Stuur op de dag zelf nog een dag specifieke reminder, + recept #DONE TOCH? KAN WEG? <---------------
- Prijzen
- Meer recepten (tot 10) <-------- Tot infinity!
:::TOEKOMST:::
- Rekening houden met gebruikte ingredienten (zodat er niks overblijft)
- Optie geven om ook met vrijdag te werken? #Is al een opening voor, weet alleen niet of het zo werkt.
- boodschappenlijst in eigen functie # DONE. (Is dit echt handig? Opzich wellicht niet.)
- Log bestand maken zodat ik langere trends kan tracken? (gerecht, prijs, weekprijs)
:::ALTIJD:::
- Meer recepten toevoegen
"""


def double_checker(keuze, week):
    """Checkt dat er geen dubbele recepten in de week komen."""
    while keuze in week:
        keuze = random.choice(food_opties.items())
    return keuze


def dag_printer(day):
    """Fixed even dat de juiste dag weergeven wordt"""
    if day == 0:
        return "Maandag"
    elif day == 1:
        return "Dinsdag"
    elif day == 2:
        return "Woensdag"
    elif day == 3:
        return "Donderdag"
    #elif day == 4:
        #return "Vrijdag"   #IK WEET NIET OF JE DIT ZOMAAR ZO KAN INVOEGEN


def sent_mail(bericht):
    """Verstuurd de mail naar alle adressen in de commandline opgegeven targets."""
    user = sys.argv[2]
    password = sys.argv[3]
    targets = sys.argv[4:]
    smtp = "smtp.gmail.com:587"
    print("sending email") # KAN WEG ZODRA HET PROGRAMMA AF IS OM DE LOG SCHOON TE HOUDEN
    for adress in targets:
        server = smtplib.SMTP(smtp)
        server.starttls()
        server.login(user, password)
        server.sendmail(user, adress, bericht)
        server.close
        print("mail verzonden naar") # KAN WEG ZODRA HET PROGRAMMA AF IS OM DE LOG SCHOON TE HOUDEN
        print adress # KAN WEG ZODRA HET PROGRAMMA AF IS OM DE LOG SCHOON TE HOUDEN


def week_recept(week, bericht): # boodschappenlijst moet eigenlijk in eigen functie
    """DEZE VERSIE GEEFT OOK EEN PRIJS, IS DAT NIET NICE?"""
    day = 0
    for dag in week:
        bericht += "\n\n"
        bericht += dag_printer(day)
        bericht += "\nGERECHT: "
        bericht += dag[0]
        bericht += "\n"
        for x in list(dag[1][1:]):
            for y in x:
                bericht += y
                bericht += "\n"
            bericht += "kosten (schatting): "
            bericht += str(prijs(week[day][0]))
        day += 1
    bericht += "\n\n"
    bericht += "BOODSCHAPPENLIJST\n"
    # Het deel hieronder maakt de boodschappenlijst
    boodschappenlijst = []
    for dag in week:
        for x in list(dag[1][1:]):
            for y in x:
                boodschappenlijst.append(y)
    boodschappenlijst.sort()
    for ing in boodschappenlijst:
        if ing in boodschappenlijst:
            if boodschappenlijst.count(ing) == 1: # we hoeven niet 1 XX op te schrijven
                bericht += ing
            elif boodschappenlijst.count(ing) > 1:
                bericht += str(boodschappenlijst.count(ing)) + " porties " + ing
                while boodschappenlijst.count(ing) > 1: # HIJ HAALDE HEM MAAR 1 KEER WEG. Nu een while loop die doorgaat totdat ze allemaal zijn exterminated.
                    boodschappenlijst.remove(ing)

            """
            else:
                bericht += str(boodschappenlijst.count(ing)) + " " + ing
            boodschappenlijst.remove(ing)
            """
        bericht += "\n"
    bericht += "\n\n"
    bericht += "totale kosten (schatting): "
    bericht += str(totale_prijs(week)) #Werkt dit? <-- Ja.
    return bericht


def dag_recept(week, day, message):
    """ Maak een leesbaar format van de dag herinnering """
    message += dag_printer(day)
    message += "\n\n"
    message += str(week[day][0])
    message += "\n\n"
    for x in list(week[day][1][1:]):
        for y in x:
            message += y
            message += "\n"
    message += "\n"
    message += "totale kosten (schatting): "
    message += str(prijs(week[day][0]))
    message += "\n\n"
    message += "BEREIDINGSWIJZE:\n"
    for x in list(week[day][1][0]): #HIJ GEEFT NOG EEN KEER ING
        message += str(x)
    return message


def prijs(recept):
    """Rekent de prijs uit van een recept """
    prijs = 0
    for gerecht in food_opties[recept][1]:
        for key, value in ingredienten.items():
            if key == gerecht:
                prijs += value
    return prijs


def totale_prijs(week):
    """Berekent de totale kosten van de week"""
    totale_prijs = 0
    for gerecht in week:
        totale_prijs += prijs(gerecht[0])
    return totale_prijs

#Kies de recepten voor de dagen

while True:

    max_budget = sys.argv[1]
    week = [] # Is deze dubbelop?
    day = 0
    doorgaan = "nee"

    while doorgaan == "nee":

        week = []

        maandag = random.choice(food_opties.items())
        week.append(maandag)
        dinsdag = random.choice(food_opties.items())
        week.append(double_checker(dinsdag, week))
        woensdag = random.choice(food_opties.items())
        week.append(double_checker(woensdag, week))
        donderdag = random.choice(food_opties.items())
        week.append(double_checker(donderdag, week))

        #vrijdag = random.choice(food_opties.items()) GEEN IDEE OF DIT ZOMAAR WERKT
        #week.append(double_checker(vrijdag, week))

        if totale_prijs(week) <= max_budget: # Deze opzet lijkt te werken, maar durf er nog niet 100% mijn hand voor in het vuur te steken.
            doorgaan = "ja"

    bericht = ""
    header = "Subject: %s\n\n" % "Weekoverzicht" #Onderwerp verschilt per bericht, dus moet buiten de functie.
    bericht += header
    #Mail het overzicht
    sent_mail(week_recept(week, bericht))

    #Hierna elke dag een recept mail
    #time.sleep(86400) # Een dag wachten !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #time.sleep(2)  #LET EROP DAT DE TIJDEN KLOPPEN
    for x in range(0,4): #Want voor 4 dagen
        message = ""
        header = "Subject: %s\n\n" % "Dagmail" #Onderwerp verschilt per bericht, dus moet buiten de functie.
        message += header
        sent_mail(dag_recept(week,day, message))
        day += 1
        if DEBUG == True:
            time.sleep(2)
        if DEBUG == False:
            time.sleep(86400) # <------ MOET JE DIE TIME.SLEEP VOOR EEN DAG NIET HIER DOEN?

    if DEBUG == True:
        time.sleep(2)
    if DEBUG == False:
        time.sleep(604800) # 1 week wachten, MOET ONDERAAN WANT ANDERS BEGIN JE HIERMEE.
    #time.sleep(2) #LET EROP DAT DE TIJDEN KLOPPEN
