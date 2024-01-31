# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

image mc neutral = im.Scale("mc_neutral.png", 732, 1035)


image betta fish neutral:
    im.Scale("betta_fish_neutral.png", 1061, 1501)
    pos (960, 1350)

image night bg = im.Scale("night_background.png", 1920, 1080)
image inside bg = im.Scale("inside_background.png", 1920, 1080)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene night bg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mc neutral

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    scene inside bg

    show betta fish neutral

    e "Come in for some tea!"

    menu:
        "Yes":
            pass

        "no":
            pass

    # This ends the game.

    return
