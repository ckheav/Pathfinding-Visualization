# Pathfinding Visualization
A pathfinding visualizer created in python, which uses A* search algorithm to find the shortest path from the start and end nodes location. Once the start and end nodes are chosen, the user is allowed to create walls between the start and end nodes. 

# Instructions
To use the visualizer, download the files and make sure the pygame library is installed. Once everything is clear run the "pathfinding main.py". Once the GUI has appear with the left mouse button choose the position of the start and end nodes. Then, you can create walls between the nodes by pressing and holding left mouse button and basically drawing walls around the entire grid. If you messed up or do not like certain walls you can click or hold the right mouse button to erase the unwanted wall. Otherwise, you can press the R key on your keyboard to reset the grid or press the spacebar to start the A* search algorithm. 
Keys:
- Left mouse button: chooses the start and end nodes positions, then creates walls.
- Right mouse button: deletes any node
- R key: resets the grid
- Spacebar: starts the algorithm (when both start and end node are chosen)

# Requirements
- Python 3.7.6 or up
- pygame

# Future improvements:
- Adding recursive backtracking algorithm to generate a maze of walls in between the start and end nodes
