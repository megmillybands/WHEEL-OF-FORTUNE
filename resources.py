# from dataclasses import dataclass
import random

def spin_the_wheel() -> int:
    result = random.choice(wheel)
    return result

def find_all_occurrences(random_puzzle, letter) -> list:
    indices = []
    start_index = 0
    while True:
        found_index = random_puzzle[0].find(letter, start_index)
        if found_index == -1:
            break
        indices.append(found_index)
        start_index = found_index + len(letter)
    return indices

def flip_letters(random_puzzle: tuple[str, str], letter: str, indices: list) -> tuple:
    for i in indices:
        ...

wheel = [
    800,
    350,
    450,
    5000,
    300,
    600,
    700,
    600,
    500,
    300,
    500,
    800,
    550,
    300,
    900,
    500,
    300,
    900,
    350,
    600,
    400,
    300,
]

around_the_house = [
    ("BATHROOM MIRROR", "-------- ------"),
    ("BUNK BEDS", "---- ----"),
    ("CLAWFOOT BATHTUB", "-------- --------"),
    ("DECORATIVE AREA RUGS", "---------- ---- ----"),
    ("LAUNDRY BASKET", "------- ------"),
]

fictional_characters = [
    ("AQUAMAN", "-------"),
    ("CLIFFORD THE BIG RED DOG", "-------- --- --- --- ---"),
    ("DOCTOR DOLITTLE", "------ --------"),
    ("ELMER FUDD", "----- ----"),
    ("FROSTY THE SNOWMAN", "------ --- -------"),
]

food_and_drink = [
    ("AN ASSORTMENT OF COLORFUL HARD CANDY", "-- ---------- -- -------- ---- -----"),
    ("AUTHENTIC ITALIAN MEATBALLS", "--------- ------- ---------"),
    ("BEEF TENDERLOIN WITH MASHED POTATOES", "---- ---------- ---- ------ --------"),
    ("BUTTERED BISCUITS", "-------- --------"),
    ("CARAFE OF WINE", "------ -- ----"),
]

phrases = [
    ("ADDING INSULT TO INJURY", "------ ------ -- ------"),
    ("AS YOU WISH", "-- --- ----"),
    ("BITE YOUR TONGUE", "---- ---- ------"),
    ("CASE CLOSED", "---- ------"),
    ("DRAWING A BLANK", "------- - -----"),
]

puzzles = [around_the_house, fictional_characters, food_and_drink, phrases]

consonants = [
    "B",
    "C",
    "D",
    "F",
    "G",
    "H",
    "J",
    "K",
    "L",
    "M",
    "N",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

vowels = ["A", "E", "I", "O", "U"]

# @dataclass
# class Player:
#     name: str
#     money: int

player = []