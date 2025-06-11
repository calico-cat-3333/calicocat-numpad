import board

from kmk.bootcfg import bootcfg

bootcfg(
    # required:
    sense = board.GP28,
    # optional:
    source = board.GP27,
    boot_device = 0,
    cdc_console = True,
    cdc_data = False,
    midi = False,
    nkro = True,
    storage = True,
)
