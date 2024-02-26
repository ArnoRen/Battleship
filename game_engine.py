from components import initialize_board, create_battleships, place_battleships

def attack(coordinates, board, battle_ships):
    '''Generating attacks on board. 
    The function returns True if there is and this is a 'Hit' else
    if it is a 'Miss' the function returns False.
    Additionally, the coordinates position in the board data is updated
    to None and the size value in the battleships dictionary is decremented.
    If the value in the battleships data is decremented to zero, you have sunk that battle ship.'''
    row, column = coordinates
    #Checking for ships
    if board[row][column] is not None: 
        print("Hit!")
        name = board[row][column]
        battle_ships[name] -= 1 #Taking a hit returns as value decreasing
        board[row][column] = None
        if battle_ships[name] == 0:
            print("The Ship has sunk, May God Have Mercy on them...") #If value is 0, ship has sunk
        return True, board, battle_ships
    elif board[row][column] is None:
        print("Miss...")
        return False, board, battle_ships
    else:
        raise ValueError("WHAT IS HAPPENING??... GOD OF BUGS!!!")

def cli_coordinates_input():
    '''This function request the user to input coordinates for an attack and process the input
    to return a tuple containing row and column, ex. (3, 1) '''
    row = int(input("Row:")) # row value (row, )
    col = int(input("Column:")) #column value ( , column)
    if not (0<=row<10) or not (0<=col<10):
        raise ValueError("Put coordinates between board size")
    coordinates = (row, col)
    return coordinates #return as tuple

def simple_game_loop():
    '''1 Player mode, sets the game and take coordinates from user until there is no ship standing.'''
    print("Morning Admiral O7","\nWELCOME!, this war never changes...")
    #Initialize the Game
    board = initialize_board()
    battle_ships = create_battleships()
    board = place_battleships(board, battle_ships, "simple")
    print("Sir, Ready, Sir") #Battle Time
    while any(value > 0 for value in battle_ships.values()): #Until all ships are sunk
        coordinates = cli_coordinates_input()
        hit, board, battle_ships = attack(coordinates, board, battle_ships)

    print("|GAME OVER| All ships has sunk!")
    

if __name__ == "__main__":
    attack()
    cli_coordinates_input()
    simple_game_loop()
