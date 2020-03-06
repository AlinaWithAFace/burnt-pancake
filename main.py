def pancake_problem(pancake_input):
    print(pancake_input)

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


def astar_flip_pancakes(pancake_stack):
    return pancake_stack


def bfs_flip_pancakes(pancake_stack):
    return pancake_stack


def flip_pancakes(pancake_stack, number_to_flip):
    pancakes_to_flip = pancake_stack[0:number_to_flip]
    pancakes_to_flip.reverse()
    flipped_pancakes = []

    for pancake in pancakes_to_flip:
        flipped_pancakes.append(flip_color(pancake))

    for i in range(number_to_flip):
        pancake_stack[i] = flipped_pancakes[i]

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


pancake_problem("1b2b3b4w-a")
