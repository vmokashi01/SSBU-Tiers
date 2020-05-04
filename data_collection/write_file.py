from frame_data import *

characters = get_chars()
acceleration = get_air_acc()
air_speed = get_air_spd()
fall_speed = get_fall_spd()
gravity = get_grav()
jump_height = get_jump_height()
jump_duration = get_jump_duration()
weight = get_weight()
landing = get_landing()
walk_speed = get_walk_spd()
dash_speed = get_dash_spd()
dash_turn = get_dash_turn()
ledge = get_ledge()
shield = get_shield()

tables = [['acceleration', acceleration], ['air_speed', air_speed], ['fall_speed', fall_speed], ['gravity', gravity], ['jump_height', jump_height], [
    'jump_duration', jump_duration], ['weight', weight], ['landing', landing], ['walk_speed', walk_speed], ['dash_speed', dash_speed], ['ledge', ledge], ['shield', shield]]


f = open('characters.csv', 'x')
for line in characters:
    f.write(line + "\n")


def table_to_file():
    for table in tables:
        f = open(table[0] + '.csv', 'x')
        for line in table[1]:
            for item in line:
                f.write(item + ';')
            f.write("\n")


table_to_file()
