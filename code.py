import board
import digitalio
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import usb_hid

# Make sure the Keyboard object is instantiated
kbd = Keyboard(usb_hid.devices)

# Set up the first button
button1 = digitalio.DigitalInOut(board.GP7)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

# Set up the second button
button2 = digitalio.DigitalInOut(board.GP2)  # Use a different pin for the second button
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

# Set up the third button
button3 = digitalio.DigitalInOut(board.GP4)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP
    
# Set up the fourth button
button4 = digitalio.DigitalInOut(board.GP0)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.UP

button1_was_pressed = False
button2_was_pressed = False
button3_was_pressed = False
button4_was_pressed = False

while True:
    # Check the first button
    if not button1.value and not button1_was_pressed:
        kbd.press(Keycode.RIGHT_GUI)
        button1_was_pressed = True
    elif button1.value and button1_was_pressed:
        kbd.release(Keycode.RIGHT_GUI)
        button1_was_pressed = False

    # Check the second button
    if not button2.value and not button2_was_pressed:
        kbd.press(Keycode.LEFT_GUI)
        button2_was_pressed = True
    elif button2.value and button2_was_pressed:
        kbd.release(Keycode.LEFT_GUI)
        button2_was_pressed = False

    # Check the third button
    if not button3.value and not button3_was_pressed:
        kbd.press(Keycode.N)
        button3_was_pressed = True
    elif button3.value and button3_was_pressed:
        kbd.release(Keycode.N)
        button3_was_pressed = False

    # Check the fourth button
    if not button4.value and not button4_was_pressed:
        kbd.press(Keycode.V)
        button4_was_pressed = True
    elif button4.value and button4_was_pressed:
        kbd.release(Keycode.V)
        button4_was_pressed = False

    time.sleep(0.01)  # Debounce delay
