import random


# # hirsipuu
#  Lisää hirsipuu-pelille 'used_letters'-muuttuja, 
# jossa kerätään pelaajan syötetty validia kirjaimia. 
# Jos pelaaja yrittää käyttää yksi niistä uudelleen, ilmoita hänelle asiasta.



# hidden_word = 'hirsipuu'
# resolved_word = ['_'] * len(hidden_word)
# VALID_LETTERS = 'abcdefghijklmnopqrstuvwxyzäö'
# used_letters  = []


# def ask_user(question: str) -> str:
#     while True:
#         answer = input(question).lower()
#         match answer:
#             case '':
#                 continue
#             case '0':
#                 return '0'
#             case answer if answer in used_letters:
#                 print('tämä kirjain on jo kokeiltu')
#             case _:
#                 for letter in answer:
#                     if letter not in VALID_LETTERS:
#                         break
#                 else:
#                     return answer
            

# while True:
#     print(f"Arvattava sana on {''.join(resolved_word)}")
#     user_answer = ask_user('Syötä kirjain tai sana (A-Za-zÄäÖö). 0 -> lopettaa peli\n? ')
#     used_letters.append(user_answer)
#     match user_answer:
#         case '0':
#             print('Kiitos pelaamisesta')
#             break
#         case _ if len(user_answer) == 1:
#             for index, word_letter in enumerate(hidden_word):
#                 if user_answer == word_letter:
#                     resolved_word[index] = user_answer
#         case _ if user_answer == hidden_word:
#            resolved_word = list(hidden_word)
    
#     if resolved_word.count('_') == 0:
#            print(f'Voitit. Sana oli {hidden_word}')
#            break




 


# Muokkaa Kivi, Sakset, Paperi -peli niin, 
# että toinen pelaajaa on tietokone. 
# Tietokone pelaa vain randomisti.



# Optimized solution with input and functions

MOVES = ['kivi', 'sakset', 'paperi']
INITIALS = ['k', 's', 'p']
ANSWERS = INITIALS + MOVES

def get_move(name: str) -> int:
    """
    Get the player move and returns it in integer form

    This function will ask the user to choose between 'Kivi', 'Sakset' and 'Paperi'.
    The whole word or initials are accepted (case insensitive).
    It will keep asking the user until it gets a valid answer. It can not be cancelled.

    Parameters:
    - name (str): Name of the player that will be presented in the question

    Returns:
    An integer that represents the index in the options.
    """

    answer = ''
    while answer not in ANSWERS:
        answer = input(f'{name}: [K]ivi, [S]akset tai [P]aperi? ').lower()
    if answer in INITIALS:
        return INITIALS.index(answer)
    else:
        return MOVES.index(answer)

def play(player_1: int, player_2: int) -> str:
    """
    Calculate the winner according to the rules of the game and return a string declaring the winner.

    Parameters:
    - player_1 (int): The first player move. It's an index of the list of possible moves.
    - player_2 (int): The second player move. It's an index of the list of possible moves.

    Returns:
    A string containing a message declaring the winner or that the game was a draw.
    """
    if player_1 == player_2:
        return f'Tasapeli!'
    elif (player_1 + 1) % 3 == player_2:
        return f'Pelaaja 1 voittaa'
    else:
        return f'Pelaaja 2 voittaa'


player_1 = get_move('Pelaaja 1')
player_2 = random.choice([0,1,2])
# get_move('Pelaaja 2')

print(play(player_1, player_2))

#   K S P
# I 0 1 2
#   A B
#     A B
#   B   A
 