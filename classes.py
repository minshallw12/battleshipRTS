class Ship:
    how_many_ships = 0          # to access how many ships in game

    def __init__(self, name, health, defense, attack):
        self._name = name
        self._health = health
        self._defense = defense
        self._attack = attack
        self._sunk = False
        Ship.how_many_ships += 1
    def get_name(self):
        return self._name
    def get_health(self):
        return self._health
    def get_defense(self):
        return self._defense
    def get_attack(self):
        return self._attack
    def get_stats(self):
        return {
            "Name:":self.get_name(),
            "Health:":self.get_health(),
            "Defense:":self.get_defense(),
            "Attack:": self.get_attack()
        }
    def attack(self):
        attack_roll = self.get_attack()
        return attack_roll
    def attacked(self, attack_roll):
        self._health -= (attack_roll - self.get_defense())
        if self.get_health() <= 0:
            self._sunk = True
            Ship.how_many_ships -= 1


class SEALs(Ship):
    how_many_squads = 0
    def __init__(self, name='Unnamed Squad', health=10, defense=10, primary_attack=200, secondary_attack=1):
        super().__init__(name, health, defense, primary_attack)
        self._secondary_attack = secondary_attack                
        # if SEALs.how_many_squads == 1:                            #debug to only allow one seal squad per team
        #     print('SEALS are already in the combat zone')
        #     return
        # else:
        #     SEALs.how_many_squads += 1

class Carrier(Ship):
    how_many_carriers = 0
    def __init__(self, name='Unnamed Carrier', health=500, defense=10, primary_attack=10):
        super().__init__(name, health, defense, primary_attack)
        Carrier.how_many_carriers += 1
        self._aircraft = True
        self._SEALs = True
    def deploy_aircraft(self):
        if self._aircraft == True:
            return 
    def deploy_SEALs(self):
        if self._SEALs == True:
            return SEALs()
        else:
            print('No SEALs aboard.')
            return

class Submarine(Ship):
    how_many_submarines= 0
    def __init__(self, name='Unnamed Submarine', health=100, defense=20, primary_attack=20):
        super().__init__(name, health, defense, primary_attack)
        Submarine.how_many_submarines += 1        
        self._secondary_attack = 50
        self._underwater = False
        self._SEALs = False
    
    def get_underwater_status(self):
        return self._underwater
    def dive(self):
        print('Dive! Dive! Dive!')
        self._underwater = True
    def surface(self):
        print('Ready to surface in all respects.')
        self._underwater = False
    def deploy_SEALs(self):
        if self._SEALs == True:
            SEAL_team = SEALs()
            return SEAL_team

# class Destroyer(Ship):
# class Cruiser(Ship):
# class Battleship(Ship):
# class Tender(Ship):
# class Skiff(Ship):
# class Transport(Ship):
# class Pirate(Ship): 

SEAL_team1 = SEALs('SEALs')
carrier1 = Carrier('USS Enterprise')
submarine1 = Submarine('USS Virginia')

print(SEAL_team1.get_stats())
print(carrier1.get_attack())
print(submarine1.how_many_squads)
print(SEAL_team1.how_many_squads)
# class Building:
#     how_many_buildings = 0

#     def __init__(self, health, queue_length)
#         Building.how_many_buildings +=1
#         self.health = health
#         self.queue = queue_length

#     def create_ship(self, ship_type)

# class Shipyard(Building):
# class Oil_rig(Building):
# class Naval_base(Building)


