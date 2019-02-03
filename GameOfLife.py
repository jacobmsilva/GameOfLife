#Names of members
#Fehmina
#Victoria
#Jacob S.
#Rules to Game of Life
#Any live cell with fewer than two live neighbors dies,
#as if caused by underpopulation

#Any live cell with two or three live neighbors lives on to the next generation
#Any lvie cell with more than three live neighbors dies, as if by overpopulation
#any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
import os
import time
import random
#starts at zero so really rows = 5 and cols = 5
#this is just easier to read the loops this way


def RandomlyFillArray(ar):
    rows = len(ar)
    cols = len(ar[0])
    for i in range(rows):
        for x in range(cols):
            if (random.randint(0,1)==1):
                ar[i][x]= '*'
    return ar

def display_array(ar):
    "Clear the screen, display the contents of an array, wait for 1sec"
    os.system('clear')
    #grab the rows
    rows = len(ar)

    if rows == 0:
        raise ValueError("Array contains no data")
    #grab the columns - indices start at 0
    cols = len(ar[0])

    for i in range(rows):
        for j in range(cols):
            #no carriage return, space separated
            print(ar[i][j],end=' ')
        print()
    time.sleep(1)
    return ar
def main():
    ar = [[' ',' ',' ',' ',' ' ],
          [' ',' ',' ',' ',' ' ],
          [' ',' ',' ',' ',' ' ],
          [' ',' ',' ',' ',' ' ],
          [' ',' ',' ',' ',' ' ]]
    ar= RandomlyFillArray(ar)
    display_array(ar)


# add live cells that fulfil any of the rules to a list
#so they can be compared to with others later
