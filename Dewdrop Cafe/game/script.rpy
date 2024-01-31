# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("MC")
define b = Character("Betta Fish")

image mc neutral = im.Scale("mc_neutral.png", 732, 1035)

image betta fish neutral:
    im.Scale("betta_fish_neutral.png", 1061, 1501)
    pos (960, 1350)

image night bg = im.Scale("night_background.png", 1920, 1080)
image inside bg = im.Scale("inside_background.png", 1920, 1080)


# The game starts here.

label start:
    # call variables --> uncomment to use variables
    scene night bg
    show mc neutral

    mc "You've created a new Ren'Py game."

    mc "Once you add a story, pictures, and music, you can release it to the world!"

    scene inside bg

    show betta fish neutral

    b "Come in for some tea!"

    menu:
        "Yes":
            pass
            # jump eventName (if "yes" is clicked, goes to eventName, will run until return but nothing below the jump line happens)

        "no":
            pass
            # call eventName2 (if "no" is clicked, goes to eventName2, and once returned, game continues beyond this line) 

    return # end of start, nothing else so it ends the game


# label eventName:
#   ...
# label eventName2:
#   ...
#   return


# label variables --> can organize game variables in here
#   $ variableName = "" --> declare with $, reference with []
#   return

