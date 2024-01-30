# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

image mc_neutral = im.Scale("mc_neutral.png", 732, 1035)

image night_bg = im.Scale("night_background.png", 1920, 1080)

image inside_bg = im.Scale("inside_background.png", 1920, 1080)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene night_bg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mc_neutral

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    scene inside_bg

    show mc_neutral

    e "Come in for some tea!"

    # This ends the game.

    return
