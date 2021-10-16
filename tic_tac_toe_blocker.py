#8 Tic Tac Toe blocker

"""In this Python challenge, write a function that’ll accept two numbers. 
These numbers will represent a position on a tic-tac-toe board. 
They can be 0 through 8, where 0 is the top-left spot, and 8 is the bottom-right spot.

These parameters are two marks on the tic-tac-toe board. The function should return the number of the 
spot that can block these two spots from winning the game."""

block_combos = {
    "02" : 1,
    "06" : 3,
    "08" : 4,
    "17" : 4,
    "26" : 4,
    "28" : 5,
    "35" : 4,
    "68" : 7,
    }

"""This assumes that the input is correct - being a number between 0 and 8"""
def move_blocker(square1, square2):

    sq1, sq2 = str(square1), str(square2)

    if square1 < square2:
        key = sq1 + sq2
    else:
        key = sq2 + sq1

    try:
        return block_combos[key]
    except:
        return "No block required"



print(move_blocker(0,2), "| 1")
print(move_blocker(0,8), "| 4")
print(move_blocker(0,6), "| 3")
print(move_blocker(6,8), "| 7")
print(move_blocker(2,8), "| 5")
print(move_blocker(0,1), "| No block required")
print(move_blocker(4,5), "| No block required")
print(move_blocker(0,7), "| No block required")
