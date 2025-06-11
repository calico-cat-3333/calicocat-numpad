print("Starting")

# import microcontroller
# # 超频到 150Mhz 或者也可以超频到 180Mhz
# # 网上一些人声称可以超频到 250Mhz 但是我比较保守，暂时只打算超频到 150Mhz
# # 警告：超频可能导致树莓派 pico 损坏，请注意小心
# microcontroller.cpu.frequency = 150000000
# # microcontroller.cpu.frequency = 180000000

import board
import os

from kb import KMKKeyboard
from kmk.keys import KC

from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# # circuitpython 9 上需要进一步降低 refresh_rate
# refresh_rate = 30
# if os.uname().release[0] == '9':
#     refresh_rate = 15

rgb = RGB(
    pixel_pin=board.GP16,
    num_pixels=20,
    val_limit=30,
    val_default=20,
    val_step=1,
    animation_speed=4,
    animation_mode=AnimationModes.RAINBOW,
    refresh_rate=30
)

keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())

keyboard.extensions.append(rgb)
keyboard.extensions.append(MediaKeys())


keyboard.keymap = [[
    KC.A,    KC.B,    KC.C,    KC.D,    KC.E,
    KC.F,    KC.G,    KC.H,    KC.I,    KC.J,
    KC.K,    KC.L,    KC.M,    KC.N,    KC.O,
    KC.P,    KC.Q,    KC.R,    KC.S,    KC.T,
    KC.MUTE, KC.VOLU, KC.VOLD,
    ],]

if __name__ == '__main__':
    #keyboard.debug_enabled = True
    keyboard.go()
