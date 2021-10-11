from karel.stanfordkarel import *

"""
File: DoYourThing.py
----------------------------
Karel shows the world some moves.
"""

def main():
    turn_left()
    move()
    function_a()
    move()
    turn_left()
    move()
    function_a()
    move()
    while front_is_blocked():
        turn_left()
        move()
        function_a()
        move()
    put_beeper()
    move()
    function_a()
    move()
    turn_left()
    move()
    function_a()
    move()
    turn_left()
    while front_is_clear():
        move()
        function_a()
        move()
        turn_left()

def function_a():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
