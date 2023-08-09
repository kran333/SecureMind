class Maze_maker():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar_alog(maze, start, end):
    start_Maze_maker = Maze_maker(None, start)
    start_Maze_maker.g = start_Maze_maker.h = start_Maze_maker.f = 0
    end_Maze_maker = Maze_maker(None, end)
    end_Maze_maker.g = end_Maze_maker.h = end_Maze_maker.f = 0
    open_list = []
    closed_list = []
    open_list.append(start_Maze_maker)
    while len(open_list) > 0:
        current_Maze_maker = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_Maze_maker.f:
                current_Maze_maker = item
                current_index = index
        open_list.pop(current_index)
        closed_list.append(current_Maze_maker)
        if current_Maze_maker == end_Maze_maker:
            path = []
            current = current_Maze_maker
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            Maze_maker_position = (current_Maze_maker.position[0] + new_position[0], current_Maze_maker.position[1] + new_position[1])
            if Maze_maker_position[0] > (len(maze) - 1) or Maze_maker_position[0] < 0 or Maze_maker_position[1] > (
                    len(maze[len(maze) - 1]) - 1) or Maze_maker_position[1] < 0:
                continue
            if maze[Maze_maker_position[0]][Maze_maker_position[1]] != 0:
                continue
            new_Maze_maker = Maze_maker(current_Maze_maker, Maze_maker_position)
            children.append(new_Maze_maker)
        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            child.g = current_Maze_maker.g + 1
            child.h = ((child.position[0] - end_Maze_maker.position[0]) ** 2) + (
                        (child.position[1] - end_Maze_maker.position[1]) ** 2)
            child.f = child.g + child.h
            for open_Maze_maker in open_list:
                if child == open_Maze_maker and child.g > open_Maze_maker.g:
                    continue
            open_list.append(child)

def mainControll():
    maze = [[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 0, 0]]
    start = (0, 0)
    end = (7, 6)
    path = astar_alog(maze, start, end)
    print(path)


mainControll()