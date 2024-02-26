import random
import json

def initialize_board(size=10):
    '''Initializing the Board for the game by creating a list with 10x10 and none values.
    Board begins from (0,0) to (9,9)'''
    board = [[None]*size for _ in range(size)] #Creating a board
    return board


def create_battleships(filename= "battleships.txt"):
    '''Reading battleships.txt(filename) file and returns a dictionary called battle_ships.
    Filename is the name of the .txt file with battleship info.'''
    battle_ships= {}
    with open(filename) as ships: #Read and build battleships
        liste= ships.readlines()
        for i in liste:
           (name,size)=i.split(":")
           battle_ships[name]=int(size.strip())
    return battle_ships

battleship = create_battleships()

def place_battleships(board = initialize_board() , battle_ships = create_battleships(), algorithm= "simple"):
    '''Placing battleships on board and updating the board.
    
    Algortihms:
    simple - Placing each battleship horizontal on a new rows starting from (0,0) 
    random - Placing the battleships in random positions and orientations.
    custom - Placing the battleships based on placement.json file'''
    
    #Simple Algorithm
    if algorithm == "simple":
        for name, size in battle_ships.items():
            placed = False
            row = -1
            while not placed:
                try:
                    row += 1
                    col = 0 #Only horizontal and beginning from first column
                    for i in range(size):
                        if board[row][col + i] is not None:
                            raise ValueError("Ship overlap detected.")
                    for i in range(size):
                        board[row][col + i] = name
                    placed = True
                except:
                    pass
    
    #Random Algorithm
    elif algorithm == "random":
        for name, size in battle_ships.items():
            placed = False
            while not placed:
                try:
                    row = random.randint(0, 9) #Random
                    col = random.randint(0, 9 - (size + 1)) #To make sure it will fit on board
                    rot = random.choice(["horizontal","vertical"])
                    if rot == "horizontal": #Algorithm for horizontal placement
                        for i in range(size):
                            if board[row][col + i] is not None:
                                raise ValueError("Ship overlap detected.")
                        for i in range(size):
                            board[row][col + i] = name
                        placed = True
                    elif rot == "vertical": #Algorithm for vertical placement
                        for i in range(size):
                            if board[row + i][col] is not None:
                                raise ValueError("Ship overlap detected.")
                        for i in range(size):
                            board[row + i][col] = name
                        placed = True
                except:
                    pass
    
    #Custom Algorithm
    elif algorithm == "custom":
        custom_placement_pre = {}
        with open("placement.json", "r") as place: #Read and process .json file
            custom_placement_pre = json.load(place)
        for name, value in custom_placement_pre.items():
            placed = False
            while not placed:
                try:
                    #Placements based on .json file
                    row = int(value[0])
                    col = int(value[1])  
                    rot = value[2]
                    size = battle_ships[name] #Getting appropriate size info from battle_ships
                    if rot == "h":
                        for i in range(size): 
                            if board[row][col + i] is not None:
                                raise ValueError("Ship overlap detected.")
                        for i in range(size):
                            board[row][col + i] = name
                        placed = True
                    elif rot == "v":
                        for i in range(size):
                            if board[row + i][col] is not None:
                                raise ValueError("Ship overlap detected.")
                        for i in range(size):
                            board[row + i][col] = name
                        placed = True
                except:
                    raise ValueError("AAAHHH!!!") #Custom system gave me some rough time
            
    else:
        raise ValueError("Please put a appropriate algorithm!")
    return board

def flask_user_placement(board,battle_ships,ships): #Function for the flask app
    custom_placement_pre = ships
    for name, value in custom_placement_pre.items():
        placed = False
        while not placed:
            try:
                #Placements based on data variable
                row = int(value[1])
                col = int(value[0])   #Due to problems I got to change their order
                rot = value[2]
                size = battle_ships[name] #Getting appropriate size info from battle_ships
                if rot == "h":
                    for i in range(size): 
                        if board[row][col + i] is not None:
                            raise ValueError("Ship overlap detected.")
                    for i in range(size):
                        board[row][col + i] = name
                    placed = True
                elif rot == "v":
                    for i in range(size):
                        if board[row + i][col] is not None:
                            raise ValueError("Ship overlap detected.")
                    for i in range(size):
                        board[row + i][col] = name
                    placed = True
            except:
                raise ValueError("AAAHHH!!!?") 
    return board

board = initialize_board()
battleship = create_battleships()
place_battleships(board, battleship,"random")

if __name__ == "__main__":
    initialize_board()
    create_battleships()
    place_battleships()
    flask_user_placement()
