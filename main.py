import heapq
import heapdict


class PancakeState:
    def __init__(self, stack, cost):
        self.parent = None  # type: PancakeState
        self.stack = stack
        self.cost = cost
        self.heuristic_cost = None
        self.flip_1_state = None  # type: PancakeState
        self.flip_2_state = None  # type: PancakeState
        self.flip_3_state = None  # type: PancakeState
        self.flip_4_state = None  # type: PancakeState

    def __repr__(self):
        # "Pancake: {}".format(self.stack)
        string = ''.join(self.stack)
        return string

    def __str__(self):
        # "Pancake: {}".format(self.stack)
        string = ''.join(self.stack)
        return string
        # string = "\nPancake: {}\n" \
        #          "  Cost: {}\n" \
        #          "  Children:\n" \
        #          "      {}\n" \
        #          "      {}\n" \
        #          "      {}\n" \
        #          "      {}\n".format(self.stack,
        #                              self.cost,
        #                              # self.parent,
        #                              self.flip_1_state,
        #                              self.flip_2_state,
        #                              self.flip_3_state,
        #                              self.flip_4_state)
        # "  Parent: {}\n" \
        # string = "Pancake: {}".format(self.stack)
        # string = "Pancake: {} | Cost: {}\n    {}\n    {}\n    {}\n    {}".format(self.stack, self.cost,
        #                                                                          self.flip_1_state,
        #                                                                          self.flip_2_state,
        #                                                                          self.flip_3_state,
        #                                                                          self.flip_4_state)

        # return string

    def print_winning_state_tree(self):
        string = ''.join(self.stack)
        temp = "{} cost: {}".format(string, self.cost)
        print(temp)
        if self.parent is not None:
            self.parent.print_winning_state_tree()

            # for state in winning_states:  # type: PancakeState
        #     print("\nwinning state step {}".format(state))
        #     if state.parent is not None:
        #         winning_states.append(state.parent)
        #
        # string = "\nPancake: {}\n" \
        #          "  Cost: {}\n" \
        #          "  Parent: {}\n" \
        #          "  Children:\n" \
        #          "      {}\n" \
        #          "      {}\n" \
        #          "      {}\n" \
        #          "      {}\n".format(self.stack,
        #                              self.cost,
        #                              self.parent,
        #                              self.flip_1_state,
        #                              self.flip_2_state,
        #                              self.flip_3_state,
        #                              self.flip_4_state)
        return None

    def build_state(self):
        # print("\n\n\nBuilding state for: {}".format(self.stack))
        # self.flip_1_state = PancakeState(None, -1)
        # self.flip_2_state = PancakeState(None, -1)
        # self.flip_3_state = PancakeState(None, -1)
        # self.flip_4_state = PancakeState(None, -1)

        flip_1_stack = self.stack[:]
        flip_2_stack = self.stack[:]
        flip_3_stack = self.stack[:]
        flip_4_stack = self.stack[:]

        self.flip_1_state = PancakeState(flip_pancakes(flip_1_stack, 1), self.cost + 1)
        self.flip_2_state = PancakeState(flip_pancakes(flip_2_stack, 2), self.cost + 2)
        self.flip_3_state = PancakeState(flip_pancakes(flip_3_stack, 3), self.cost + 3)
        self.flip_4_state = PancakeState(flip_pancakes(flip_4_stack, 4), self.cost + 4)

        self.flip_1_state.parent = self
        self.flip_2_state.parent = self
        self.flip_3_state.parent = self
        self.flip_4_state.parent = self

        # print(self.flip_1_state)
        # print(self.flip_2_state)
        # print(self.flip_3_state)
        # print(self.flip_4_state)
        # print("finished building: {}\n\n\n\n".format(self))

    # def __lt__(self, other):
    #     if other is not None:
    #         return self.cost < other.cost
    #     else:
    #         return self


def pancake_problem(pancake_input):
    pancake0 = pancake_input[0] + pancake_input[1]
    pancake1 = pancake_input[2] + pancake_input[3]
    pancake2 = pancake_input[4] + pancake_input[5]
    pancake3 = pancake_input[6] + pancake_input[7]

    pancake_stack = [pancake0, pancake1, pancake2, pancake3]

    # print("Read in pancakes: {}".format(pancake_stack))

    search_type = pancake_input[9]

    pancake_state = PancakeState(pancake_stack, 0)

    if search_type == "a":
        print("trying a* search...")
        astar_flip_pancakes(pancake_state)
    elif search_type == "b":
        print("trying breadth first search...")
        bfs_flip_pancakes(pancake_state)
    else:
        print("Invalid search type, received")
        print(search_type)

    print("ended up with {}".format(pancake_state.stack))
    return pancake_state.stack


def flip_color(pancake):
    pancake_weight = pancake[0]
    pancake_color = pancake[1]
    if pancake_color == "b":
        pancake_color = "w"
    elif pancake_color == "w":
        pancake_color = "b"

    pancake = pancake_weight + pancake_color
    return pancake


def flip_pancakes(pancake_stack, number_to_flip):
    number_to_flip - 1
    pancakes_to_flip = pancake_stack[0:number_to_flip]
    # print("going to flip: {}, {}".format(number_to_flip, pancakes_to_flip))
    pancakes_to_flip.reverse()

    flipped_pancakes = []

    for pancake in pancakes_to_flip:
        flipped_pancakes.append(flip_color(pancake))

    for i in range(number_to_flip):
        pancake_stack[i] = flipped_pancakes[i]

    # print("flipping {} complete! : {}".format(number_to_flip, pancake_stack))
    return pancake_stack


def perfect_stack(pancake_stack):
    perfect_pancake_1w = "1w"
    perfect_pancake_2w = "2w"
    perfect_pancake_3w = "3w"
    perfect_pancake_4w = "4w"

    perfect_pancake_stack = [perfect_pancake_1w, perfect_pancake_2w, perfect_pancake_3w, perfect_pancake_4w]
    if pancake_stack == perfect_pancake_stack:
        return True
    else:
        return False


def astar_flip_pancakes(pancake_state):
    # TODO
    return pancake_state


def bfs_flip_pancakes(pancake_state):
    print("starting bfs")
    pancake_states_to_build = [(pancake_state.cost, pancake_state)]  # fringe
    winning_state = None
    searched_state_count = 0

    for entry in pancake_states_to_build:  # type: tuple
        searched_state_count += 1
        # print("building out: {}".format(entry))
        state = entry[1]  # type: PancakeState

        state.build_state()
        if perfect_stack(state.stack):
            # print("Found a match!")
            winning_state = state
            break

        pancake_states_to_build.append((state.flip_1_state.cost, state.flip_1_state))
        pancake_states_to_build.append((state.flip_2_state.cost, state.flip_2_state))
        pancake_states_to_build.append((state.flip_3_state.cost, state.flip_3_state))
        pancake_states_to_build.append((state.flip_4_state.cost, state.flip_4_state))

    print("found solution after searching {} states".format(searched_state_count))
    winning_state.print_winning_state_tree()

    return winning_state


def tests():
    print("Starting tests!")
    test_pancake_1w = "1w"
    test_pancake_1b = "1b"
    test_pancake_2w = "2w"
    test_pancake_2b = "2b"
    test_pancake_3w = "3w"
    test_pancake_3b = "3b"
    test_pancake_4w = "4w"
    test_pancake_4b = "4b"

    test_stack_1w2w3w4w_1 = [test_pancake_1w, test_pancake_2w, test_pancake_3w, test_pancake_4w]
    test_stack_1w2w3w4w_2 = [test_pancake_1w, test_pancake_2w, test_pancake_3w, test_pancake_4w]
    test_stack_1w2w3w4w_3 = [test_pancake_1w, test_pancake_2w, test_pancake_3w, test_pancake_4w]
    test_stack_1w2w3w4w_4 = [test_pancake_1w, test_pancake_2w, test_pancake_3w, test_pancake_4w]

    assert flip_color(test_pancake_1w) == test_pancake_1b
    assert flip_pancakes(test_stack_1w2w3w4w_1, 1) == [test_pancake_1b, test_pancake_2w, test_pancake_3w,
                                                       test_pancake_4w]
    assert flip_pancakes(test_stack_1w2w3w4w_2, 2) == [test_pancake_2b, test_pancake_1b, test_pancake_3w,
                                                       test_pancake_4w]
    assert flip_pancakes(test_stack_1w2w3w4w_3, 3) == [test_pancake_3b, test_pancake_2b, test_pancake_1b,
                                                       test_pancake_4w]
    assert flip_pancakes(test_stack_1w2w3w4w_4, 4) == [test_pancake_4b, test_pancake_3b, test_pancake_2b,
                                                       test_pancake_1b]

    test_stack_state = [test_pancake_1w, test_pancake_2w, test_pancake_3w, test_pancake_4w]

    test_pancake_state = PancakeState(test_stack_state, 0)
    test_pancake_state.build_state()

    test_bfs_stack_0 = [test_pancake_1w, test_pancake_2w, test_pancake_3w, test_pancake_4w]
    test_bfs_state_0 = PancakeState(test_bfs_stack_0, 0)
    bfs_flip_pancakes(test_bfs_state_0)

    test_bfs_stack_1 = [test_pancake_4b, test_pancake_3b, test_pancake_2b, test_pancake_1b]
    test_bfs_state_1 = PancakeState(test_bfs_stack_1, 0)
    bfs_flip_pancakes(test_bfs_state_1)
    print("finished tests!")


pancake_problem("1b2b3b4w-b")

tests()
