Harjoitus 4
Aikaisemmin (3. päivä perusteista) on tehty sellainen harjoitus/peli kuin 'guessword.py'.
Tehdään luokkaa, joka toimii samalla tavalla ja sopii tälle koodille:
game = Guessword('kuningas')
while not game.is_resolved():
print(game.hidden_word())
letter = input('Kirjain? ')
game.resolve_letter(letter)
print('Voitit!'