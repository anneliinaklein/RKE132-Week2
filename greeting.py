""" 
Kirjuta programm, mis küsib kasutajalt tema perekonnanime ja sugu (vali „m“ või „n“).
Programm tervitab kasutajat vastavalt soole:
- Kui kasutaja valib „m“, väljasta: „Tere, härra [Perekonnanimi]!“
- Kui kasutaja valib „n“, väljasta: „Tere, proua [Perekonnanimi]!“
- Kui kasutaja sisestab midagi muud, väljasta: „Tere tulemast, [Perekonnanimi]! (sugu ei olegi tähtis).“ 
"""
#Alusta programmi
#Küsi kasutaja perekonna nime
#Küsi kasutaja sugu (m/n)
#Kui "m", siis väljasta „Tere, härra [Perekonnanimi]!“
#Kui "n", siis väljasta „Tere, proua [Perekonnanimi]!“
#Kui vastus on midagi muud, väljasta „Tere tulemast, [Perekonnanimi]! (sugu ei olegi tähtis).“
#Lõpeta programm

perekonnanimi = input("Sisesta perekonnanimi: ")
sugu = input("Sisesta sugu (m/n): ")
if sugu == "m":
    print(f"Tere, härra {perekonnanimi}!")
elif sugu == "n":
    print(f"Tere, proua {perekonnanimi}!")
else:
    print(f"Tere tulemast, {perekonnanimi}! Sugu ei olegi tähtis")
