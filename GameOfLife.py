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
            else:
                ar[i][x]="_"
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
def check_neighbors(ar):
    rows = len(ar)
    cols = len(ar[0])
    NextGeneration = [['',' ',' ',' ',' ' ],
          [' ',' ',' ',' ',' ' ],
          [' ',' ',' ',' ',' ' ],
          [' ',' ',' ',' ',' ' ],
          [' ',' ',' ',' ',' ' ]]
    #this counter will calculate the surrounding neighbors
    #if this counter is equal to 2 or 3 then the cell will live
    # otherwise if its greater than 3 or less than 2 it will die
    for i in range(rows-1):
        Neighbor = 0
        for x in range(cols-1):
            if(ar[i][x] == "*"):
                #this will now check to the left and the right
                #Checking all the corners
                if(x == cols):
                    if(i == 0):
                        #top right corner
                        if(ar[i][x] == ar[i+1][x]):
                            Neighbor = Neighbor + 1
                        if(ar[i][x]==ar[i][x-1]):
                            Neighbor = Neighbor + 1
                    elif(i == rows ):
                        #bottom right corner
                        if(ar[i][x] == ar[i-1][x]):
                            Neighbor = Neighbor + 1
                        if(ar[i][x]==ar[i][x-1]):
                            Neighbor = Neighbor + 1
                elif(x == 0):
                    if(i==0):
                        #top left
                        if(ar[i][x]==ar[i][x+1]):
                            Neighbor = Neighbor + 1
                        if(ar[i][x] == ar[i+1][x]):
                            Neighbor = Neighbor + 1
                    elif(i==rows):
                        #bottom left corner
                        if(ar[i][x]==ar[i-1][x]):
                            Neighbor=Neighbor+1
                        if(ar[i][x]==ar[i][x+1]):
                            Neighbor = Neighbor + 1
                ##checking everything besides corners
                ##starting off with top row checking left right and down
                elif(i==0 and x !=0 and x != cols ):
                    if(ar[i][x]==ar[i+1][x]):
                        Neighbor=Neighbor+1
                    if(ar[i][x]==ar[i][x+1]):
                        Neighbor=Neighbor+1
                    if(ar[i][x]==ar[i][x-1]):
                        Neighbor=Neighbor+1
                elif(i==rows and x!=0 and x !=cols):
                    ##bottom row checking left right and up
                    if(ar[i][x]==ar[i][x+1]):
                        Neighbor=Neighbor+1
                    if(ar[i][x]==ar[i][x-1]):
                        Neighbor=Neighbor+1
                    if(ar[i][x]==ar[i-1][x]):
                        Neighbor=Neighbor+1
                elif(i != rows and i !=0 and x != cols  and x != 0):
                    ##now we can check in every direction (up down left and right)
                    if(ar[i][x]==ar[i][x+1]):
                        Neighbor=Neighbor+1
                    if(ar[i][x]==ar[i][x-1]):
                        Neighbor=Neighbor+1
                    if(ar[i][x]==ar[i-1][x]):
                        Neighbor=Neighbor+1
                    if(ar[i][x]==ar[i+1][x]):
                        Neighbor=Neighbor+1
                
                    
                if (Neighbor == 2 or Neighbor == 3):
                    NextGeneration[i][x] = "*"
    #fill in the blanks
    for i in range(rows):
        for x in range(cols):
            if(NextGeneration[i][x] !="*"):
                NextGeneration[i][x] ="_"
    return NextGeneration


def GameOfLife(ar,x):
    #begin recursive calls
    previousBoardState = ar
    nextGeneration = check_neighbors(ar)
    #check if this generation is all dead now
    EmptyMap = True
    rows = len(ar)
    cols = len(ar[0])
    for i in range(rows):
        for j in range(cols):
            if(ar[i][j] =="*"):
                EmptyMap = False
    if (EmptyMap == True):
        print("Game has ended")
    else:
        x=x+1
        print("Generation: ",x)
        display_array(nextGeneration)
        
    if(previousBoardState != nextGeneration):
       GameOfLife(nextGeneration,x)
    
def main():
    
    ar = [['',' ',' ',' ',' ' ],
          [' ',' ',' ',' ',' ' ],
          [' ',' ',' ',' ',' ' ],
          [' ',' ',' ',' ',' ' ],
          [' ',' ',' ',' ',' ' ]]
    ar= RandomlyFillArray(ar)
    print("Generation: 1")
    x = 1
    display_array(ar)
    GameOfLife(ar,x)

    


# add live cells that fulfil any of the rules to a list
#so they can be compared to with others later
