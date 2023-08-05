# Measurements

TILE_LENGTH = 33

# Playfield
NUM_CELLS = 4

NUM_TILE_IN_ROWS = 4
NUM_TILE_IN_COLS = 4

CELL_WIDTH = TILE_LENGTH * NUM_TILE_IN_COLS
CELL_HEIGHT = TILE_LENGTH * NUM_TILE_IN_ROWS

PLAY_WIDTH = CELL_WIDTH * NUM_CELLS
PLAY_HEIGHT = CELL_HEIGHT * NUM_CELLS

# Footer
NUM_FOOTER_ROWS = 2

FOOTER_WIDTH = PLAY_WIDTH
FOOTER_HEIGHT = TILE_LENGTH * NUM_FOOTER_ROWS

# Root

ROOT_WIDTH = PLAY_WIDTH
ROOT_HEIGHT = PLAY_HEIGHT + FOOTER_HEIGHT

# Canvas

CANVAS_WIDTH = ROOT_WIDTH
CANVAS_HEIGHT = ROOT_HEIGHT

# Colors
PLAYFIELD_GRAY = "#DDE6ED"
FOOTER_GRAY = "#DBDFEA"
CELL_LT_BLUE = "#ECF9FF"



LABEL_FONT = ('Helvetica', 16, "bold")
BUTTON_FONT = ('Helvetica', 14, "bold")