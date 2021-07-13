# Q4: Cleanup Karel, Milestone 2

Karel has a bit of spring cleaning to do! Karel's world will have beepers in some positions in the bottom row; write a program to have Karel walk across the bottom row and, at each position, pick up a beeper only if one is present. Notice that you've already written the code to check if a beeper is present and only pick up a beeper if one is there from the previous milestone -- you should use your code from the previous milestone as a helper function to help with the decomposition of this problem!
Additionally, note that Karel's starting position will never contain a beeper, so there's no need to check it.
For example, if this is the initial starting world, with some beepers in the first row:

<p align="center">
  <img width="500" src="https://static.us.edusercontent.com/files/wrFTLPTbItmNInxXGsu6vf6Z" alt="Material Bread logo">
</p>

This should be the end result, with a clear bottom row:

<p align="center">
  <img width="500" src="https://static.us.edusercontent.com/files/pR9y61NWe7bH7kJ5QaaIlOhn" alt="Material Bread logo">
</p>

We've provided you two worlds on which to test your code. You can toggle between them by changing the very last line in the file from:

`run_karel_program('Cleanup1.w')`

to

`run_karel_program('Cleanup2.w')`

(and vice versa) -- you will likely need to press Run (it's fine if you do so without any code written) for the world change to take effect.


