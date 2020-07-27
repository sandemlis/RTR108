# HTML un CSS

Visa darbību gaita simulācijas izpildei, kas tika uzrakstīta LaTeX tika pārrakstīta uz HTML - bildes tiek saistītas caur internetu tieši uz github repozitoriju.

Piemēri CSS ielietojumiem šajā HTML failā.

Inline:
> style="background-color:#F2F2EB"

(Tiek izmantots lai nomainītu tabulā klāsu, lai vieglāk pamanītu ierakstītās koda līnijas)

Internal:
> <style>
>     body {
>         height: 842px;
>         width: 595px;
>         /* to centre page on screen*/
>         margin-left: auto;
>         margin-right: auto;
>     }
>  </style>

(Iestata lapai fiksētus izmērus, kā arī centrē to, lai tā izskatītos pēc A4 lapas)

External:
> < link rel="stylesheet" href="Voltade_devider.css">

(norāda saiti uz ārējo kaskadēšanas stila failu - noderīgs, lai katrā lapā nebūtu jāvada iekšā kāds noteikts izkārtojuma formāts)
