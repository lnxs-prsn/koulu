# Optimized solution with input and functions

MOVES = ['kivi', 'sakset', 'paperi']
INITIALS = ['k', 's', 'p']
ANSWERS = INITIALS + MOVES

def get_move(name: str) ->int:
    """
    functio ottaa vastaan str
    ja palautaa int

    functiolle annetaan pelaajan nimi
    ja loop kysyy ja odottaa validia vastausta
    jos liike on hyväksytty 
    functio palauttaa 
    liikkeen

    """
    answer = ''
    while answer not in ANSWERS:
        answer = input(f'{name}: [K]ivi, [S]akset tai [P]aperi? ').lower()
    if answer in INITIALS:
        return INITIALS.index(answer)
    else:
        return MOVES.index(answer)

def play(player_1: int, player_2: int)->str:
    """
    functio ottaa vastaan kaksi int data tyyppiä

    functio vertaa kuka voittaa
    ja palauttaa voittajan nimen
    """
    if player_1 == player_2:
        return 'Tasapeli!'
    elif (player_1 + 1) % 3 == player_2:
        return 'Player 1 wins'
    else:
        return 'Player 2 wins'


player_1 = get_move('Player 1')
player_2 = get_move('Player 2')

print(play(player_1, player_2))

#   K S P
# I 0 1 2
#   A B
#     A B
#   B   A
