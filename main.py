import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.extensions.rgb import RGB, AnimationModes

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

rgb = RGB(
    pixel_pin=board.GP0,
    num_pixels=2,
    val=150,
    hue_default=0,
    sat_default=255,
    rgb_order=(1, 0, 2),
    animation_mode=AnimationModes.STATIC,
)
keyboard.extensions.append(rgb)

def make_red(keyboard):
    rgb.set_hsv(0, 255, 150)

def make_green(keyboard):
    rgb.set_hsv(85, 255, 150)

def make_blue(keyboard):
    rgb.set_hsv(170, 255, 150)

def make_purple(keyboard):
    rgb.set_hsv(200, 255, 150)

PINS = [board.GP26, board.GP27, board.GP28, board.GP29]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.MACRO(make_red, KC.A),
        KC.MACRO(make_green, KC.DELETE),
        KC.MACRO(make_blue, "Hello world!"),
        KC.MACRO(make_purple, KC.LCMD(KC.S)),
    ]
]

if __name__ == '__main__':
    keyboard.go()
