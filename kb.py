import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.encoder import RotaryioEncoder
from kmk.scanners.keypad import MatrixScanner


class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        super().__init__()

        self.col_pins = [board.GP28, board.GP26, board.GP21, board.GP18, board.GP17]
        self.row_pins = [board.GP27, board.GP22, board.GP20, board.GP19, board.GP6]
        self.diode_orientation = DiodeOrientation.COL2ROW

        self.coord_mapping = [
            0,  1,  2,  3,  4,
            5,  6,  7,  8,  9,
            10, 11, 12, 13, 14,
            15, 16, 17, 18, 19,
            24, 25, 26# this three key for rotaryioencoder
            ]

        self.matrix = [
            MatrixScanner(
                column_pins=self.col_pins,
                row_pins=self.row_pins,
                columns_to_anodes=self.diode_orientation
                ),
            RotaryioEncoder(
                pin_a=board.GP8,
                pin_b=board.GP9
                ),
            ]
