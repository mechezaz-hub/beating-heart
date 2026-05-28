def on_forever():
    basic.show_icon(IconNames.HEART)
    music.set_volume(127)
    music.ring_tone(Note.C)
    basic.show_icon(IconNames.SMALL_HEART)
basic.forever(on_forever)
