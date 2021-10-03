from assets import *
from random import sample, choice, randint
from os import system, name
from time import sleep
import math

try:
    import keyboard
except ModuleNotFoundError:
    print("Please wait while the keyboard module installs.\n")
    system('py -m pip install keyboard')
    import keyboard

NUM_COLS = NUM_ROWS = 5


class Boat:
    """The variable surrounding the player."""
    def __init__(self, x, y, number_of_fish,
                 number_of_moves=0, turns_till_fish_loss=2):
        self.y, self.x = y, x
        self.number_of_fish = number_of_fish
        self.number_of_moves = number_of_moves
        self.TURNS_TILL_FISH_LOSS = turns_till_fish_loss
        self.won = False


def print_board_compass(board, compass):
    """Print the tiled board with the chosen compass 1 tile row at a time

    Args:
        board (list[list[str]]): A 2D array that represents the board
        compass (str): The compass that points to the island
    """
    number_of_lines = 0
    tiles = {' ': BlankTile.TILE, 'f': FishTile.TILE,
             's': StormTile.TILE, 'n': NorthIsland.TILE, 'b': BoatTile.TILE}

    for row in board:
        for pretty_row in zip(*(tiles[tile] for tile in row)):
            print(*pretty_row, compass[min(number_of_lines, len(compass) - 1)])
            number_of_lines += 1


def pretty_print_board():
    """Takes a board from an array of letters and prints a grid of tiles"""
    print(f"You have {math.ceil(maui.number_of_fish)} fish left.")
    Δy, Δx = y - maui.y, x - maui.x

    chosen_compass = Compass.angle_to_compass(math.atan2(Δy, Δx)).splitlines()

    temp_board = [row[:] for row in board]

    island_on_board = (maui.x - NUM_COLS//2 <= x <= maui.x + NUM_COLS//2 and
                       maui.y - NUM_ROWS//2 <= y <= maui.y + NUM_ROWS//2)

    if island_on_board:
        temp_board[NUM_ROWS//2 - Δy][NUM_COLS//2 + Δx] = 'n'

    print_board_compass(temp_board, chosen_compass)


def add_tile(tile_type, number_to_place):
    """Adds the specified tile to the map in a location that is blank

    Args:
        tile_type (string): The type of tile to add
        number_to_place (int): The number of tiles to add to the board
    """
    # Put fish tiles on the board
    type_left_to_place = number_to_place

    while type_left_to_place:
        # Get random square
        selected_row = randint(0, NUM_ROWS - 1)
        selected_column = randint(0, NUM_COLS - 1)

        if board[selected_row][selected_column] == ' ':
            board[selected_row][selected_column] = tile_type
            type_left_to_place -= 1


def new_board(n_fish=3, n_storms=10, boat_coords=(NUM_ROWS//2, NUM_COLS//2)):
    """Create a new random board with the boat at the chosen coords"""
    global board
    # Replace the board with a blank one
    board = [[' ' for col in range(NUM_COLS)] for row in range(NUM_ROWS)]

    boat_row, boat_col = boat_coords
    board[boat_row][boat_col] = 'b'

    # Add fish to the board
    add_tile('f', n_fish)

    # Add storms to the board
    add_tile('s', n_storms)

    pretty_print_board()


def move(key_press):
    """Move the boat accourding to key press

    Args:
        key_press (str): The key pressed
    """
    key = str(key_press)[14:-6].lower()
    if key not in VALID_KEYS or maui.number_of_fish <= 0 or maui.won:
        return None
    system("cls" if name == "nt" else "clear")

    # Record the value of the moved to square and place the there
    tile, board[NUM_ROWS//2][NUM_COLS//2] = move_boat(key), 'b'

    TILE_EFFECTS = {'f': FishTile.move_onto, 's': StormTile.move_onto,
                    ' ': BlankTile.move_onto, 'n': NorthIsland.move_onto}
    TILE_EFFECTS[tile](maui, add_tile)

    pretty_print_board()

    maui.won = (maui.x, maui.y) == (x, y)


def move_boat(key):
    """Run the function associated with each keypress

    Returns:
        str: The value of the moved to square
    """
    board[NUM_ROWS//2][NUM_COLS//2] = ' '
    if key in {'w', 'up'}:
        maui.y += 1
        board.insert(0, sample(board.pop(NUM_ROWS - 1), NUM_ROWS))

    elif key in {'s', 'down'}:
        maui.y -= 1
        board.insert(NUM_ROWS, sample(board.pop(0), NUM_ROWS))

    elif key in {'a', 'left'}:
        maui.x -= 1
        shuffle_move_col(NUM_COLS - 1, 0)

    elif key in {'d', 'right'}:
        maui.x += 1
        shuffle_move_col(0, NUM_COLS - 1)
    elif key == 'h':
        print(Text.rules)

    maui.number_of_fish -= 1 / maui.TURNS_TILL_FISH_LOSS

    return board[NUM_ROWS//2][NUM_COLS//2]


def shuffle_move_col(index, new_index):
    """Shuffle a coloumn and then move it from the index to the new index"""
    for row in board:
        n = randint(0, 3)
        # Shuffle the coloumns
        row[index], board[n][index] = board[n][index], row[index]
        # Move to the specified index
        row.insert(new_index, row.pop(index))


if __name__ == '__main__':
    VALID_KEYS = {'w', 'up', 'a', 'left', 's', 'down', 'd', 'right', 'h'}

    try_again = 'yes'
    print(Text.rules)
    input("Press Enter to Start the game")
    while try_again in {'y', 'yes'}:
        system("cls" if name == "nt" else "clear")

        radius_of_circle = randint(35, 40)
        x = randint(0, radius_of_circle) * choice((-1, 1))
        y = (radius_of_circle - abs(x)) * choice((-1, 1))

        maui = Boat(0, 0, 2000)

        # Create the board and then print it.
        new_board()

        keybind = keyboard.on_press(move)

        while maui.number_of_fish > 0 and not maui.won:
            sleep(0)
        keybind()

        system("cls" if name == "nt" else "clear")
        print(End.VICTORY if maui.won else End.DEATH)
        try_again = input('Try again (Y|N)').lower()
