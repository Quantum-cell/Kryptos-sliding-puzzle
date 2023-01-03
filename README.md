# Kryptos-sliding-puzzle
Looking at Kryptos passage 4 as a possible sliding puzzle

You may have noticed that Kryptos passage 4 has 98 characters, including the ? at the start. 98 has quite a surprisingly low amount of divisors: 1, 2, 7, 14, 49, 98. 
IF this passage was to belong in a grid, the options are limited to 1x98, 2x49, 7x14, 14x7, 49x2 and 98x1. 
I don't know about you, but I find 7 rows by 14 columns preferable.

When we do this, we have the first element being the ? in the top left-hand corner.
I wondered "What if this is some sort of sliding puzzle, and the ? is the blank space?"
Would there maybe be an intuitive set of movements, or a set of movements prescribed somewhere in the rest of Kryptos, that would solve the grid?

So here is the first of two Python programs I am working on.
You might see how it is similar to regular sliding puzzles where the blank space (?) is swapped with an adjacent tile.
