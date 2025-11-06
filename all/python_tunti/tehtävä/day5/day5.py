# tee hirsipuu projekti


"""
1. pelaaja syöttää kirjaimen 
2. ohjelma kertoo kyllä ja näyttää missä osassa kirjain on sanassa 
tai ohjelma kertoo ei ja antaa arvata seuraavan
4. pelaaja voittaa jos arvaa sanan

plan
1. kirjain arvataan
scenaario 1: sana = hello
pelaaja arvaa o
kirjain on osana sanaa
printataan ---o
    mistä kone tietää että sana on oikein
        - ensin if kirjain osana listaa
    mistä kone tietää missä osassa sanaa kirjain on
    käytä find str joka kertoo mikä on index 
    vaihda indexi listassa kirjaimeen 
    mitä jos sanassa on kaksi samaa kirjainta
        - eli jos pelaaja arvaa L
            - str.find() jos löytyy index
            - sitten lisätään + 1 indexiin ja etsitään seuraava kirjain
            - jos löytyy

miten saadaan kysyttyä kysymyksiä kunnes sana on arvattu


"""

sana = input('aseta sana ').lower() 
#pelaaja_arvaus = input('arvaa kirjain')

sana1 = list(sana)
arvaus_lista = list('-'*len(sana))




n = True
while '-' in arvaus_lista:
    n = False
    arvaus = input('arvaa kirjain:')

    match arvaus:
        case aravaus if len(arvaus) == 1:
            for index, sana_letter in enumerate(sana):
                if arvaus == sana_letter:
                    arvaus_lista[index] = arvaus
                    print(arvaus_lista)
                n = True
        case arvaus if len(arvaus) > 1:
            print('one letter at a time thank you very much')





