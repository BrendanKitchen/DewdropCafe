# starts with chapter 1
# remaining chapters are in separate .rpy files under the story folder 
# WHEN CREATING NEW CHAPTERS: make sure to add a jump
label start:
    # ----------------------------- SCENE ONE -----------------------------
    play music "pas_de_deuxdrop.mp3"
    pause 0.25
    mc "There we go, that should do it!"

    window hide
    pause 0.25
    show night bg with fade
    pause 2.5
    show kari neutral at center
    with easeinright
    pause 0.25
    window show

    mc "I think a change of scenery is just what I needed."
    mc "Oh, I almost forgot..."

    "{i}Kari reaches into her pocket and pulls out a framed picture of her family, looking at it with a somber gaze.{/i}"
    window hide
    show photo frame with dissolve
    pause 1.0
    window show
    play sound "Dewdrop_KariSigh.mp3" volume 0.7
    mc "{i}...sigh...{/i}"
    mc "Things have been rough since I left home, but I'm doing well now."
    mc "The last place I set up shop was quite busy. I had to serve over a dozen lattes at once!"
    window hide 
    pause 0.5
    hide photo frame with dissolve
    window show
    "{i}Placing it down, the framed picture now rests silently on the counter.{/i}"

    show kari frown

    mc "...I miss you guys. I promise I'll come back someday... just not today."
    play sound "Dewdrop_Splash.mp3" volume 0.7
    "{i}Suddenly, a loud splashing sound comes from the swamp behind the cafe.{/i}"
    show kari -frown
    show kari surprised
    play sound "Dewdrop_KannikaPanting.mp3" volume 0.7
    bquestionmark "{i}Huff... huff...{/i}"
    bquestionmark "...I think I lost them for now."

    mc "Uhhh... what was that?"

    show kari -surprised
    window hide
    show kari:
        xzoom -1.0
        align (1.0, 0.5)
    with MoveTransition(1.0)
    window show

    "{i}Kari walks towards the back of the cafe to check out the noise.{/i}"

    mc "Um, hello? Is anyone there?"

    show kari:
        xzoom 1.0
    "{i}After rounding the corner, Kari sees a collapsed Nagai breathing heavily.{/i}"
    show kari surprised
    "{i}She quickly runs over to check on them.{/i}"

    mc "Oh my Lanta, are you okay?"
    
    show kari -surprised
    "{i}Kari lifts the panting stranger up on their tail.{/i}"

    window hide
    pause 0.25
    show kannika neutral at left
    with easeinbottom
    window show

    bquestionmark "...quickly, do you have a place I can hide?"
    window hide

    menu:
        "Hide?! Are you a criminal?!":
            show kari surprised
            show kannika angry
            window show
            bquestionmark "I can assure you I am anything BUT a criminal."
            show kannika -angry
            bquestionmark "I ask again, do you have a place I can hide?"
            show kari -surprised
            "{i}Kari ponders the circumstances for a moment.{/i}"
            mc "I have a place set up close to here."
            show kannika smile
            bquestionmark "Excellent!"
        "I have a place set up close to here!":
            show kannika smile
            window show
            bquestionmark "Excellent!"

    play sound "Dewdrop_Splash.mp3" volume 0.7
    "{i}Only a few seconds later, there's more loud splashing coming from behind the cafe.{/i}"

    g "She must have gone this way."

    show kannika -smile
    show kannika surprised
    bquestionmark "We must hurry! Lead the way."

    show kannika -surprised
    "{i}Kari brings the stranger into the cafe and shuffles them behind the counter.{/i}"

    window hide
    show kannika:
        xzoom -1.0
    show kannika -smile at offscreenleft
    with easeoutleft

    show luan neutral at left
    with easeinleft

    "{i}Kari just manages to shove the woman's folded parasol out of sight before another Nagai slithers up to the table just outside the cafe.{i}"
    "{i}Seemingly a guard based on their attire, they look around frantically before turning their attention to Kari.{i}"

    window show
    g "You there! Have you seen a lady around here? Pink hair, blue tail, holding a parasol?"
    window hide

    menu:
        "What's it to ya?":
            window show
            show kari angry
            g "I mean no harm, but it is absolutely vital I find her."
            show kari -angry
            mc "I haven't seen her."
        "No, I just got here.":
            pass
        "I don't know who you're talking about.":
            pass
        "Yeah, she's right there, behind my counter.":
            window show
            g "Thank you for your service, citizen."
            show luan neutral:
                xzoom -1.0
            show luan neutral at offscreenleft
            with easeoutleft
            show kari at center 
            with move
            "{i}The Nagai is taken away by the guard and Kari never sees her again.{/i}"
            "{i}Perhaps if she had reached out a helping hand to the poor girl instead, things may have turned out differently.{/i}"
            "{i}Maybe the two of them could've even become friends... or really good friends... maybe even roommates.{/i}"
            "{i}But alas, the world will never know.{/i}"
            window hide
            $ renpy.full_restart(transition=Fade(0.5,0.5,0.25))

    window show
    g "In any case, please bring her back to the {b}Naga Kingdom{/b} if you see her."
    show luan frown
    g "It's too dangerous for her to be out here alone this late in the evening."
    mc "Yessir, I will make sure to do that."
    show luan -frown
    g "Thank you."
    show luan neutral:
        xzoom -1.0

    window hide
    show luan neutral at offscreenleft
    with easeoutleft
    pause 1.0
    window show

    mc "..."
    mc "I think he left, you can come out now."

    window hide
    show kannika:
        xzoom 1.0
    show kannika at left
    with MoveTransition(0.75)
    window show 

    bquestionmark "Thank you. I'm not sure what I would've done had I been caught, but I'm glad you were there."
    mc "If you're on the run, shouldn't you be wearing something, I don't know, less flashy?"
    show kannika surprised
    bquestionmark "Less flashy? This is the most subtle clothing I have available."
    mc "...Right... and your parasol?"
    bquestionmark "Is that even a question? It completes the fit!"
    show kari surprised
    mc "..."
    mc "{i}Huh.{/i}"
    mc "That is ridiculous..."
    show kari -surprised
    mc "Anyways, could I get you something while we are at my cafe?"
    mc "I don't think that guard is going to come back anytime soon."
    show kannika -surprised
    bquestionmark "A cafe? How quaint. For now, a cup of tea sounds nice."

    play sound "Dewdrop_MakeDrink.mp3" volume 0.7
    with Fade(0.5, 0.5, 0.5)

    show drink bg:
        align (0.5, 0.4)
    show betta drink:
        align (0.5, 0.4)
    with dissolve
    "{i}Kari makes a cup of tea and sets it down in front of her mysterious, on-the-run, guest.{/i}"
    play sound "Dewdrop_Sip.mp3" volume 0.8 
    "{i}With grace, she picks up the cup and takes a sip.{/i}"
    "{i}And before long, the contents of the drink are gone.{/i}"

    hide drink bg
    hide betta drink
    with dissolve
    bquestionmark "Thank you, that was quite refreshing."
    mc "Glad to see it calmed you down."
    "{i}Kari takes the empty cup and places it in the sink before turning her attention back to the girl.{/i}"

    mc "Now, you feel like telling me what all that fuss earlier was about?"
    bquestionmark "Ah, well you see-"
    "{i}Before the Nagai can even begin to tell her story, they hear a familiar voice, sounding slightly distressed, and not too far in the distance.{/i}"
    g "Where is she?... I can't rest until I find her."
    show kannika surprised
    bquestionmark  "Dammit, he's back already!?"
    show kannika -surprised
    bquestionmark "I'm sorry, but I really must go."

    window hide
    pause 0.25
    show kannika:
        xzoom -1.0
    pause 0.25
    show kannika:
        align (-0.3, 0.5)
    with move
    pause 0.5
    window show
    bquestionmark "..."
    show kannika:
        xzoom 1.0
        align (0.0, 0.5)
    with move
    show kannika smile
    bquestionmark "Thank you for your service, the drink was delightful."
    show kannika:
        xzoom -1.0
    show kari surprised
    mc "Wait! You forgot your-"
    play sound "Dewdrop_Fwip.mp3" volume 0.9
    #Kannika leaves the scene
    window hide
    show kannika -smile
    show kannika at offscreenleft
    with easeoutleft
    window show
    play sound "Dewdrop_Splash.mp3" volume 0.7
    mc "..."
    mc "parasol..."
    "{i}And with that, she was gone -- leaving just as abruptly as she came.{/i}"
    show kari -surprised
    mc "..."

    show kari at center
    with MoveTransition(0.75)
    mc "Well, I hope she'll be alright..."
    pause 0.5
    mc "What a strange place I'm in."

    window hide
    hide kari
    show day bg with Fade(0.5,0.5,0.5)

    jump chapter2

    # leaving this here in case of a bug
    # but it shouldn't play at all if there are no bugs
    "{i}to be continued{/i}"
    # return to main menu
    $ renpy.full_restart(transition=Fade(0.5,0.5,0.25))

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

