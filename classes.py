
class Ship:
    how_many_ships = 0          # to access how many ships in game

    def __init__(self, color, name, health, defense, attack):
        self._name = name
        self._health = health
        self._defense = defense
        self._attack = attack
        self._sunk = False
        self._color = color
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
            "Team":self.get_color(),
            "Name:":self.get_name(),
            "Health:":self.get_health(),
            "Defense:":self.get_defense(),
            "Attack:": self.get_attack()
        }
    def get_color(self):
        return self._color
    def attack(self, enemy):
        attack_roll = self.get_attack()
        print(f"{self.get_name()} attacked {enemy.get_name()}.")
        return attack_roll
    def attacked_by(self, attack_roll):
        damage = abs(attack_roll - self.get_defense())
        self._health -= damage
        print(f'{self.get_name()} took {damage} damage!')
        if self.get_health() <= 0:
            self._sunk = True
            print(f'{self.get_name()} has sunk...')
            Ship.how_many_ships -= 1
    def healed_by(self, heal_roll):
        self._health += heal_roll
        print(f'{self.get_name()} recieved {heal_roll} HP!')


# health is usually set between 0 and 1000, defense on a scale of 1 to 5, attack from 10 to 200

# class SEALs(Ship):                    #cool feature but not totatlly necessary for the beginning framework
#     how_many_squads = 0
#     def __init__(self, name='Unnamed Squad', health=10, defense=10, primary_attack=200, secondary_attack=1):
#         super().__init__(name, health, defense, primary_attack)
#         self._secondary_attack = secondary_attack                
#         # if SEALs.how_many_squads == 1:                            #debug to only allow one seal squad per team
#         #     print('SEALS are already in the combat zone')
#         #     return
#         # else:
#         #     SEALs.how_many_squads += 1

class Carrier(Ship):
    how_many_carriers = 0
    def __init__(self, color, name='Unnamed Carrier', health=1000, defense=5, primary_attack=10):
        super().__init__(color,name, health, defense, primary_attack)
        Carrier.how_many_carriers += 1
        self._aircraft = True
        self._SEALs = True
        print(f"{name} has been created as a carrier.")

    def deploy_aircraft(self):
        if self._aircraft == True:
            return 
            
    def get_stats(self):
        return {
            "Team":self.get_color(),
            "Name:":self.get_name(),
            "Health:":self.get_health(),
            "Defense:":self.get_defense(),
            "Attack:": self.get_attack(),
            "Aircraft Onboard:": self._aircraft,
            "SEALs Onboard:": self._SEALs
        }
    # def deploy_SEALs(self):               #part of seal feature
    #     if self._SEALs == True:
    #         return SEALs()
    #     else:
    #         print('No SEALs aboard.')
    #         return

class Submarine(Ship):
    how_many_submarines= 0
    def __init__(self, color, name='Unnamed Submarine', health=200, defense=2, primary_attack=10):
        super().__init__(color, name, health, defense, primary_attack)
        Submarine.how_many_submarines += 1        
        self._secondary_attack = 50
        self._underwater = False
        self._SEALs = False
        print(f"{name} has been created as a submarine")

    def get_stats(self):
        return {
            "Team":self.get_color(),
            "Name:":self.get_name(),
            "Health:":self.get_health(),
            "Defense:":self.get_defense(),
            "Attack:": self.get_attack(),
            "Submerged:":self._underwater,
            "SEALs Onboard:": self._SEALs
        }
    def get_underwater_status(self):
        return self._underwater
    def dive(self):
        print(f'{self.get_name()} is diving...')
        print('     Dive! Dive! Dive!')
        self._underwater = True
    def surface(self):
        print(f'{self.get_name()} is surfacing...')
        print('     Ready to surface in all respects.')
        self._underwater = False
    def deploy_SEALs(self):
        if self._SEALs == True:
            SEAL_team = SEALs()
            return SEAL_team

class Destroyer(Ship):
    how_many_destroyers= 0
    def __init__(self, color, name='Unnamed Destroyer', health=200, defense=2, primary_attack=10):
        super().__init__(color, name, health, defense, primary_attack)
        Destroyer.how_many_destroyers += 1 

class Cruiser(Ship):
    how_many_cruisers= 0
    def __init__(self, color, name='Unnamed Cruiser', health=500, defense=3, primary_attack=15):
        super().__init__(color, name, health, defense, primary_attack)
        Cruiser.how_many_cruisers += 1

class Battleship(Ship):
    how_many_battleships= 0
    def __init__(self, color, name='Unnamed Battleship', health=500, defense=3, primary_attack=15):
        super().__init__(color, name, health, defense, primary_attack)
        Battleship.how_many_battleships += 1

class Tender(Ship):
    how_many_tenders= 0
    def __init__(self, color, name='Unnamed Tender', health=200, defense=2, primary_attack=10):
        super().__init__(color, name, health, defense, primary_attack)
        Tender.how_many_tenders += 1
    def heal(self, ally):
        heal_roll = self.get_attack()
        print(f"{self.get_name()} healed {ally.get_name()}")
        return heal_roll

class Skiff(Ship):
    how_many_skiffs= 0
    def __init__(self, color, name='Unnamed Skiff', health=10, defense=0, primary_attack=2):
        super().__init__(color, name, health, defense, primary_attack)
        Skiff.how_many_skiffs += 1

class Transport(Ship):
    how_many_transports= 0
    def __init__(self, color, name='Unnamed Transport', health=200, defense=2, primary_attack=10):
        super().__init__(color, name, health, defense, primary_attack)
        Transport.how_many_transports += 1

class Pirate(Ship):
    how_many_pirates= 0
    def __init__(self, color, name='Unnamed Destroyer', health=5, defense=0, primary_attack=1):
        super().__init__(color, name, health, defense, primary_attack)
        Pirate.how_many_pirates += 1


# class Building:
#     how_many_buildings = 0
#     def __init__(self, color, health=1000,):
#          Building.how_many_buildings +=1
#          self.color = color
#          self.health = health
#          self.queue = []
#     def get_color(self):
#         return self.color
#     def get_health(self):
#         return self.health
#     def get_queue(self):
#         return self.queue
#     def get_stats(self):
#         return {
#             "Team":self.get_color(),
#             "Health:":self.get_health(),
#             "Queue":self.queue
#         }

# class Shipyard(Building):
#     def create_ship(self, ship_type, name):
#         if ship_type == 'Destroyer':
#             return Destroyer(name)
#         elif ship_type == 'Carrier':
#             return Carrier(name)
#         elif ship_type == 'Submarine':
#             return Submarine(name)
#         elif ship_type =='Battleship':
#             return Battleship(name)
         
# class Oil_rig(Building):
# class Naval_base(Building)



#------------------------------------------- Playground ----------------------------------------------
# shipyard1.create_ship("Carrier","USS Enterprise")
# carrier1 = Carrier('Blue','USS Enterprise')
# submarine1 = Submarine('Red','USS Virginia')
# battleship1 = Battleship('Red',"USS Arizona")
# tender1 = Tender('Blue',"HMS King James")
# pirates1 = Pirate('Blue',"Somali Pirates")
# cruiser1 = Cruiser('Red',"HMS King James")

# submarine1.dive()                                       #submarine dives
# carrier1.attacked_by(submarine1.attack(carrier1))       #sub attacks carrier 4 times    
# carrier1.attacked_by(submarine1.attack(carrier1))
# carrier1.attacked_by(submarine1.attack(carrier1))
# carrier1.attacked_by(submarine1.attack(carrier1))
# submarine1.surface()                                    #submarine surfaces
# submarine1.attacked_by(carrier1.attack(submarine1))     #carrier attacks submarine once
# submarine1.healed_by(tender1.heal(submarine1))          #tender heals submarine

# print(carrier1.get_stats())
# print(submarine1.get_stats())      