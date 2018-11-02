"""
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games results. You are given a result of a game and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".
Example:
	checkio([
	    "X.O",
	    "XX.",
	    "XOO"]) == "X"
	checkio([
	    "OO.",
	    "XOX",
	    "XOX"]) == "O"
	checkio([
	    "OOX",
	    "XXO",
	    "OXX"]) == "D"
"""
from typing import List


def checkio(result):
    rows = result
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)

    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'

def checkio_v2(board):
    # First we put everything together into a single string
    x = "".join(board)
    
    # Next we outline the 8 possible winning combinations. 
    combos = ["012", "345", "678", "036", "147", "258", "048", "246"]
    
    # We go through all the winning combos 1 by 1 to see if there are any
    # all Xs or all Os in the combos
    for i in combos:
        if x[int(i[0])] == x[int(i[1])] == x[int(i[2])] and x[int(i[0])] in "XO":
            return x[int(i[0])]
    return "D" 

def checkio_v3(game_result):
    sample = "".join(game_result)
    data = game_result + [sample[i:9:3] for i in range(3)] + [sample[0:9:4], sample[2:8:2]]

    if "OOO" in data:
        return "O"
    elif "XXX" in data:
        return "X"
    else:
        return "D"


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")