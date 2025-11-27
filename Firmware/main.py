import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.rgb import RGB

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# Eight GPIO pins
PINS = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP7,
    board.GP6,
    board.GP29,
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Three WS2812/NeoPixel RGB LEDs on GPIO 28
rgb = RGB(pixel_pin=board.GP28, num_pixels=3)
keyboard.modules.append(rgb)

keyboard.keymap = [
    [
        KC.A,
        KC.DELETE,
        KC.MACRO("Hello world!"),
        KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()
