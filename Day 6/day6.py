# @author   Lucas Cardoso de Medeiros
# @since    09/06/2022
# @version  1.0

# Reeborg's World challenge


def turn_rigth():
    for i in range(3):
        turn_left()


def jump():
    turn_left()
    for i in range(2):
        move()
        turn_rigth()
    move()
    turn_left()


# Hurdle 1:
def hurdle1():
    for i in range(6):
        move()
        jump()


# Hurdle 2:
def hurdle2():
    while not at_goal():
        move()
        jump()


# Hurdle 3:
def hurdle3():
    while not at_goal():
        if wall_in_front():
            jump()
        else:
            move()


# Hurdle 4:
def jump4():
    turn_left()
    while not right_is_clear():
        move()
    turn_rigth()
    move()
    turn_rigth()
    while not wall_in_front():
        move()
    turn_left()


def hurdle4():
    while not at_goal():
        if wall_in_front():
            jump4()
        else:
            move()


def escape():
    while not is_facing_north():
        turn_left()
    turn_rigth()
    while front_is_clear():
        move()
    turn_left()
    while not at_goal():
        if right_is_clear():
            turn_rigth()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()


escape()
