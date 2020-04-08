def pancake_problem(pancake_input):
    tests()

    pancake0 = pancake_input[0] + pancake_input[1]
    pancake1 = pancake_input[2] + pancake_input[3]
    pancake2 = pancake_input[4] + pancake_input[5]
    pancake3 = pancake_input[6] + pancake_input[7]

    pancake_stack = [pancake0, pancake1, pancake2, pancake3]

    print("Read in pancakes: ")
    print(pancake_stack)

    search_type = pancake_input[9]

    if search_type == "a":
        print("trying a* search...")
        astar_flip_pancakes(pancake_stack)
    elif search_type == "b":
        print("trying breadth first search...")
        bfs_flip_pancakes(pancake_stack)
    else:
        print("Invalid search type, received")
        print(search_type)

    print(pancake_stack)
    return pancake_stack


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
    print("going to flip: {}".format(pancakes_to_flip))
    pancakes_to_flip.reverse()

    flipped_pancakes = []

    for pancake in pancakes_to_flip:
        flipped_pancakes.append(flip_color(pancake))

    for i in range(number_to_flip):
        pancake_stack[i] = flipped_pancakes[i]

    print("flipping {} complete! : {}".format(number_to_flip, pancake_stack))
    return pancake_stack


def astar_flip_pancakes(pancake_stack):
    return pancake_stack


def bfs_flip_pancakes(pancake_stack):
    return pancake_stack


def tests():
    test_pancake_1w = "1w"
    test_pancake_1b = "1b"
    test_pancake_2w = "2w"
    test_pancake_2b = "2b"
    test_pancake_3w = "3w"
    test_pancake_3b = "3b"
    test_pancake_4w = "4w"
    test_pancake_4b = "4b"

    test_stack_1_1w2w3w4w = [test_pancake_1w, test_pancake_2w, test_pancake_3w, test_pancake_4w]
    test_stack_2_1w2w3w4w = [test_pancake_1w, test_pancake_2w, test_pancake_3w, test_pancake_4w]
    test_stack_3_1w2w3w4w = [test_pancake_1w, test_pancake_2w, test_pancake_3w, test_pancake_4w]
    test_stack_4_1w2w3w4w = [test_pancake_1w, test_pancake_2w, test_pancake_3w, test_pancake_4w]

    assert flip_color(test_pancake_1w) == test_pancake_1b
    assert flip_pancakes(test_stack_1_1w2w3w4w, 1) == [test_pancake_1b, test_pancake_2w, test_pancake_3w,
                                                       test_pancake_4w]
    assert flip_pancakes(test_stack_2_1w2w3w4w, 2) == [test_pancake_2b, test_pancake_1b, test_pancake_3w,
                                                       test_pancake_4w]
    assert flip_pancakes(test_stack_3_1w2w3w4w, 3) == [test_pancake_3b, test_pancake_2b, test_pancake_1b,
                                                       test_pancake_4w]
    assert flip_pancakes(test_stack_4_1w2w3w4w, 4) == [test_pancake_4b, test_pancake_3b, test_pancake_2b,
                                                       test_pancake_1b]


pancake_problem("1b2b3b4w-a")
