from Maze import Maze
# from MazeController import ControlMaze
# # from testController import ControlMaze
from bi_di_search import ControlMaze


# file_name = "temp_maze1.txt"
# file_name = "maze1.txt"
file_name = "Maze2.txt"


maze_obj = Maze(file_name)
maze = maze_obj.get_maze_data()
maze_control_obj = ControlMaze(maze)

maze_control_obj.get_start_end_pos()
maze_control_obj.do_bi_directional_search()
