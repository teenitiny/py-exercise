"""
Chess is a two-player strategy game played on a checkered game board laid out in eight rows (called ranks and denoted with numbers 1 to 8) and eight columns (called files and denoted with letters a to h) of squares. Each square of the chessboard is identified by a unique coordinate pair — a letter and a number (ex, "a1", "h8", "d6"). For this mission we only need to concern ourselves with pawns. A pawn may capture an opponent's piece on a square diagonally in front of it on an adjacent file, by moving to that square. For white pawns the front squares are squares with greater row number than the square they currently occupy.

A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall. With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square. We have several white pawns on the chess board and only white pawns. You should design your code to find how many pawns are safe.

Example:
	safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
	safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
"""

def safe_pawns(pawns: set) -> int:
    num = 0
    for point in pawns:
        if is_safe(point ,pawns):
            num += 1
    return num

def is_safe(point, pawns):
    safe_point_left = chr(ord(point[0]) - 1) + str(int(point[1]) - 1)
    safe_point_right = chr(ord(point[0]) + 1) + str(int(point[1]) - 1)
    return safe_point_left in pawns or safe_point_right in pawns


def is_safe_v2(point, pawns):
	c, r = map(ord, pawn)
	return chr(c-1) + chr(r-1) in pawns or chr(c+1) + chr(r-1)

def safe_pawns_v2(pawns):
    
    def is_safe(p):
        file, rank = ord(p[0]), int(p[-1])
        return (chr(file-1)+str(rank-1) in pawns or 
                chr(file+1)+str(rank-1) in pawns)
        
    return sum(is_safe(p) for p in pawns)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")