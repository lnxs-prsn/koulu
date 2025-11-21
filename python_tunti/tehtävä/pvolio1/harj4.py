class Guessword():
    def __init__(self, word):
        self.word = word
        self.guessed = list('_'*len(word))

    def is_resolved(self):
        if ''.join(self.guessed) == self.word:
            return True


    def resolve_letter(self, letter):
        
        if letter in self.word:
            for x in range(len(self.word)):
                if self.word[x] == letter:
                    self.guessed[x] = letter
        else:
            print(''.join(self.guessed))
        
        return ''.join(self.guessed)
    def hidden_word(self):
        return ''.join(self.guessed)


game = Guessword('damsdumsdims')
while not game.is_resolved():
    print(game.hidden_word())
    letter = input('Kirjain? ')
    game.resolve_letter(letter)
print(f'Voitit!')
            