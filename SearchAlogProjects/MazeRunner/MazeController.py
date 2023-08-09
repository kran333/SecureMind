import queue

class ControlMaze:
    def __init__(self, maze):
        self.maze = maze
        self.nums = queue.Queue()
        self.stack = []
        self.nums.put("")
        self.add = ""
        self.visited = []
        self.temp = []
        self.control_options = ['U', 'D', 'L', 'R']

    def check_path(self, moves):
        for x, pos in enumerate(self.maze[0]):
            if pos == "S":
                start = x
        i = start
        j = 0
        for move in moves:
            if move == "L":
                i -= 1
            elif move == "R":
                i += 1
            elif move == "U":
                j -= 1
            elif move == "D":
                j += 1
            if not (0 <= i < len(self.maze[0]) and 0 <= j < len(self.maze)):
                return False
            elif (self.maze[j][i] == "#"):
                return False
        return True

    def get_end_point(self, moves):
        for index, position in enumerate(self.maze[0]):
            if position == "S":
                start = index
        i = start
        j = 0
        for move in moves:
            if move == "L":
                i -= 1
            elif move == "R":
                i += 1
            elif move == "U":
                j -= 1
            elif move == "D":
                j += 1
        if self.maze[j][i] == "E":
            print("Path Found: " + moves)
            self.print_maze_found_path(moves)
            return True
        return False

    def print_maze_found_path(self, path=""):
        for index, position in enumerate(self.maze[0]):
            if position == "S":
                start = index
        i = start
        j = 0
        pos = set()
        for move in path:
            if move == "L":
                i -= 1
            elif move == "R":
                i += 1
            elif move == "U":
                j -= 1
            elif move == "D":
                j += 1
            pos.add((j, i))
        for j, row in enumerate(self.maze):
            for i, col in enumerate(row):
                if (j, i) in pos:
                    print(". ", end="")
                else:
                    print(col + " ", end="")
            print()

    def do_bfs_search(self):
        while not self.get_end_point(self.add):
            self.add = self.nums.get()
            print("Next possible Path: ", self.add)
            # print("nums: ", self.nums.get())
            for control in self.control_options:
                # print("step 4")
                put = self.add + control
                if self.check_path(put):
                    # print("step 5")
                    self.nums.put(put)