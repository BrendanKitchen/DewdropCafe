define mc = Character("Kari", color="#B6F9C4", window_background=Image("gui/textboxes/textbox_kari.png", style="window"))
define b = Character("Princess  Kannika", color="#FFA3CA", window_background=Image("gui/textboxes/textbox_pbf.png", style="window"))
define bquestionmark = Character("???", color="#FFA3CA", window_background=Image("gui/textboxes/textbox_pbf.png", style="window"))
define g = Character("Guard", window_background=Image("gui/textboxes/textbox_pbf.png", style="window"))

#Kari portraits
# image mc neutral: 
#     im.Scale("mc_neutral.png", 732, 1035)
image mc = Live2D("images/Kari", top=-0.037, base=1.0, default_fade=0.0, loop=True)

#Betta Fish portraits
# image betta fish neutral:
#     im.Scale("betta_fish_neutral.png", 1061, 1501)
#     yoffset(300)
image b = Live2D("images/Kannika", top=0.075, base=0.825, default_fade=0.0, loop=True)

#Guard portraits
image guard neutral:
    im.Scale("kingdom_guard.png", 944, 1334)
    yoffset(300)

#Food images
image betta drink = im.Scale("BettaDrink.png", 960, 540)

#Backgrounds
image night bg = im.Scale("night_background.png", 1920, 1080)
image inside bg = im.Scale("inside_background.png", 1920, 1080)

label start:
    #FIRST SCENE
    pause 0.25

    mc "There we go, that should do it!"

    window hide
    pause 0.25
    show night bg with fade
    pause 2.5
    show mc neutral at right
    with easeinright
    pause 0.25
    window show

    mc "I think a change of scenery is just what I needed."
    mc "Oh, I almost forgot..."

    "{i}Kari reaches into her pocket and pulls out a framed picture of her family, then places it on the counter.{/i}"

    mc "{i}...sigh...{/i}"
    mc "Things have been rough since I left home, but I'm doing well now."
    show mc smile
    mc "The last place I set up shop was quite busy. I had to serve over a dozen drinks at once!"
    show mc -smile
    
    "{i}The framed picture rests silently on the counter.{/i}"

    show mc frown

    mc "...I miss you guys. I promise I'll come back someday... just not today."

    "{i}Suddenly, a loud splashing sound comes from the swamp behind the cafe.{/i}"
    show mc surprised

    bquestionmark "{i}Huff... huff...{/i}"
    bquestionmark "...I think I lost them for now."

    mc "Uhhh... what was that?"

    show mc -surprised

    "{i}Kari walks towards the back of the cafe to check out the noise.{/i}"

    mc "Um, hello? Is anyone there?"

    "{i}After rounding the corner, Kari sees a collapsed Nagai breathing heavily.{/i}"
    show mc surprised
    "{i}She quickly runs over to check on them.{/i}"

    mc "Oh my god, are you okay?"
    
    show mc -surprised
    "{i}Kari lifts the stranger up on their tail.{/i}"


    pause 0.25
    show b neutral at left
    with easeinbottom

    bquestionmark "...quickly, do you have a place we can hide?"

    menu:
        "Hide?! Are you a criminal?!":
            show mc surprised
            show b angry
            bquestionmark "I can assure you I am anything BUT a criminal."
            show b -angry
            bquestionmark "...however, I could really use your help."
            show mc -surprised
            "{i}Kari ponders the circumstances for a moment.{/i}"
            mc "You can hide behind the counter in my cafe."
            show b smile
            bquestionmark "Excellent!"
        "You can hide behind the counter in my cafe!":
            show b smile
            bquestionmark "Excellent!"

    "{i}Kari shuffles the stranger into the cafe behind the counter. {/i}"

    show b at offscreenleft
    with easeoutleft

    "{i}Only a few seconds later, there's some loud splashing coming from behind the cafe.{/i}"

    g "Hurry! I think she went this way!"

    show guard neutral at left
    with easeinleft

    g "You there! Have you seen a lady around here? Pink hair, blue tail, holding a parasol?"

    menu:
        "What's it to ya?":
            show mc angry
            g "We mean no harm but it is vital we find her."
            show mc -angry
            mc "I haven't seen her."
        "No, I just got here.":
            pass
        "I don't know who you're talking about.":
            pass

    g "If you see someone matching her description, please alert us as soon as possible."
    g "It's too dangerous for her to be out here alone."
    mc "Will do."
    g "Move out, men!"

    show guard neutral at offscreenleft
    with easeoutleft

    mc "..."
    mc "I think they left, you can come out now."

    show b -smile at left
    with easeinbottom

    bquestionmark "Thank you. I'm not sure what I would have done without your help."
    mc "If you're on the run, shouldn't you be wearing something less flashy?"
    show b surprised
    bquestionmark "Less flashy? These are my casual clothes."
    mc "...Right. But why the parasol?"
    bquestionmark "Is that even a question? It completes the fit!"
    mc "...Okay. Most importantly, why were you running from them?"
    show b -surprised
    bquestionmark "Let me sit for a moment and catch my breath, then I'll explain everything."
    mc "Fine. While you're here, why don't I make you something?"
    

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

