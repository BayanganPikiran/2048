import random
import tkinter as tk
from constants import *
import numpy as np


class Board:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(("{}x{}".format(ROOT_WIDTH, ROOT_HEIGHT)))
        self.root.resizable(None, None)
        self.root.configure(background=PLAYFIELD_GRAY)
        self.root.title("2048")

        self.game_frame = self.create_game_frame()
        self.footer_frame = self.create_footer_frame()

    # ----------------------------- Frames ------------------------------- #
    def create_game_frame(self):
        game_frame = tk.Frame(self.root, width=PLAY_WIDTH, height=PLAY_HEIGHT, bg=PLAYFIELD_GRAY)
        game_frame.pack(anchor=tk.CENTER, expand=True)
        return game_frame

    def create_footer_frame(self):
        footer = tk.Frame(self.root, width=FOOTER_WIDTH, height=FOOTER_HEIGHT, bg=FOOTER_GRAY)
        footer.pack(anchor=tk.CENTER, expand=True)
        return footer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
