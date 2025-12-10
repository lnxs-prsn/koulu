Tee Henkilö -luokka, joka hyväksi kaksi parametria: nimi ja ikä. Implementoi __eq__ -metodi, joka
palauttaa True jos olioiden attribuutit ovat samoja.
Käyttö esimerkki:
h1 = Henkilö('Matti', 23)
h2 = Henkilö('Matti', 23)
h3 = Henkilö('Matti', 24)
h1 == h2 # True
h1 == h3 # False