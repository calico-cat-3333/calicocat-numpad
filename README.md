# calicocat-numpad

使用 树莓派 Pico 主控的数字键盘，带旋钮，带扩展接口。

使用 [kmk](https://github.com/KMKfw/kmk_firmware) 固件。

disptest.py 是外扩屏幕用的测试代码，尚未完成。

main.py 和 kb.py 是键盘的主要代码，可在 main.py 中修改键位布局。

boot.py 实现了默认禁用储存和串口，在插入键盘时按住左上角按键可以临时启用。

## 安装固件

在开发板上安装 [circuitpython](https://circuitpython.org/)

克隆 kmk 储存库，并将其中的 kmk 文件夹复制到 CIRCUITPY 储存器中。

将 [neopixel 库](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/main/neopixel.py)复制到在 CIRCUITPY 的 lib 文件夹中。

将 boot.py kb.py main.py 复制到 CIRCUITPY 储存器中。