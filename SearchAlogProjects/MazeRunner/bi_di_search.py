import queue

class ControlMaze:
    def __init__(self, maze):
        self.maze = maze
        self.f_nums = queue.Queue()
        self.b_nums = queue.Queue()
        self.f_nums.put("")
        self.b_nums.put("")
        self.f_add = ""
        self.b_add = ""
        self.start = 'S'
        self.start_ind = []
        self.end = 'E'
        self.end_ind = []
        self.control_options = ['U', 'D', 'L', 'R']
        self.track_all_farward_pos = []
        self.track_path_farward_pos = []
        self.track_all_backward_pos = []
        self.track_path_backward_pos = []
        self.current_forward_search_pos = []
        self.current_backward_search_pos = []
        self.final_path_cods = []
        self.final_f_b_cods = {}
        self.f = open("output.txt", 'w')

    def check_forward_path(self, moves, i, j):
        self.current_forward_search_pos = []
        self.track_all_farward_pos.append([i, j])
        self.current_forward_search_pos.append([i, j])
        for move in moves:
            if move == "L":
                i -= 1
                self.track_all_farward_pos.append([i, j])
                self.current_forward_search_pos.append([i, j])
            elif move == "R":
                i += 1
                self.track_all_farward_pos.append([i, j])
                self.current_forward_search_pos.append([i, j])
            elif move == "U":
                j -= 1
                self.track_all_farward_pos.append([i, j])
                self.current_forward_search_pos.append([i, j])
            elif move == "D":
                j += 1
                self.track_all_farward_pos.append([i, j])
                self.current_forward_search_pos.append([i, j])
            if not (0 <= i < len(self.maze[0]) and 0 <= j < len(self.maze)):
                return False
            elif (self.maze[j][i] == "#"):
                return False
        return True

    def check_backward_path(self, moves, i, j):
        self.current_backward_search_pos = []
        self.track_all_backward_pos.append([i, j])
        self.current_backward_search_pos.append([i, j])

        for move in moves:
            if move == "L":
                i -= 1
                self.track_all_backward_pos.append([i, j])
                self.current_backward_search_pos.append([i, j])
            elif move == "R":
                i += 1
                self.track_all_backward_pos.append([i, j])
                self.current_backward_search_pos.append([i, j])
            elif move == "U":
                j -= 1
                self.track_all_backward_pos.append([i, j])
                self.current_backward_search_pos.append([i, j])
            elif move == "D":
                j += 1
                self.track_all_backward_pos.append([i, j])
                self.current_backward_search_pos.append([i, j])
            if not (0 <= i < len(self.maze[0]) and 0 <= j < len(self.maze)):
                return False
            elif (self.maze[j][i] == "#"):
                return False
        return True

    def get_start_end_pos(self):
        for index, position in enumerate(self.maze[0]):
            if position == self.start:
                self.start_ind.append([index, 0])
        for index, position in enumerate(self.maze[-1]):
            if position == self.end:
                self.end_ind.append([index, len(self.maze)-1])
        print(self.start_ind)
        print(self.end_ind)


    def check_end_point(self, current_pos):
        if len(current_pos) == 0:
            return False
        if ((current_pos[-1][0] == self.end_ind[0][0]) and (current_pos[-1][1] == self.end_ind[0][1])):
            return True
        else:
            return False

    def check_meeting_point(self, f_path, b_path):
        if len(f_path) <= 0 or len(b_path) <= 0:
            return False
        else:
            if f_path[-1] == b_path[-1]:
                f_temp = []
                b_temp = []
                for x in f_path:
                    if x in self.final_path_cods:
                        continue
                    else:
                        self.final_path_cods.append(x)
                        f_temp.append(x)
                self.final_f_b_cods['f'] = f_temp

                b_path.reverse()
                for x in b_path:
                    if x in self.final_path_cods:
                        continue
                    else:
                        self.final_path_cods.append(x)
                        b_temp.append(x)
                self.final_f_b_cods['b'] = b_temp
                print("************* Two paths met *************")
                print("Meeting point at ", f_path[-1])
                print("The final path codinates are is :", self.final_path_cods)
                self.f.write("************* Two paths met *************\n")
                self.f.write("Meeting point at {}\n".format(f_path[-1]))
                self.f.write("The final path codinates are is : {}\n".format(self.final_path_cods))
                return True
            else:
                return False



    def print_maze_found_path(self, path_cods = {}):
        for vale in self.maze:
            for x in vale:
                print(x + "  ", end="")
                self.f.write(x + "  ")
            print()
            self.f.write('\n')
        print("------------------------------------")
        self.f.write("------------------------------------\n")
        temp_maze = self.maze
        for x in path_cods['f']:
            temp_maze[x[1]][x[0]] = '.'
        for x in path_cods['b']:
            temp_maze[x[1]][x[0]] = '+'
        for vale in temp_maze:
            for x in vale:
                print(x + "  ", end="")
                self.f.write(x + "  ")
            print()
            self.f.write('\n')
        print("------------------------------------")
        print("'.' represents the forward search")
        print("'+' represents the Backward search")
        self.f.write("------------------------------------\n")
        self.f.write("'.' represents the forward search\n")
        self.f.write("'+' represents the Backward search\n")



    def do_bfs_search(self, start_ind_i, start_ind_j, direction = 'forward'):
        if direction == 'forward':
            self.f_add = self.f_nums.get()
            for control in self.control_options:
                put = self.f_add + control
                if self.check_forward_path(put, start_ind_i, start_ind_j):
                    print("Next possible Forward Path: ", put)
                    self.f.write("Next possible Forward Path: {}\n".format(put))
                    self.f_nums.put(put)
        else:
            self.b_add = self.b_nums.get()
            for control in self.control_options:
                put = self.b_add + control
                if self.check_backward_path(put, start_ind_i, start_ind_j):
                    print("Next possible Backward Path: ", put)
                    self.f.write("Next possible Backward Path: {}\n".format(put))
                    self.b_nums.put(put)


    def do_bi_directional_search(self):
        while not self.check_meeting_point(self.current_forward_search_pos, self.current_backward_search_pos):
            self.do_bfs_search(self.start_ind[0][0], self.start_ind[0][1], 'forward')
            self.do_bfs_search(self.end_ind[0][0], self.end_ind[0][1], 'backward')

        self.print_maze_found_path(self.final_f_b_cods)

