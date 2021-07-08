import random

def main():
    stonesLeft = 20
    actualTurn = 0
    ###################################################
    while True:
        print("There are", stonesLeft, "stones left")
        actualTurn += 1
        actualPlayer = actualTurn % 2
        actualPlayer = 2 if actualPlayer == 0 else 1
        StonetoRemove = int(input("Player "+str(actualPlayer)+" would you like to remove 1 or 2 stones? "))
        while StonetoRemove != 1 and StonetoRemove != 2:
            StonetoRemove = int(input("Please enter 1 or 2: "))
        print("")
        stonesLeft -= StonetoRemove
        if stonesLeft <= 0:
            break
    ###################################################
    actualTurn += 1
    if actualTurn % 2 == 0:
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")

if __name__ == '__main__':
    main()
