from flask import Flask, render_template, request, jsonify, session
from components import initialize_board, create_battleships, place_battleships, flask_user_placement
from game_engine import attack
from mp_game_engine import generate_attack

#Initialization
app = Flask(__name__)
app.secret_key = 'Why'
board = initialize_board()

#Ship Placement Page
@app.route("/placement" , methods=['GET', 'POST'])
def placement_interface():
    '''Game Placement Page'''
    if request.method =="GET":
        ships = create_battleships() 
        session['ships'] = ships #Storing ship value to tranfer across functions
        return render_template("placement.html", ships=ships , board_size= 10)
    elif request.method == 'POST':
        data = request.get_json()
        session['data'] = data #Storing placement data to tranfer across functions
        return jsonify({'message': 'Received'}), 200

#Gameplay Page
@app.route('/', methods=["GET"])
def root():
    '''Gameplay Page'''
    #Initializing basic game variables
    ai_board = initialize_board()
    ai_battleships = create_battleships()
    ai_board = place_battleships(ai_board, ai_battleships, "random")  #AI placement
    if request.method =="GET":
        data = session.get('data')
        user_battle_ships = session.get('ships')
    user_board = flask_user_placement(board, user_battle_ships, data) #Placement
    #Making variables to transfer across functions
    session["user_board"] = user_board
    session["user_battle_ships"] = user_battle_ships
    session["ai_board"]= ai_board
    session["ai_battleships"] = ai_battleships
    return render_template('main.html', player_board= user_board)

#Attack Route
@app.route("/attack", methods=["GET"])
def game_attack():
    '''Game attacking mechanics and logging'''
    #Initializing variables
    user_board = session.get('user_board')
    user_battle_ships = session.get('user_battle_ships')
    ai_board = session["ai_board"]
    ai_battleships = session["ai_battleships"]
    if request.method=="GET":
        #Getting coordinates
        x = request.args.get('x')
        y = request.args.get('y')
        coordinates = (int(y),int(x)) 
        x, y = generate_attack() #Creating AI's attack
        AI_Turn = (y,x)
        hit, ai_board, ai_battle_ships = attack(coordinates, ai_board, ai_battleships) #User's attack
        #Game Loop
        if any(value != 0 for value in user_battle_ships.values()) and any(value != 0 for value in ai_battleships.values()):
            if hit == True: #Did I hit?
                session["user_board"] = user_board
                session["user_battle_ships"] = user_battle_ships
                session["ai_board"]= ai_board    #I was sick of not updating so I took the dirty way
                session["ai_battleships"] = ai_battleships
                return jsonify({'hit': True,
                'AI_Turn': AI_Turn
                })
            else:
                session["user_board"] = user_board
                session["user_battle_ships"] = user_battle_ships
                session["ai_board"]= ai_board    #I was sick of not updating so I took the dirty way
                session["ai_battleships"] = ai_battleships
                return jsonify({'hit': False,
                'AI_Turn': AI_Turn
                })
        else: #Finishing and check who won and game end messages
            if all(user_battle_ships.values())==0: #I lose
                return jsonify({'hit': hit,
                'AI_Turn': AI_Turn,
                'finished': '|GAME OVER| You lose. \nRETREAT! RETREAT! !!!'})
            elif all(ai_battleships.values()) == 0: #I win
                return jsonify({'hit': hit,
                'AI_Turn': AI_Turn,
                'finished': '|GAME OVER| You WİN! \nAdmiral Computer is falling down, falling down...'})
            else:
                raise ValueError("WHAT AGAIN NOW!!!")
        hit, user_board, user_battle_ships = attack(AI_Turn, user_board, user_battle_ships) #AI attack

if __name__ == '__main__':
    app.template_folder = "templates" #Where template html files are at
    app.run()