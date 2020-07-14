largest = 0				#Definē lielāko vērtību kā nulli
smallest = 0xff				#Definē mazāko vērtību kā 256
while True:
    num = input("Enter a number: ")	#Pieprasa texta ievadu
    if num == "done" : break		#Ja ievadā saņem vārdu "done" pārtrauc ciklu
    try:				#Pārbauda vai iespējams pārvērst ievadīto tekstu intiger mainīgajā.
        n = int(num)			#Veic mainīgā pārveidi intiger mainīgajā un piešķir mainīgajam n
    except:				#Ja nav iespēmas veikt darbības kuras definētas ar try: izpilda turpmāko darbību
        print("Invalid input")		#Izvada tekstu
    if largest < n: largest = n		#Piešķir largest jaunu vērtību ja ievadītais mainīgais ir lielāks
    if smallest > n: smallest = n	#Piešķir smallest jaunu vērtību ja ievadītais mainīgais ir mazāks

print("Maximum is", largest)		#Izvada lielāko no ievadītajām vērtībām
print("Minimum is", smallest)		#Izvada mazāko no iedadītajām vērtībām
