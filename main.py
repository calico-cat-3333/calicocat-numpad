print("Starting")

# import microcontroller
# # 超频到 150Mhz 或者也可以超频到 180Mhz
# # 网上一些人声称可以超频到 250Mhz 但是我比较保守，暂时只打算超频到 150Mhz
# # 警告：超频可能导致树莓派 pico 损坏，请注意小心
# microcontroller.cpu.frequency = 150000000
# # microcontroller.cpu.frequency = 180000000

# 参考资料：https://github.com/KMKfw/kmk_firmware/tree/main/docs/en

import board
import os

from kb import KMKKeyboard
from kmk.keys import KC

from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.macros import Macros, Delay, Tap, Press, Release
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# # circuitpython 9 上需要进一步降低 refresh_rate
# refresh_rate = 30
# if os.uname().release[0] == '9':
#     refresh_rate = 15

class LayerRGB(RGB):
    def __init__(self, reserve_indexs=[0], *kargs, **kwargs):
        super().__init__(*kargs, **kwargs)
        self.current_layre = 0
        self.reserve_indexs = reserve_indexs

    def after_matrix_scan(self, sandbox):
        super().after_matrix_scan(sandbox)
        if self.current_layre != sandbox.active_layers[0]:
            self.current_layre = sandbox.active_layers[0]
        self._do_update()

    def show(self):
        for i in self.reserve_indexs:
            self.set_hsv((self.current_layre * 20) % 256, self.sat, self.val, i)
        super().show()

rgb = LayerRGB(
    pixel_pin=board.GP16,
    num_pixels=20,
    val_limit=30,
    val_default=20,
    val_step=1,
    animation_speed=4,
    animation_mode=AnimationModes.RAINBOW,
    refresh_rate=30,
    reserve_indexs=[0, 1, 2, 3, 4]
)

keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())
keyboard.modules.append(Macros())

keyboard.extensions.append(rgb)
keyboard.extensions.append(MediaKeys())

# Macros
VIM_WQ = KC.MACRO(Tap(KC.ESC), ':wq', Tap(KC.ENTER))
VIM_Q = KC.MACRO(Tap(KC.ESC), ':q', Tap(KC.ENTER))
VIM_QF = KC.MACRO(Tap(KC.ESC), ':q!', Tap(KC.ENTER))
VIM_CP = KC.MACRO(Tap(KC.ESC), 'yy')
VIM_CUT = KC.MACRO(Tap(KC.ESC), 'dd')
VIM_PU = KC.MACRO(Tap(KC.ESC), 'P')
VIM_PD = KC.MACRO(Tap(KC.ESC), 'p')
VIM_UNDO = KC.MACRO(Tap(KC.ESC), 'u')
VIM_REDO = KC.MACRO(Tap(KC.ESC), Press(KC.LCTL), Tap(KC.R), Release(KC.LCTL))
VIM_PGU = KC.MACRO(Tap(KC.ESC), Press(KC.LCTL), Tap(KC.B), Release(KC.LCTL))
VIM_PGD = KC.MACRO(Tap(KC.ESC), Press(KC.LCTL), Tap(KC.F), Release(KC.LCTL))
VIM_FTOP = KC.MACRO(Tap(KC.ESC), 'gg')
VIM_FEND = KC.MACRO(Tap(KC.ESC), 'G')

# Keymap
keyboard.keymap = [[
    KC.P7,   KC.P8,   KC.P9,   KC.PSLS, KC.NLCK,
    KC.P4,   KC.P5,   KC.P6,   KC.PAST, KC.LCTL(KC.C),
    KC.P1,   KC.P2,   KC.P3,   KC.PMNS, KC.BSPC,
    KC.MO(1),KC.P0,   KC.PDOT, KC.PPLS, KC.PENT,
    KC.TG(2), KC.VOLU, KC.VOLD,
    ],[
    KC.P7,   KC.P8,   KC.P9,   KC.PSLS, KC.NLCK,
    KC.P4,   KC.P5,   KC.P6,   KC.PAST, KC.LCTL(KC.V),
    KC.P1,   KC.P2,   KC.P3,   KC.PMNS, KC.DEL,
    KC.TRNS, KC.P0,   KC.PDOT, KC.PPLS, KC.PEQL,
    KC.MUTE, KC.BRIU, KC.BRID,
    ],[
    VIM_WQ,  VIM_Q,   VIM_QF,  VIM_FTOP,KC.BSPC,
    VIM_UNDO,VIM_REDO,VIM_PGU, VIM_FEND,KC.DEL,
    VIM_PU,  VIM_PD,  VIM_PGD, KC.K,    KC.ENTER,
    VIM_CP,  VIM_CUT, KC.H,    KC.J,    KC.L,
    KC.TG(2), KC.BRIU, KC.BRID,
    ]]

if __name__ == '__main__':
    #keyboard.debug_enabled = True
    keyboard.go()
