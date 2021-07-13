from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""

def main():
    while front_is_clear():
        put_beeper()
        move()
        move()
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
    put_beeper()

if __name__ == '__main__':
    run_karel_program('RampKarel1.w')
