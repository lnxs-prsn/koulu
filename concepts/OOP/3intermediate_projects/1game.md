

### **Exercise 1: Simple Game Objects**
# Game → Player? (Game manages players)
# Player → Game? (Player knows which game they're in)
# Player → Card? (Player holds cards)
# Card → Player? (Card knows who holds it?)

# Python implementation level questions:
# 1. Should Game create Player objects, or are they created separately?
    -   game should create player objects
    -   because the players existing outside the game makes very little sense
# 2. When Player plays a Card, who updates the game state?
    -   player sends request for update and the game checks the rules and approves or not according to rules
# 3. If Player quits, what happens to their Cards?
    -   depends if the game has feature to store game states 


ACTION
    -   game manages players
    -   player operates in the game
    -   card operates within the game with player


PARTICIPANTS
    -   game
    -   player
    -   card

RESPONSABILITY
    -   game
        -   place where the player and card participate
        -   space where everything happens 
    -   player
        -   participant in the game
        -   operate according to games rules
        -   interacts with other participants 
    -   card
        -   participant in the game
        -   operate accordign to games rules
        -   interacts with other participants 


AUTHORITY
    -   game 
        -   game has most of the authority
        -   I dont know games where the player can go to other games 
        -   so game is the biggest authority 
    -   player 
        -   participant in the game
    -   card 
        -   participant in the game



ARROWS
    -   game > player and game > card


TASK CONSTRAINTS 
    -   as the game rules are unknown 
    -   its not easy to say clearly
    -   but everything must happen in the game and by the game
    -   all the participants are dependent on the game 