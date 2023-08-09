# defining a class for Maze
class Maze:
    # Intilizing the file name
    def __init__(self, maze_file):
        self.maze_file = maze_file

    def get_maze_data(self):
        maze_data = []
        f = open(self.maze_file)
        lines = f.readlines()
        for line in lines:
            x = (line.replace('\n', '')).split(',')
            maze_data.append(x)
        return maze_data