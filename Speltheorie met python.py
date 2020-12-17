import random
from bke import *

class MyRandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1,500)

class MijnSpeler(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        getal = 1
        if can_win(board, opponent_symbol):
            getal = getal - 50
        return getal
 
mijn_speler = MijnSpeler()
my_random_agent = MyRandomAgent()
start(player_x=my_random_agent, player_o=mijn_speler)

