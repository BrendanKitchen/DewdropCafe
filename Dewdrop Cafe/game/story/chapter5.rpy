label chapter5:
    $ persistent.ch5 = True

    # Chapter Card Intro
    window hide
    $ quick_menu = False
    scene black bg
    show ch overlay
    show ch5:
        align (0.5, 0.5)
    with fade
    pause 2
    hide ch5
    hide ch overlay
    with fade
    $ quick_menu = True
    window show

    # Intro
    show day bg
    with dissolve
    show kari neutral at right
    with dissolve
    ""
    window hide 

    # return to main menu
    $ renpy.full_restart(transition=Fade(0.5,0.5,0.25))

label runaway:
    

label arrangedmarriage:
    

label rejecttradition:
    

label sloppystyle:
