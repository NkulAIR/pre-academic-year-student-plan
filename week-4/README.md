## ProblemSet4 : Libaries
### Emojize
It was very interesting learning about the different libraries in Python especially the emoji library which made emojize.py way simpler that what I imagined. My initial plan was parsing the string for the keyword using regex and somehow looking for the character associated with the term. This would have taken a whole lot of time to implement and the emoji library 


This week's problem set was interesting and a bit more challenging. I spent the most time on professor and game.py because one check50 test kept on failing.
### Professor
It seems like the program does not generate random numbers on level 1 (numbers from 0-9)
#### Update
Ended up rewriting the generate integer function to return a single number and called it twice in my main function, once for the first number of the sum and again for the other number. I then came across this problem
#### New problem & Solution
The score count was inaccurate and the program stopped after the user gets the same sum wrong after three tries
I wrote another variable to reset the tries to 0 after 3 tries (the while loop) and instead of using break to stop the program. 
I'm proud of myself for being able to debug that with one line