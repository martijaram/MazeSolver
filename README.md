Hi, please read the following text to better understand the maze program.



# SECTION 1: Maze structure


For making your own maze file, set up a .txt

Then, set up your .txt as follows:

WIDTH
HEIGHT
...
MAZE (separated by spaces and visually 1s are walls and 0s are pathways)
...

- MAKE SURE THE FIRST AND LAST ROW ARE ALL FULL OF 1s AS WELL AS THE FIRST AND LAST COLUMN OF EVERY ROW -
The program is going to assume your first 0 and last 0 are the start and end.

___________________________
Here is an example of a maze file.txt:

4 # Width of maze <br>
6 # Height of maze <br>
1 1 1 1 # First row is full of 1s <br> 
1 0 1 1 # First and last column are all 1s <br> 
1 0 0 1 <br>
1 0 1 1 <br>
1 0 1 1 <br>
1 1 1 1 # Last row is full of 1s <br>

__________________________

As you can see, it can be very easy to set up a maze as it is very visually accessible to create one with 1s representing walls and 0s representing pathways.




# SECTION 2: Installing pygame

This program utilizes pygame for input and rendering purposes. 

___________________________
You can install pygame by inputting the following in your console:

> pip install pygame
___________________________

Make sure you have python3 installed. Otherwise the pip command is not going to work.




# SECTION 3: Personilization

Make sure to change the following files for better personification.

___________________________
To change the character:

Replace character.png with one of your choice
___________________________

To change the walls:

Replace wall.png with one of your choice
___________________________


# Tasks
- Implement the stack data structure using a linked list: DONE (see code)

- Implement the stack data structure using a partially-filled array: DONE (see code)

- Handle all the appropriate exception situations, such as a) undoing too many moves
(cannot return past the start of the maze), and b) pushing onto a full stack (not enough
bread crumbs to go forward!): DONE (Will see when playing the game)

- Create three images: one that represents a straight corridor, one that represents a left turn,
and one for a right turn. When the user chooses to go home, display on a window each of
these according to the appropriate path. DONE (Game itself is visual)

- Design an input file that describes some kind of simple maze. At any point in the maze,
limit the user’s options (forward, right, left) according to what the maze allows. DONE (Read above)

- In conjunction with the previous two, add some images: one for a dead end, one for a T-
junction, one for an intersection, and one that represents the goal (such as finding a
treasure). Set up the program to only show the choice ahead of the user according to the
maze you have created. DONE (Game itself is visual with limited view of player)



