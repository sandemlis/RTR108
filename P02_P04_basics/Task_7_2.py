# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")	#Ievada faila nosaukumu "mbox-short.txt"
fh = open(fname)			#atver norādīto failu
rez = float('0')			#definē mainīgo
skaits = int('0')			#definē mainīgo
for line in fh:				#iet cauri katrai rindiņai failā
    if not line.startswith("X-DSPAM-Confidence:") : continue	#ja neatrod norādīto rindas sākumu iet pie nākamās rindas
    atpos = line.find('0')		#meklē skaitļa sākumu
    host = line[atpos:]			#nolasa skaitli
    rez = rez + float(host)		#saskaita nolasītos skaitļus kopā
    skaits=skaits+1			#saskaita nolasīto skaiļu skaitu
print("Average spam confidence:",rez/skaits)	#izvada uz ekrāna vidējo vērtību
