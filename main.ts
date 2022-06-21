basic.pause(1000)
basic.clearScreen()
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.clearScreen()
    basic.showString("BUTTON_B_PRESSED")
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.forever(function on_forever() {
        basic.showString("NOW_LOOPING")
        basic.pause(1000)
    })
})
