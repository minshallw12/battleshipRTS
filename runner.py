from classes import *
from game import *

high_score = 0
prompt = """
== Battleships Turn Based Strategy ==
1. Play
2. View high score
3. Instruction
4. Exit

"""

while True:
    selection = int(input(prompt))

    if selection == 1:
        start()
        pass
    if selection == 2:
        #view high score code
        pass
    if selection == 3:
        #print instruction
        pass
    if selection == 4:
        break
