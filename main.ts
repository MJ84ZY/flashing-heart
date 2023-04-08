input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    basic.showString("Hello!")
})
basic.forever(function on_forever() {
    basic.showLeds(`
        # . . . #
                . . # # .
                . # . # .
                . . . # .
                # . . # #
    `)
})
