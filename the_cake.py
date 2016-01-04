import random
import time
import smtplib
import sys
from recepten import food_opties
from recepten import ingredienten

"""
:::TODO (v1):::
- Stuur elke week een kort overzicht + totale boodschappenlijst
- Stuur op de dag zelf nog een dag specifieke reminder, + recept
:::TOEKOMST:::
- Rekening houden met gebruikte ingredienten (zodat er niks overblijft)
- Kennis geven van hoe duur iets is (hoe specifiek dit wordt moet ik nog beslissen)
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

def sent_mail(bericht):
    """Verstuurd de mail naar alle adressen in de commandline opgegeven targets."""
    user = sys.argv[2]
    password = sys.argv[3]
    targets = sys.argv[4:]
    smtp = "smtp.gmail.com:587"
    print("sending email")
    for adress in targets:
        server = smtplib.SMTP(smtp)
        server.starttls()
        server.login(user, password)
        server.sendmail(user, adress, bericht)
        server.close
        print("mail verzonden naar")
        print adress

def week_recept(week, bericht):
    """DEZE VERSIE GEEFT OOK PRIJS, IS DAT NIET NICE?"""
    day = 0
    for dag in week:
        bericht += "\n\n"
        bericht += dag_printer(day)
        bericht += "\nGERECHT: "
        bericht += dag[0]
        bericht += "\n"
        for x in list(dag[1:]):
            for y in x:
                bericht += y
                bericht += "\n"
            bericht += "kosten: "
            bericht += str(prijs(week[day][0]))
        day += 1
    bericht += "\n\n"
    bericht += "totale kosten: "
    bericht += str(totale_prijs(week)) #Werkt dit?
    return bericht


def dag_recept(week, day, message):
    """ Maak een leesbaar format van de dag herinnering """
    message += dag_printer(day)
    message += "\n\n"
    message += str(week[day][0])
    message += "\n\n"
    for x in list(week[day][1:]):
        for y in x:
            message += y
            message += "\n"
    message += "\n"
    message += "totale kosten: "
    message += str(prijs(week[day][0]))
    return message


def prijs(recept):
    """Rekent de prijs uit van een recept """
    prijs = 0
    for gerecht in food_opties[recept]:
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

    #time.sleep(604800)
    time.sleep(2) #LET EROP DAT DE TIJDEN KLOPPEN

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

        if totale_prijs(week) <= max_budget:
            doorgaan = "ja"

    bericht = ""
    header = "Subject: %s\n\n" % "Weekoverzicht" #Onderwerp verschilt per bericht, dus moet buiten de functie.
    bericht += header
    #Mail het overzicht
    sent_mail(week_recept(week, bericht))

    #Hierna elke dag een recept mail
    #time.sleep(86400)
    time.sleep(2)  #LET EROP DAT DE TIJDEN KLOPPEN
    for x in range(0,4): #Want voor 4 dagen
        message = ""
        header = "Subject: %s\n\n" % "Dagmail" #Onderwerp verschilt per bericht, dus moet buiten de functie.
        message += header
        sent_mail(dag_recept(week,day, message))
        day += 1
