def on_logo_pressed():
    basic.show_string("Hello!")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    basic.show_leds("""
        # . . . #
                . . # # .
                . # . # .
                . . . # .
                # . . # #
    """)
basic.forever(on_forever)
