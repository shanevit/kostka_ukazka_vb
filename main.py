def on_button_pressed_a():
    basic.show_number(randint(1, 6))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global hod
    hod = randint(1, 6)
    for index in range(hod):
        music.play_tone(262, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.QUARTER))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_number(randint(1, 6) + randint(1, 6))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global hod
    hod = randint(1, 6)
    if hod == 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    elif hod == 2:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . # . # .
                        . . . . .
                        . . . . .
        """)
    elif hod == 3:
        basic.show_leds("""
            . . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . .
        """)
    elif hod == 4:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        . # . # .
                        . . . . .
        """)
    elif hod == 5:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . #
        """)
    else:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        # . . . #
                        . . . . .
                        # . . . #
        """)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

hod = 0
basic.show_icon(IconNames.YES)
music.set_built_in_speaker_enabled(True)

def on_forever():
    pass
basic.forever(on_forever)
