import random
from bke import *

class MyRandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1,500)

class MijnSpeler(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        getal = 1
        if board[4] == my_symbol:
            getal += 2
        if can_win(board, my_symbol):
            getal += 3
        if is_winner(board, my_symbol):
            getal = 10
        elif can_win(board, opponent_symbol):
            getal = -10
        return getal
 
mijn_speler = MijnSpeler()
my_random_agent = MyRandomAgent()
start(player_o=mijn_speler, player_x=my_random_agent)

