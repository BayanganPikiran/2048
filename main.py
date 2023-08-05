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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
