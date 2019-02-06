#Names of members
#Fehmina
#Victoria
#Jacob S.
#Rules to Game of Life
#Any live cell with fewer than two live neighbors dies,
#as if caused by underpopulation
#Any live cell with two or three live neighbors lives on to the next generation
#Any live cell with more than three live neighbors dies, as if by overpopulation
#any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
import os
import time
import random
import sys
#makes it so array can be made from user input
def GiveBoundaries(rows,cols):
    a = []
    for i in range(rows):
        a.append([])
        for j in range(cols):
                a[i].append("_")
    return a
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
    NextGeneration = GiveBoundaries(rows,cols)
    #this counter will calculate the surrounding neighbors
    #if this counter is equal to 2 or 3 then the cell will live
    # otherwise if its greater than 3 or less than 2 it will die
    for i in range(rows):
        for x in range(cols):
            Neighbor = 0
            ChancesOfReproduction = 0
            if(ar[i][x] == "*"):
                if(i!=rows-1):
                    if(ar[i][x] == ar[i+1][x]):
                        Neighbor = Neighbor + 1
                if(i!=0):
                    if (ar[i][x] == ar[i-1][x]):
                        Neighbor = Neighbor + 1
                if(x!=cols-1):
                    if (ar[i][x] == ar[i][x+1]):
                        Neighbor = Neighbor + 1
                if(x!=0):
                    if (ar[i][x] == ar[i][x-1]):
                        Neighbor = Neighbor + 1
                ##remove these and statements if you only want it to check up down left and right
                if(x!=0 and i != 0):
                    #checking top left
                    if(ar[i][x]==ar[i-1][x-1]):
                        Neighbor = Neighbor + 1
                if(x!=0 and i != rows-1):
                    #checking bottom left
                    if(ar[i][x]==ar[i+1][x-1]):
                        Neighbor = Neighbor + 1
                if(x!=cols-1 and i !=0):
                    ##checking top right
                    if(ar[i][x] ==ar[i-1][x+1]):
                        Neighbor = Neighbor + 1
                if(x!=cols-1 and i != rows-1):
                    #checking bottom right
                    if(ar[i][x]==ar[i+1][x+1]):
                        Neighbor = Neighbor + 1
                if (Neighbor == 2 or Neighbor == 3):
                    NextGeneration[i][x] = "*"
            if(ar[i][x] =="_"):
                if(i!=rows-1):
                    if(ar[i+1][x] == "*"):
                       ChancesOfReproduction = ChancesOfReproduction + 1
                if(i!=0):
                    if (ar[i-1][x] == "*"):
                       ChancesOfReproduction = ChancesOfReproduction + 1
                if(x!=cols-1):
                    if (ar[i][x+1] == "*"):
                       ChancesOfReproduction = ChancesOfReproduction + 1
                if(x!=0):
                    if (ar[i][x-1] == "*"):
                       ChancesOfReproduction = ChancesOfReproduction + 1
                ##remove these and statements if you only want it to check up down left and right
                if(x!=0 and i != 0):
                    #checking top left
                    if(ar[i-1][x-1]=="*"):
                        ChancesOfReproduction = ChancesOfReproduction + 1
                if(x!=0 and i != rows-1):
                    #checking bottom left
                    if(ar[i+1][x-1]=="*"):
                        ChancesOfReproduction = ChancesOfReproduction + 1
                if(x!=cols-1 and i !=0):
                    ##checking top right
                    if(ar[i-1][x+1] =="*"):
                        ChancesOfReproduction = ChancesOfReproduction + 1
                if(x!=cols-1 and i != rows-1):
                    #checking bottom right
                    if(ar[i+1][x+1]=="*"):
                        ChancesOfReproduction = ChancesOfReproduction + 1
                if(ChancesOfReproduction == 3):
                    NextGeneration[i][x]="*"
                
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
    rows = int(input("Enter the number of desired rows: "))
    cols = int(input("Enter the number of desired colums: "))
    ar=GiveBoundaries(rows,cols)
    ar= RandomlyFillArray(ar)
    print("Generation: 1")
    x = 1
    display_array(ar)
    GameOfLife(ar,x)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main()
    else:
        main()
    


# add live cells that fulfil any of the rules to a list
#so they can be compared to with others later
