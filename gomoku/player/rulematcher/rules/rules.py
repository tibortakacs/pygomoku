# Collection of rules descriptors
#
# o - player
# x - enemy
# - - empty field
#

cell_x = "x"
cell_o = "o"
cell_e = "-"
cell_X = "X"

rules = [
    (100, 1, "xxxxx"), # Win the game with five

    (95, 1, "xoooo"), # Block enemy's five
    (95, 1, "oxooo"),
    (95, 1, "ooxoo"),

    (90, 1, "-xxxx-"), # Create free four

    (85, 1, "-xooo-"), # Block enemy's free three
    (85, 2, "--ooox"),
    (85, 1, "-oxoo-"),
    (85, 2, "-o-oox"),
    (85, 3, "xo-oo-"),

    (80, 1, "--xxx-"), # Create free tree
    (80, 2, "-x-xx-"),

    (75, 1, "xxxxo"), # Create closed four
    (75, 2, "x-xxxo"),
    (75, 2, "xx-xxo"),

    (70, 1, "xooox-"), # Block enemy's closed three
    (70, 2, "xooxo-"),
    (70, 2, "xoo-ox"),

    (65, 1, "xx---"), # Form potential two
    (65, 1, "-xx--"),
    (65, 2, "x-x--"),
    (65, 2, "-x-x-"),
    (65, 3, "x--x-"),

    (60, 1, "xx"), # Just put close
    (60, 1, "x-x"),

    (55, 1, "xo"), # Just block the enemy

    (0, 1, "x") # Basic step
]