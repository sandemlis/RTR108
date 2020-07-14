text = "X-DSPAM-Confidence:    0.8475";	#Piešķir mainīgajam noteiktu tekstu
atpos = text.find('0')			#atrod nulles atrašanās vietu tekstā
host = text[atpos:]			#nolasa nākamās vērtības no teksta
f = float(host)				#pārvērš novērotās vērtības float mainīgajā
print(f)				#izvada float mainīgo
