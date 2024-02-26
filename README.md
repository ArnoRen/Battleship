# BATTLESHIPS
730055520 - Furkan Burak Yalcintepe (c)

## Description
A battleship game which can be played in terminal and can play player vs computer with flask at browser.
Also has 1-player mode and 2-player mode(vs computer) and 2-player on browser.
## Functions
### initialize_board:
```Python
initialize_board(size=10)
```

Initializing the Board for the game by creating a list with 10x10 and none values.
Board begins from (0,0) to (9,9)

**Methods**:

*size* = Size of board (*size* x *size*) ex.(10x10)

**Return**

board = *size* list of *size* long list

### create_battleships:
```Python
create_battleships(filename = "battleship.txt")
```

Reading battleships.txt(filename) file and returns a dictionary called battle_ships.
    Filename is the name of the .txt file with battleship info.

**Methods**:

*filename* = Filename or directory of the text file of battleship values.

**Return**

battle_ships = dictionary of battleship with size values.

### place_battleships:
```Python
place_battleships(board = initialize_board() , battle_ships = create_battleships(), algorithm= "simple")
```

Placing battleships on board and updating the board.
    
    Algortihms:
    simple - Placing each battleship horizontal on a new rows starting from (0,0) 
    random - Placing the battleships in random positions and orientations.
    custom - Placing the battleships based on placement.json file

**Methods**:

*board* = The board (series of list) to place battleships on.

*battle_ships* = Dictionary of battleships and their size as value to place.

*algorithm* = Method of placing battleships.

**Return**

board = updated version of board with ships on

### flask_user_placement:
```Python
flask_user_placement(board,battle_ships,ships)
```

Placement method created due to need of placement method without reading json file.

**Methods**:

*board* = The board (series of list) to place battleships on.

*battle_ships* = Dictionary of battleships and their size as value to place.

*ships* = Dictionary with placement variables of ships.

### attack:
```Python
attack(coordinates, board, battle_ships)
```

Generating attacks on board. 
    The function returns True if there is and this is a 'Hit' else
    if it is a 'Miss' the function returns False.
    Additionally, the coordinates position in the board data is updated
    to None and the size value in the battleships dictionary is decremented.
    If the value in the battleships data is decremented to zero, you have sunk that battle ship.

**Methods**:

*coordinates* = Tuple value ex.(3,1) x and y value to attack on board

*board* = Board to attack

*battle_ships* = Battleships dictionary which will decrease the hit ship's value.

**Return**

hit = *Bool* value that if it hit or not.

board = Attacked board.

battle_ships = Updated battleships dictionary.

### cli_coordinates_input:
```Python
cli_coordinates_input()
```

This function request the user to input coordinates for an attack and process the input
    to return a tuple containing row and column, ex. (3, 1)

**Methods**:

*None*

**Return**

coordinates = Tuple value ex.(3,1) x and y value to attack on board

### single_game_loop:
```Python
simple_game_loop()
```

1 Player mode, sets the game and take coordinates from user until there is no ship standing.

**Methods**:

*None*

**Return**

*None*

### generate_attack:
```Python
generate_attack()
```

Create random tuple ex.(3,1) for AI to attack.

**Methods**:

*None*

**Return**

coordinates = Tuple value ex.(3,1) x and y value to attack on board

### ai_opponent_game_loop:
```Python
ai_opponent_game_loop(players=players)
```

2 Player (Against Computer) Game Mode
    User's battleship placement is custom
    AI's battleship placement is random
    If you hit you get one more turn (IT IS HOW I PLAYED OK!?)
    Game ends when one side lose all the battleships

**Methods**:

players = Dictionary of players with names.
```
players = {"Player" : [],
           "AI" : []} 
```

**Return**

*None*

### placement_interface:
```Python
placement_interface()
```

Function for flask to render the placement page.

**Methods**:

*None*

**Return**

*None*

### root:
```Python
root()
```

Function for flask to render the gameplay page.

**Methods**:

*None*

**Return**

*None*

### game_attack:
```Python
game_attack()
```

Function for flask for attacking mechanics and game ending.

**Methods**:

*None*

**Return**

*None*

## Data
**battleships.txt** = .TXT file with battleships name and size

**placement.json** = .json file with battleships name and their placement values ex['x', 'y','h'] row, column and orientation of ship.

**main.html** = .html file, template of gameplay page in main.py

**placement.html** = .html file, template of placement page in main.py
## Notes
* Some files gives error when they work on their main page due to if __name__ == "__main__" run the functions line by line and they will work.
* With comments and print I tried to have fun and add fun lines.
* To make browser work you have to go to 127.0.0.1/placement in browser after running.
* Some of the comments I made is explanatory for themselves I reflected my emotions on extreme.
* Licence is MIT License without allowing selling.
* ENJOY :)