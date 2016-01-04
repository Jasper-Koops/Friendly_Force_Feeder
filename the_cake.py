import random
import time
import smtplib
import sys
from recepten import food_opties

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
    """Verstuurd de mail naar alle in de commandline opgegeven targets."""
    user = sys.argv[1]
    password = sys.argv[2]
    targets = sys.argv[3:]
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
    """Maakt een leesbaar format van het week overzicht"""
    day = 0
    for dag in week:
        bericht += "\n"
        bericht += dag_printer(day)
        bericht += "\nGERECHT: "
        bericht += dag[0]
        bericht += "\n"
        for x in list(dag[1:]):
            for y in x:
                bericht += y
                bericht += "\n"
        day += 1
    return bericht

def dag_recept(week, day, message):
    """Maak een leesbaar format van de dag herinnering"""
    message += dag_printer(day)
    message += "\n"
    vandaag = week[day]
    message += str(week[day])
    return message


#Kies de recepten voor de dagen

while True:

<<<<<<< HEAD
    time.sleep(604800) 
    #time.sleep(2) VINK DEZE UIT ALS JE HEM ECHT GAAT DRAAIEN
=======
    time.sleep(604800)
    #time.sleep(2) LET EROP DAT DE TIJDEN KLOPPEN
>>>>>>> 615ca34a7616262a736280b6a0609f1fc2a09cdc

    week = []
    day = 0

    maandag = random.choice(food_opties.items())
    week.append(maandag)
    dinsdag = random.choice(food_opties.items())
    week.append(double_checker(dinsdag, week))
    woensdag = random.choice(food_opties.items())
    week.append(double_checker(woensdag, week))
    donderdag = random.choice(food_opties.items())

    week.append(double_checker(donderdag, week))

    bericht = ""
    header = "Subject: %s\n\n" % "Weekoverzicht" #Onderwerp verschilt per bericht, dus moet buiten de functie.
    bericht += header
    #Mail het overzicht
    sent_mail(week_recept(week, bericht))

    #Hierna elke dag een recept mail
<<<<<<< HEAD
    time.sleep(86400) //Omdat het sneller moet gaan bij het testen
    #time.sleep(2) VINK DEZE UIT ALS JE HEM ECHT GAAT DRAAIEN
=======
    time.sleep(86400)
    #time.sleep(2)  LET EROP DAT DE TIJDEN KLOPPEN
>>>>>>> 615ca34a7616262a736280b6a0609f1fc2a09cdc
    for x in range(0,4): #Want voor 4 dagen
        message = ""
        header = "Subject: %s\n\n" % "Dagmail" #Onderwerp verschilt per bericht, dus moet buiten de functie.
        message += header
        sent_mail(dag_recept(week,day, message))
        day += 1
