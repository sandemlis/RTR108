# Shēmu zīmēšana un simulācija ar NGSpice palīdzību.

Šajā nodarbībā tika veikta sprieguma dalītāja shēma un veikta tās simulācija
Shēma tika uzzīmēta GSchem vidē, ar gnetlist tika iegūts elementu un mezglu saraksts, bet tālāk ar NGSpice tika veikta shēmas simulācija

## Shēmas simulācijai veicamās darbības

Lai veiktu shēmas simulāciju, tā vispirms ir jauzīmē un jāapstrādā, lai programmās varētu apstrādāt tām piešķirto informāciju.
Veicot datu sagatavošanu apstrādei ir jāzin noteiktas lietas, lai darbs notiktu veiksmīgi un nebūtu jāsaskaras ar liekām problēmām.

### Shēmas zīmēšana, jeb GSchem daļa

Sāksm ar shēmas zīmēšanu, šim darbam mēs izmantosim 'gschem' programmu, to var palaist ierakstot konsolē 'gschem'.

Vispirms veiksim shēmas zīmēšanu un tikai pēctam veiksim vērtību ievadīšanu.
Lai sāktu zīmēt shēmu, mums tajā ir jāievieto komponentes, tās ver atrast zem pogas 'Add component', kas atvērs sarakstu ar daudzām komponentēm.
Lai vieglāk būtu atrast komponenti kura mums ir nepieciešama, var izmantot meklētāju jeb filtru 'Filter:' tajā ierakstot komponentes nosaukumu angļu valodā.

Kad komponentes ir izvietotas vēlamajās vietās, tās jāsavieno ar vadiem, jeb šajā gadījumā tie ir iedomāti savienojumi, kuriem nav pretestības.
Vadus sāk zīmēt nospiežot uz pogas 'Add netsmode', kas pārslēgs rezīmu lai sāktu zīmēt vadus.
Tagad nospiežot jebkurā vietā uz shēmas (sākumpunktā) un pēctam citā (beigu punktā) tiks uzzīmēts vads starp šiem diviem punktiem.
Tāpēc, lai savienotu komponentes, kā sākumpunktu izmantosim vienas komponentes kādu no izvadiem un kā beigu punktu kādas citas komponentes kādu no izvadiem.

Kad shēma ir uzzīmēta, ir nepieciešams norādīt elementu vērtības.
Lai to varētu sākt darīt vispirms jāizslēdz vadu zīmēšanas režīms, ja to neizdarīsim, mēģinot atlasīt elementu kuram piešķirsim vērtības, mēs turpinātu zīmēt vadus, ko šobrīd mums īsti vairs nevajag. To var izdarīt ar pogu kuras ikona ir tāda pati, vai līdzīga peles kursoram (uzbraucot uz šīs pogas parādīsies 'Select mode').
Tagad kad esam izslēguši vadu zīmēšanas režīmu, varam sākt vērtību piešķiršanu elementiem.

Divreiz noklikšķinot uz elementa atvērsies logs kurā būs redzam dažādi tā raksturojošie parametri.
Atribūts 'refdes' norāda šī elementa norādīto nosaukumu, nomainot šī atribūta vērtību mēs elementam piešķirsim nausaukumu, kuru mēs pēctam spēsim atpazīt (Piemēram 'V1' - avotam, 'R3' - pretestībai utt.).
Diemžēl, mums nav vēl atribūta kurš norāda uz elementa nomināla vērtību, tādēļ to pievienosim.
Lai pievienotu nomināla vērtību, atribūtu sarakstā atradīsim atribūtu kurš norāda elementa vērtību 'Value' un kad esam atlasījuši šo atribūtu iedosim viņam skaitlisko vērtību, kad tas ir izdarīts nospidīsim 'Add' un būsim elementam piešķīruši nepieciešamās vērtības (Sarežģītākiem elementiem varētu būt arī nepieciešams piešķirt vairāk vērtību).
To pašu atkārtosim arī citiem elementiem.

#### Shēmas attēla izvadīšana

GSchem piedāvā arī izvadīt shēmas attēlu, kuru varēs apskatīties bez paša GSchem klātbūtnes.
Lai to izdarītu programmas loga augšpusē uzpiedīsim uz file, kas atvērs izvelni.
Šajā izvēlnē nospiedīsim 'print...'. Tik atvērts lodziņš kurā tik piedāvādas dažādas attēla izvadīšanas opcijas.
Mums tikai būs nepieciešams atlasīt, lai tiek izvadīts uz failu 'File:' un nospiežot print, tiks izveidots fails ar shēmas attēlu.

### Elementu-mezglu faila izveidošana

Šis fails (saraksts) ir nepieciešams, lai mēs no izveidotās shēmas varētu veikt simulācijas, tas saturēs elementu vērtības un meglus pie kuriem šie elementi ir savienoti.
Šīs darbības veikšanai izmantosim komandu 'gnetlist'
Tālāk tiks norādīts komandas pielietošanas piemērs, lai šo darbību varētu veikt:
> gnetlist -g spice -o [fails kur] [fails no kura]
"[fails kur]" norāda komandai failu, kurā tiks veikts elementu-mezglu saraksts
"[fails no kura]" norāda shēmas failu, no kura tiks veidots elementu-mezglu saraksts

### Shēmas simulācijas veikšana

Lai veiktu shēmas simulāciju ir jāpalaiž NGSpice ierakstot 'ngspice' konsolē
Kad NGSpice ir palaists būs jāieraksta dažas komandas kuras tiks izmantotas, lai iegūtu simulācijas recultātus.

Šīs komandas jāraksta ir šādā secībā, lai veiktu simulāciju
> source [fails] 
> tran [solis] [beigas] [sākums]

Komanda 'source' norāda failu, kuram tiks veikta simulācija, šis fails jānorāda "[fails]" vietā.
Šājā failā, kuru izmantos, lai veiktu simulāciju, ir jābūt mezlu-elementu sarakstam.

Komanda 'tran' veiks simulāciju laika posmā, "[solis]" norāda ik pēc cik ilga laika tiks veikta mērījumu fiksēšana, ["beigas"] norāda beigu laiku, kad beigs veikt mērījumu piefiksēšanu, un ["sākums"] norāda laiku, kurā sākt veikt mērījumu piefiksēšanu
Norādot laiku, ja netiek norādītas mērvienības, ievadītie cipari tiek uzskatīti kā sekundes, bet ja vēlas norādīt mērīšanas intervālu mazākā diapazonā, piemēram ja ir straujas izmaiņas, būs laiks jānorāda ar mērvienību, piemēram ms, us, utt.

Tālāk norādītās komandas tiek izmantotas, lai izvadītu veikto simulāciju grafikus.
> plot "[mezgls]"                   vai arī      plot "[mezgls1]" "[mezgls2]"
> hardcopy [fails kur] "[mezgls]"   vai arī      hardcopy [fails kur] "[mezgls1]" "[mezgls2]"

Komanda plot parādīs uz ekrāna grafiku, bet komanda hardcopy grafiku izvadīs failā.

