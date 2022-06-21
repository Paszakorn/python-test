
basic.pause(1000)
basic.clear_screen()

def on_button_pressed_b():
    basic.clear_screen()
    basic.show_string("BUTTON_B_PRESSED")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_a():
    def on_forever():
        basic.show_string("NOW_LOOPING")
        basic.pause(1000)
    basic.forever(on_forever)
input.on_button_pressed(Button.A, on_button_pressed_a)


