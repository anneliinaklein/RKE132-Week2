print("Hello, world!")
""" 
kirjuta progtamm, mis küsib kasutajalt mis päev on homme (tööpäev või puhkepäev), ning väljastab vastuse põhjal sobiva sõnumi. Kasutaja sisestab ühe sõna: "tööpäev" või "puhkepäev". 
kui sisestus on "tööpäev", siis kuvatakse ekraanile tekst: 
"ma lähen magama, head ööd"! 
kui vastus on "puhkepäev": kuvatakse ekraanile tekst: 
Veel üks osa Netflixist. 
"""
#Alusta programmi.
#Küsi kasutajalt: "Mis päev on homme? (tööpäev/puhkepäev)".
#Salvesta vastus muutujasse day.
#Kui day on võrdne sõnaga "tööpäev", siis väljasta ekraanile: "Ma lähen magama, head ööd!"
#Kui day on võrdne sõnaga "puhkepäev", siis väljasta ekraanile: "Veel üks osa Netflixist"
#Muidu (kui sisestus ei olnud õige), siis väljasta ekraanile: "Vale väärtus"
#Lõpeta programm

""" day = input("Mis päev on homme? (tööpäev/puhkepäev):")

if day == "tööpäev":
    print("Ma lähen magama, head ööd!")
elif day == "puhkepäev":
    print("Veel üks osa Netflixist")
else: 
    print("Vale väärtus") """

""" print("Tere tulemast programmi 'Finantsnõustaja'!")
print("Sinu isiklik nõustaja ei tee emotsionaalseid oste.")

money = int(input("Kui palju raha sul praegu on?"))


if money < 2500:
    print("Sul pole veel piisavalt raha. Ole kannatlik ja kogu edasi.")
elif money == 2500:
    print("Palju õnne, saad osta uue iPhone 17 Pro sularahas!")
else:
    print("Saad osta iPhone 17 Pro ja veel jääb raha üle!") """


#Sammulugeja

goal = 10000
steps = int(input("Mitu sammu oled juba teinud?:"))
percent = (steps/goal) * 100
print(f"{percent}%")

if percent < 50:
    print("Alles poolel teel, liigu edasi")
elif percent < 75:
    print("Tubli, oled peaaegu kohal!")
elif percent < 100:
    print("Suurepärane, oled peaaegu kohal!")
else:
    print("Palju õnne, oled eesmärgi täitnud!")






