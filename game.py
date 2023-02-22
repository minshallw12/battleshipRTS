from classes import *
# game play goes here

def start():
    #player initialization
    #player_name = str(input("What is your name Admiral? > "))
    color_prompt = """
        What team?
1. Blue
2. Red
3. YelloW
"""
    
    user_input = input(color_prompt)            #choose team color
    color = ''
    if user_input == 1:
        color = 'blue'
    if user_input == 2:
        color = 'red'
    if user_input == 3:
        color = 'yellow'

    prompt = """

1. Carrier
2. Submarine
3. Destroyer
    """
    def initialize_ship(team, ship_type):
        if ship_type == 1:
            return Carrier(team, str(input("Whats the name of this vessel? > ")))
        if ship_type == 2:
            return Submarine(team, str(input("Whats the name of this vessel? > ")))
        if ship_type == 3:
            return Destroyer(team, str(input("Whats the name of this vessel? > ")))

    ship_type = str(input(prompt))
    ship1 = initialize_ship(color, ship_type)
    ship2 = initialize_ship(color, ship_type)
    ship3 = initialize_ship(color, ship_type)
    player_fleet = [ship1, ship2, ship3]            #beginning fleet
    
    print(player_fleet)






start()



        





