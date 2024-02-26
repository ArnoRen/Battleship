from components import initialize_board, create_battleships, place_battleships
from game_engine import attack, cli_coordinates_input
import random


# Store the username of each player as the key and their board and battleships as the value.
players = {"Player" : [],
           "AI" : []}

def generate_attack():
    '''Create random tuple ex.(3,1) for AI to attack.'''
    row = random.randint(0, 9)
    col = random.randint(0, 9)
    return (row,col) #AI opponents attack coordinates

def ai_opponent_game_loop(players = players):
    ''' 2 Player (Against Computer) Game Mode
    User's battleship placement is custom
    AI's battleship placement is random
    If you hit you get one more turn (IT IS HOW I PLAYED OK!?)
    Game ends when one side lose all the battleships
    '''
    print("Welcome back Admiral O7","\nThis time we have Admiral Computer against us!")
    #Initialize the game
    user_board = initialize_board()
    user_battleships = create_battleships()
    ai_board = initialize_board()
    ai_battleships = create_battleships()
    players["AI"] = [ai_battleships, ai_board]
    players["Player"] = [user_board, user_battleships]
    ai_board = place_battleships(algorithm="custom")
    user_board = place_battleships(algorithm="random")
    hit = True
    x = 0
    #AI Opponent Game Loop
    while x == 0:
        print("Your Turn") #Your Turn
        while hit == True:
            if all(value == 0 for value in user_battleships.values()) or all(value == 0 for value in ai_battleships.values()):
                x = 1
                break
            coordinates = cli_coordinates_input()
            hit, ai_board, ai_battleships = attack(coordinates, ai_board , ai_battleships)
        hit = True
        print("Admiral Computer's Turn") #AI Opponent's Turn
        while hit == True:
            if all(value == 0 for value in user_battleships.values()) or all(value == 0 for value in ai_battleships.values()):
                 x = 2
                 break
            coordinates = generate_attack()
            hit, user_board , user_battleships = attack(coordinates, user_board, user_battleships)
            print(ascii(user_board))
        hit = True
    #Ending check and messages
    if x==1:
        print("Oh wait...We have no ship left!")
        print("|GAME OVER| You lose. \nRETREAT! RETREAT! !!!")
    elif x==2:
        print("Oh wait...He has no ships!")
        print("|GAME OVER| You WİN! \nAdmiral Computer is falling down, falling down...")
    else:
        raise EOFError("Excuse me?!")

   
if __name__ == "__main__":
    generate_attack()
    ai_opponent_game_loop()