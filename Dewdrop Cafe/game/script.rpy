# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Ka\u0072i", color="#B6F9C4", window_background=Image("gui/textboxes/textbox_kari.png", style="window"))
define b = Character("Princess  Kannika", color="#FFA3CA", window_background=Image("gui/textboxes/textbox_pbf.png", style="window"))

#Kari portraits
image mc neutral = im.Scale("mc_neutral.png", 732, 1035)

#Betta Fish portraits
image betta fish neutral:
    im.Scale("betta_fish_neutral.png", 1061, 1501)
    pos (480, 1350)

#Food images
image betta drink = im.Scale("BettaDrink.png", 960, 540)

#Backgrounds
image night bg = im.Scale("night_background.png", 1920, 1080)
image inside bg = im.Scale("inside_background.png", 1920, 1080)

# The game starts here.
label start:
    #call variables --> uncomment to use variables
    scene night bg
    show mc neutral

    mc "Okay... I think I've finished gathering ingredients for the day."
    mc "I can't believe it's already so late. It's almost time to open the cafe!"
    mc "I wonder who will stop by tonight..."

    scene inside bg
    show mc neutral at right
    with fade

    mc "Just some finishing touches..."
    mc "Aaaaand it's ready! We're open for business!"
    mc "..."
    mc "And now I wait."

    show betta fish neutral with easeinleft

    b "Kari! It's been so long since I last saw you!"
    mc "Oh! Hello Princess Betta Fish!"
    b "It's so nice to see you again. Your smile can brighten up even the worst of days."
    mc "Thank you Princess, but is something wrong?"
    b "It's nothing worth talking about while you're busy working."
    mc "It's not nothing to me! I consider making conversation part of the job."
    b "..."
    b "I've always known since I was younger that one day I would have to take the throne."
    b "The high elders are very attached to old traditions. Everything was decided for me. My clothes, my hobbies, my duties... everything."
    b "I had to fit the image that the high elders created for me... it feels as if I'm just a block of clay made to be molded and shaped by them."
    mc "Could you talk to your parents about this? Maybe they could help."
    b "I never knew my parents. After I hatched from my egg, I was taken away by the high elders because of my tail color."
    b "It's foretold that an heir is born with a blue tail once the current monarch grows close to their end."
    b "Sometimes, I worry that I'm only the princess because I was born lucky... or unlucky? I feel so conflicted."
    mc "I know it's not much, but how about I make you something sweet to cheer you up?"
    b "That would be lovely. Thank you Kari."

    show betta drink at truecenter
    with fade

    mc "Tada!"

# label menuexample:
        # menu:
        # "Yes":
            # pass
            # jump eventName (if "yes" is clicked, goes to eventName, will run until return but nothing below the jump line happens)

        # "no":
            # pass
            # call eventName2 (if "no" is clicked, goes to eventName2, and once returned, game continues beyond this line) 

    # return # end of start, nothing else so it ends the game

# label eventName:
#   ...
# label eventName2:
#   ...
#   return


# label variables --> can organize game variables in here
#   $ variableName = "" --> declare with $, reference with []
#   return

