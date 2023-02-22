from classes import *
# game play goes here

def start():
    #player initialization
    #player_name = str(input("What is your name Admiral? > "))

    prompt = """

    1. Carrier
    2. Submarine
    3. Destroyer
    """
    player_fleet = []

    def initialize_ship(team, ship_type):
        if ship_type == 1:
            return Carrier(team, str(input('What do you name this vessel? > ')))
        if ship_type == 2:
            return Submarine(team, str(input('What do you name this vessel? > ')))
        if ship_type == 3:
            return Destroyer(team, str(input('What do you name this vessel? > ')))

    ship1 = initialize_ship('blue', 1)
    print(ship1.get_attack())
    # ship1_type = str(input(f'== Choose 3 ships for your fleet ==\n{prompt}'))
    # ship1 = initialize_ship(ship1_type, ship1_name)
    # player_fleet.append(ship1)
    # print(player_fleet)

    # ship2_type = str(input(f'== Choose 2 ships for your fleet ==\n{prompt}'))
    # ship1_name = str(input('What do you name this vessel? > '))
    # ship2 = initialize_ship(ship2_type, ship2_name)
    # player_fleet.append(ship2)
    # print(player_fleet)

    # ship3_type = str(input(f'== Choose 1 ship for your fleet ==\n{prompt}'))
    # ship1_name = str(input('What do you name this vessel? > '))
    # ship3 = initialize_ship(ship3_type, ship3_name)
    # player_fleet.append(ship3)
    # print(player_fleet)




start()



        





