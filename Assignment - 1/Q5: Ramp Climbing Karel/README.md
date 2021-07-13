# Q5: Ramp Climbing Karel

Write a program that has Karel draw a diagonal line across the world, with a slope of ½, like so:

<p align="center">
  <img width="600" src="https://static.us.edusercontent.com/files/19era4m85IbSZmbhWQPzhwVP" alt="Material Bread logo">
</p>

The key to drawing a diagonal line with slope ½ is to move two steps forward and one step up between each beeper. In this problem you can and should assume that the world is an odd number of columns across. Solving the problem for even columns as well is much harder and would count as an "extension".

You should assume
- Karel always begins at the bottom left corner of and empty world facing East.
- You may assume that the world is an odd number of columns across
- Karel's bag has infinite beepers.
- It does not matter which direction Karel ends up facing.
- The world is always square (the world's height is the same as its width)

We've provided you three worlds on which to test your code. You can toggle between them by changing the very last line in the file from:

`run_karel_program('RampKarel1.w')`

to

`run_karel_program('RampKarel2.w')`

or

`run_karel_program('RampKarel3.w)`

you will likely need to press Run (it's fine if you do so without any code written) for the world change to take effect. RampKarel1 is a 7x7 world, RampKarel2 is a 3x3 world, and RampKarel3 is a 25x25 world.
