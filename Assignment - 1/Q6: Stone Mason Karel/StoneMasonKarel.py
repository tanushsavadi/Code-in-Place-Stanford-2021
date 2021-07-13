from karel.stanfordkarel import *




def main():
    if no_beepers_present(): #Once use: 1x1 escenarie
        put_beeper()
    while front_is_clear(): #Repair the arches
        go_up()
        go_down()
        if front_is_clear():
            next_avenue() #move to the next avenue
            if front_is_blocked(): #check the route and end the code
                turn_left()


def go_up(): #allow go up by the column
    if facing_east():
        turn_left()
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        if front_is_clear():
            move()

def go_down(): #allow go down by the column
    if front_is_blocked():
        turn_around()
    while facing_south():
        if no_beepers_present():
            put_beeper()
        if front_is_clear():
            move()
        if front_is_blocked():
            turn_left()


def turn_around():
    turn_left()
    turn_left()

def next_avenue():
    for i in range(4):
        move()


if __name__ == '__main__':
    run_karel_program()
