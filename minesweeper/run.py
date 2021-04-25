#!/usr/bin/env python3

# Standard Imports
from pprint import pprint

# Third Party Imports

# Custom Imports
from build_board import build_board

if __name__ == "__main__":
    # Get game details
    print("Please enter the board details.")
    r = input("How many rows:     ")
    c = input("How many columns:  ")
    m = input("How many mines:    ")
    print()
    print(f'W: {r}, H: {c}, M: {m}')
    board = build_board(int(r), int(c), int(m))
    pprint(board)
