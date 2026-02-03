My 4-Key Macropad ProjectHi! This is a simple 4-key macropad I designed. It uses a Seeed Studio XIAO RP2040 and has two RGB lights that change color when you press different buttons.🛠 What you need (BOM)I used these parts for my build:1x Seeed Studio XIAO RP20402x SK6812 RGB LEDs (These are the lights)4x Push Buttons (Mechanical switches)📐 How it is wiredI connected everything to the XIAO board using these pins:PartPin on XIAOButton 1 (SW5)GP26Button 2 (SW1)GP27Button 3 (SW2)GP28Button 4 (SW3)GP29RGB LightsGP0💻 The SoftwareI used KMK Firmware (which runs on CircuitPython). It is very easy because you don't need to "compile" anything—you just save a text file.How it works:Button 1: Types "A" and turns the lights Red.Button 2: Presses "Delete" and turns the lights Green.Button 3: Types "Hello world!" and turns the lights Blue.Button 4: Presses "Cmd + S" (Save) and turns the lights Purple.The Code (main.py)Pythonimport board
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





<img width="911" height="780" alt="Case" src="https://github.com/user-attachments/assets/5ad770ba-4e8c-45f4-9c84-3a0f5a552c46" />
<img width="1176" height="820" alt="Schematic" src="https://github.com/user-attachments/assets/8f90bcac-acde-4107-9e41-08bf648d7206" />
<img width="948" height="795" alt="PCB" src="https://github.com/user-attachments/assets/a42c2b5c-02d2-4bd0-bc63-cfd2cbb2f704" />
<img width="544" height="462" alt="HAckpad" src="https://github.com/user-attachments/assets/445f8c8c-3719-4b76-b83c-b26a6df3908c" />

BOM: 
"ID";"Bezeichner";"Footprint";"Stückzahl";"Bezeichnung";"Anbieter und Referenz";
1;"D1,D3";"LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm";2;"SK6812";;;
2;"SW2,SW1,SW5,SW3";"SW_Cherry_MX_1.00u_PCB";4;"SW_Push";;;
3;"U1";"XIAO-RP2040-DIP";1;"XIAO-RP2040-DIP";;;




