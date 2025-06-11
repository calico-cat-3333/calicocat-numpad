# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid green
background, a smaller purple rectangle, and some yellow text.
"""

import board
import busio
import digitalio
import displayio
import terminalio
from fourwire import FourWire
from adafruit_display_text import label

from adafruit_st7789 import ST7789

# Release any resources currently in use for the displays
displayio.release_displays()

spi = busio.SPI(clock=board.GP14, MOSI=board.GP15)
tft_cs = board.GP13
tft_dc = board.GP10
tft_rst = board.GP11
tft_bl = board.GP7

bl = digitalio.DigitalInOut(tft_bl)
bl.direction = digitalio.Direction.OUTPUT
bl.value = False

display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.GP11)

# display = ST7789(display_bus, width=76, height=284, rowstart=18, colstart=82, rotation=180, invert=False)
display = ST7789(display_bus, width=284, height=76, rowstart=17, colstart=82, rotation=90, invert=False)
# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(284, 284, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00  # Bright Green

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=1)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(284, 75, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xAA0088  # Purple
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=1, y=0)
splash.append(inner_sprite)

text_area = label.Label(
    terminalio.FONT,
    text="Hello World!",
    color=0xFFFF00,
    scale=2,
    anchor_point=(0.5, 0.5),
    anchored_position=(display.width // 2, display.height // 2),
)
splash.append(text_area)

while True:
    pass