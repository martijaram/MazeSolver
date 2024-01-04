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

4
6
1 1 1 1
1 0 1 1
1 0 0 1
1 0 1 1
1 0 1 1
1 1 1 1

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
___________________________
To change the walls:

Replace wall.png with one of your choice
___________________________


