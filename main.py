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

        self.score_label = self.create_score_label()
        self.hi_score_label = self.create_hi_score_label()
        self.restart_btn = self.create_restart_btn()

        self.board_matrix = self.create_board_matrix()

    # ----------------------------- Frames ------------------------------- #
    def create_game_frame(self):
        game_frame = tk.Frame(self.root, width=PLAY_WIDTH, height=PLAY_HEIGHT, bg=PLAYFIELD_GRAY)
        game_frame.pack(anchor=tk.CENTER, expand=True)
        return game_frame

    def create_footer_frame(self):
        footer = tk.Frame(self.root, width=FOOTER_WIDTH, height=FOOTER_HEIGHT, bg=FOOTER_GRAY)
        footer.pack(anchor=tk.CENTER, expand=True)
        return footer

    # ------------------------- Labels & Buttons -------------------------- #

    def create_score_label(self):
        score_label = tk.Label(self.footer_frame, text="Score: 2", width=32, height=1, font=LABEL_FONT)
        score_label.grid(row=0, column=0, sticky=tk.W, padx=4, ipady=6, pady=3)
        return score_label

    def create_hi_score_label(self):
        hi_score_label = tk.Label(self.footer_frame, text="High Score: 1", width=32, height=1, font=LABEL_FONT)
        hi_score_label.grid(row=1, column=0, sticky=tk.W, padx=4, ipady=6, pady=3)
        return hi_score_label

    def create_restart_btn(self):
        restart_btn = tk.Button(self.footer_frame, text="Restart", width=5, height=1, font=LABEL_FONT)
        restart_btn.grid(row=0, column=1, rowspan=2, sticky=tk.E, padx=3, pady=2, ipadx=6, ipady=12)
        return restart_btn

    # ------------------------ Matrix Values & Cells ------------------------- #
    def create_board_matrix(self):
        matrix = [[0 for j in range(4)] for i in range(4)]
        print(f"The starting matrix is: {matrix}")
        return matrix


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
