""" 
Arstid soovitavad juua päevas 2 liitrit vett.
Kirjuta programm, mis küsib kasutajalt, kui palju klaase vett ta juba joonud on. Oletame, et üks klaas = 250 ml.
Programm arvutab, mitu protsenti päevanormist on täidetud, ja annab tagasisidet:
Kui protsent < 50: väljasta: „Joo rohkem vett, keha vajab seda!“
Kui protsent < 100: väljasta: „Tubli, jätka samas vaimus!“
Kui protsent ≥ 100: väljasta: „Suurepärane, oled oma päevase eesmärgi täitnud!“ 
"""
#Alusta programmi
#Küsi kasutajalt mitu klaasi vett on ta juba joonud
#Salvesta vastus muutujasse klaas
#Üks klaas on 250ml
#Arvuta protsent
#Kui protsent < 50: väljasta: „Joo rohkem vett, keha vajab seda!“
#Kui protsent < 100: väljasta: „Tubli, jätka samas vaimus!“
#Kui protsent ≥ 100: väljasta: „Suurepärane, oled oma päevase eesmärgi täitnud!“
#Lõpeta programm

klaasid = int(input("Mitu klaasi vett oled juba joonud?"))
Joodud_milliliitrid = klaasid * 250
percent = (Joodud_milliliitrid / 2000) * 100
print(f"{percent}%")
if percent < 50:
    print("Joo rohkem vett, keha vajab seda!")
elif percent < 100:
    print("Tubli, jätka samas vaimus!")
else:
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")
    

