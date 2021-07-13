# Q3: Cleanup Karel, Milestone 1

Your next task is to execute a "safe pickup" -- Karel can pick up beepers, but not if none are present! Write a program which will check if a beeper is present at the position Karel is currently on and pick up a beeper if one is present (if there are no beepers present, Karel shouldn't do anything).
Two worlds are provided for you to test your code on -- on the world where Karel starts on a beeper, your code should get Karel to pick the beeper up. On the world where Karel starts on a blank spot, your code shouldn't do anything.
We've provided you two 1x1 worlds (one with a beeper, one without) on which to test your code. You can toggle from the beeper-present world to the no-beeper world by changing the very last line in the file from
