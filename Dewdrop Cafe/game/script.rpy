define mc = Character("Kari", color="#B6F9C4", window_background=Image("gui/textboxes/textbox_kari.png", style="window"))
define b = Character("Kannika", color="#FFA3CA", window_background=Image("gui/textboxes/textbox_pbf.png", style="window"))
define pb = Character("Princess Kannika", color="#FFA3CA", window_background=Image("gui/textboxes/textbox_pbf.png", style="window"))
define bquestionmark = Character("???", color="#FFA3CA", window_background=Image("gui/textboxes/textbox_pbf.png", style="window"))
define g = Character("Guard", color="#4DE5BA", window_background=Image("gui/textboxes/textbox_pbf.png", style="window"))

#Kari portraits
# image mc neutral: 
#     im.Scale("mc_neutral.png", 732, 1035)
image kari = Live2D("images/Kari", top=-0.037, base=1.0, default_fade=0.0, loop=True)

#Betta Fish portraits
# image betta fish neutral:
#     im.Scale("betta_fish_neutral.png", 1061, 1501)
#     yoffset(300)
image kannika = Live2D("images/Kannika", top=0.075, base=0.825, default_fade=0.0, loop=True)

#Guard portraits
image guard neutral:
    im.Scale("kingdom_guard.png", 944, 1334)
    yoffset(300)

#Food images
image betta drink = im.Scale("BettaDrink.png", 960, 540)
image betta drink 2= im.Scale("BettaDrink2.png", 960, 540)

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
    show kari neutral at center
    with easeinright
    pause 0.25
    window show

    mc "I think a change of scenery is just what I needed."
    mc "Oh, I almost forgot..."

    "{i}Kari reaches into her pocket and pulls out a framed picture of her family, then places it on the counter.{/i}"

    mc "{i}...sigh...{/i}"
    mc "Things have been rough since I left home, but I'm doing well now."
    show kari smile
    mc "The last place I set up shop was quite busy. I had to serve over a dozen drinks at once!"
    show kari -smile
    
    "{i}The framed picture rests silently on the counter.{/i}"

    show kari frown

    mc "...I miss you guys. I promise I'll come back someday... just not today."

    "{i}Suddenly, a loud splashing sound comes from the swamp behind the cafe.{/i}"
    show kari -frown
    show kari surprised

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

    mc "Oh my god, are you okay?"
    
    show kari -surprised
    "{i}Kari lifts the stranger up on their tail.{/i}"

    window hide
    pause 0.25
    show kannika neutral at left
    with easeinbottom
    window show

    bquestionmark "...quickly, do you have a place we can hide?"
    window hide

    menu:
        "Hide?! Are you a criminal?!":
            show kari surprised
            show kannika angry
            window show
            bquestionmark "I can assure you I am anything BUT a criminal."
            show kannika -angry
            bquestionmark "...however, I could really use your help."
            show kari -surprised
            "{i}Kari ponders the circumstances for a moment.{/i}"
            mc "You can hide behind the counter in my cafe."
            show kannika smile
            bquestionmark "Excellent!"
        "You can hide behind the counter in my cafe!":
            show kannika smile
            window show
            bquestionmark "Excellent!"

    "{i}Kari shuffles the stranger into the cafe behind the counter. {/i}"

    window hide
    show kannika:
        xzoom -1.0
    show kannika -smile at offscreenleft
    with easeoutleft
    window show

    "{i}Only a few seconds later, there's some loud splashing coming from behind the cafe.{/i}"

    g "Hurry! I think she went this way!"

    show guard neutral at left
    with easeinleft

    g "You there! Have you seen a lady around here? Pink hair, blue tail, holding a parasol?"

    menu:
        "What's it to ya?":
            show kari angry
            g "We mean no harm, but it is absolutely vital we find her."
            show kari -angry
            mc "I haven't seen her."
        "No, I just got here.":
            pass
        "I don't know who you're talking about.":
            pass
        "Yeah, she's right there, behind my counter.":
            g "Thank you for your service, citizen."
            show guard neutral:
                xzoom -1.0
            show guard neutral at offscreenleft
            with easeoutleft
            show kari at center 
            with move
            "{i}The Nagai is taken away by the guard and Kari never sees her again.{/i}"
            "{i}Perhaps if she had reached out a helping hand to the poor girl instead, things may have turned out differently.{/i}"
            "{i}Maybe the two of them could've even become friends... or really good friends... maybe even roommates.{/i}"
            "{i}But alas, the world will never know.{/i}"
            $ renpy.full_restart(transition=Fade(0.5,0.5,0.25))

    g "If you see someone matching her description, please alert us as soon as possible."
    g "It's too dangerous for her to be out here alone."
    mc "Will do."
    g "Thank you."
    show guard neutral:
        xzoom -1.0
    g "Move out, men!"

    window hide
    show guard neutral at offscreenleft
    with easeoutleft
    pause 1.0
    window show

    mc "..."
    mc "I think they left, you can come out now."

    window hide
    show kannika:
        xzoom 1.0
    show kannika at left
    with MoveTransition(0.75)
    window show 

    bquestionmark "Thank you. I'm not sure what I would have done without your help."
    mc "If you're on the run, shouldn't you be wearing something less flashy?"
    show kannika surprised
    bquestionmark "Less flashy? These are my casual clothes."
    mc "...Right. But why the parasol?"
    bquestionmark "Is that even a question? It completes the fit!"
    show kari surprised
    mc "..."
    mc "{i}Huh.{/i}"
    show kari -surprised
    mc "Most importantly, why were you running from them?"
    show kannika -surprised
    bquestionmark "Let me sit for a moment and catch my breath, then I'll explain everything."
    mc "Fine."
    mc "I don't think the guards are going to come back anytime soon."
    mc "So while you're here, why don't I make you something?"

    with Fade(0.5, 0.5, 0.5)

    show betta drink:
        align (0.5, 0.4)
    "{i}Kari makes a cup of tea and sets it down in front of her mysterious, on-the-run, guest.{/i}"
    "{i}With grace, she picks up the cup and takes a sip.{/i}"
    "{i}And before long, the contents of the drink were gone.{/i}"

    hide betta drink
    bquestionmark "Thank you, that was quite refreshing."
    mc "Glad to see it calmed you down."
    "{i}Kari takes the empty cup and places it in the sink before turning her attention back to the girl.{/i}"
    mc "Now, you feel like telling me what all that fuss earlier was about?"
    bquestionmark "Ah, well you see-"
    "{i}Before the Nagai could even begin to tell her story, they heard a familiar voice, sounding slightly distressed, and not too far in the distance.{/i}"
    g "She isn't here! Maybe we should head back for now and hope she made it back alright."
    show kannika surprised
    bquestionmark "No, they're back already!?"
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
    # "{i}The stranger got up from her seat and was about to leave, but not before turning back around with a smile on her face,{/i}"
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

    #Kannika leaves the scene
    window hide
    show kannika -smile
    show kannika at offscreenleft
    with easeoutleft
    window show

    mc "..."
    mc "parasol..."
    "{i}And with that, she was gone -- leaving just as abruptly as she came.{/i}"
    show kari -surprised
    mc "..."

    show kari at center
    with MoveTransition(0.75)
    mc "Well, I hope she'll be alright..."
    mc "What a strange place I'm in."

    window hide
    hide kari
    show night bg with Fade(0.5,0.5,0.5)

    # SCENE TWO
    "{i}The following day...{/i}"
    show kari neutral at center
    show kari smile 
    mc "Thank you for coming! Have a nice day!"
    show kari -smile
    show kari:
        xzoom -1.0
    mc "Whew, glad to see that I'm getting some customers here already."
    mc "One, two, three, ..."
    show kari smile
    mc "14! Not too bad for the first day."

    "{i}As she finished counting, splashing noises resounded from behind the cafe and a sense of deja vu washes over her.{/i}"
    show kari -smile
    show kari surprised
    bquestionmark "Excuse me, is anyone there?"
    show kari -surprised
    show kari smile
    show kari:
        xzoom 1.0
    mc "Coming! What can I get for-"
    show kari -smile
    show kari surprised at right
    with move
    show kannika neutral zorder 1:
        xzoom 1.0
        align (0.2, 0.5)
    with easeinleft
    show guard neutral zorder 2:
        xzoom 1.0
        align (-0.1, 1.0)
    with easeinleft
    mc "Oh!"
    show kari -surprised
    mc "Well, hello there."
    show guard neutral:
        align (0.04, 1.0)
    with move
    g "Hello miss, my lady seems to have misplaced her parasol around here. Have you by chance seen it around?"
    show kannika angry
    bquestionmark "I am capable of speaking on my own, thank you very much."
    g "..."
    window hide
    show guard neutral:
        align (-0.1, 1.0)
    with move
    show kannika -angry

    menu:
        "Do you mean {i}this{/i} parasol?":
            show kannika smile
            window show
            bquestionmark "Ah yes! Thank you very much!"
        "Don't you have a parasol with you right now?":
            window show
            bquestionmark "Why, yes, indeed I do."
            bquestionmark "However, this is my daytime parasol. The coloring is different!"
            show kari surprised
            bquestionmark "I was looking for my night-time parasol."
            "{i}Kari blinks at her, visibly confused.{/i}"
            "{i}In her eyes, the two parasols had absolutely zero difference in color. Perhaps the Nagai simply had more color receptors?{/i}"
            mc "Right..."
            show kari -surprised
            mc "Anyways, I do have your parasol, let me get it for you."
            show kannika smile
    
    mc "Could I offer you, well, you and your... guards?... anything to drink or eat?"
    bquestionmark "Oh, how I would love to!"
    show kannika -smile
    bquestionmark "So many options! Oh, what to choose?"
    bquestionmark "..."
    show kannika smile
    bquestionmark "The Starfruit Sunset looks very appetizing. I'll gladly take one of those."
    mc "Good choice. And for the others?"
    show kannika -smile
    bquestionmark "Oh, they can't. They're on a strict diet that refrains them from consuming anything that isn't a part of their meals."
    mc "Lovely... well, if I could have you wait over by the side, I'll have your drinks out for you in a bit, Miss..."
    show kannika smile
    b "Kannika. My name is Kannika."
    mc "Thank you, Miss Kannika. I'll have it ready in a short moment."

    window hide
    show kari:
        xzoom -1.0
        align (1.1, 0.5)
    with move
    pause 0.25
    with Fade(0.5, 0.5, 0.5)
    
    window show
    "{i}Almost done making the Starfruit Sunset, Kari reaches for the starfruit...{/i}"
    show kari frown
    mc "Drat!"
    show kannika -smile
    b "Hm? Is there an issue?"
    show kari:
        xzoom 1.0
        align (1.0, 0.5)
    with move
    mc "Yeah, I'm sorry, Miss, but it looks like I am out of starfruits. I was supposed to go find some last night, I guess it slipped my mind."
    b "Oh, don't worry about that, I'll just have my guards go get them for you."
    show kari -frown
    show kari surprised
    mc "Are you sure? It's no big deal, I could always-"
    b "You, go and find some starfruit around here."
    show guard neutral:
        align (0.0, 1.0)
    with move
    g "Milady, you know we cannot leave you unattended. Your mother-"
    show kannika angry
    b "My mother {i}what?{/i}"
    b "I do not recall {i}suggesting{/i} you, I am {i}ordering{/i} you to go and find some."
    g "..."
    show guard neutral:
        align (-0.1, 1.0)
    with move
    g "Yes Milady, we will see to it."
    show kannika -angry
    b "Good. Now off you go."

    # guard leaves 
    window hide
    show guard neutral:
        xzoom -1.0
    show guard neutral at offscreenleft
    with easeoutleft
    pause 0.25
    window show
    "{i}...{/i}"
    window hide
    show kannika at left
    with move
    show kari -surprised
    window show
    show kannika frown
    b "Pardon my tone, but I just had to get them away."
    b "Especially after yesterday, they've been constantly stuck to me like a shadow."
    mc "May I ask what all of that commotion yesterday was about?"
    show kannika -frown
    b "Ah yes, I suppose I should properly introduce myself."

    "{i}Kannika smooths out her skirt and straightens her back.{/i}"
    "{i}Clearing her throat, she spoke out in a clear, sharp voice, {/i}"

    pb "I am Princess Kannika, heir to the throne of the Naga Kingdom, one of the most powerful kingdoms within these parts."

    show kari surprised
    window hide
    menu:
        "{i}Bow{/i}":
            show kannika frown
            window show
            pb "Please do not do that."
            show kari -surprised
            pb "You are the only person who has treated me like a normal person so far, and I would very much like to keep it that way."
        "Ah, so that's what the guards were about.":
            show kari -surprised
            window show
            pb "Yes. Unfortunately, I am required to have them with me at all times."
            mc "That does sound very annoying."
            show kannika frown
            pb "It truly is, especially since they always try to speak up for me."
    
    pb "But yes, I am next in line for the throne."
    pb "The high elders have always been very strict about my life."
    pb "Countless classes on mannerisms and etiquette, language, politics... it gets overwhelming at times."

    window hide
    menu: 
        "High elders?":
            show kannika surprised
            window show
            pb "Oh! You're not aware of our traditions, are you?"
            show kannika -surprised
            pb "Alongside the throne, we have the high elders. They're similar to a council who help with behind-the-scenes work of ruling the kingdom."
            pb "They also help oversee the different factions within the kingdom as well."
            mc "They sound quite important."
            pb "They are."
            pb "However, they aren't always as glamorous as they would like to lead on."
            show kannika angry
            pb "{i}Especially{/i} when they decide how to run the kingdom for me instead of leaving the decision-making to the {i}actual{/i} heir."
            show kannika -angry
        "That sounds rough.":
            window show
            pb "It can be."
            pb "I usually don't mind them much as I know it is my duty to do so, but I've been getting overwhelmed a lot and I'm not sure I know how, nor if I {i}can{/i}, relay that to them."
            show kannika -frown
    
    mc "So then, what was going on last night?"
    pb "Last night, I was getting away from the castle."
    show kannika frown
    pb "I just needed a bit of a breather, but of course, the guards were stationed right outside."
    show kannika -frown
    "{i}A faint rustling was heard coming from the nearby bushes, interrupting the conversation.{/i}"
    pb "Ah, it seems they're back."
    pb "I do hate to cut our conversation short."
    show kannika zorder 1:
        align (0.2, 0.5)
    with move
    show guard neutral zorder 2:
        xzoom 1
        align (-0.1, 1.0)
    with easeinleft
    g "Milady, we found a couple of starfruits."
    show kannika:
        xzoom -1
    pb "Indeed, you have."
    show kannika:
        xzoom 1
    pb "I hope that this will be sufficient..."
    pb "..."
    pb "I'm sorry, I don't believe I ever got your name?"
    show kari smile
    mc "Kari. The name is Kari."
    mc "And these are perfect, thank you!"
    mc "I'll finish making your drink for you."
    show kari -smile

    window hide
    show kari:
        xzoom -1.0
        align (1.1, 0.5)
    with move
    pause 0.25
    with Fade(0.5, 0.5, 0.5)
    pause 0.25
    show kari:
        xzoom 1.0
        align (1.0, 0.5)
    with move


    show betta drink 2 zorder 3:
        align (0.5, 0.4)
    window show
    mc "And here you go, one Starfruit Sunset."
    pb "Thank you."
    "{i}Like the day before, the Nagai elegantly brings the glass to her lips and takes a slow sip.{/i}"
    "{i}Taking a closer look at the princess, Kari now notices the way Princess Kannika held her cup. Fingers poised in the most perfect angle, and drinking the beverage in carefully, calculated amounts.{/i}"
    "{i}If the guards were not proof enough, this certainly was. Only somebody who has done this all their life, somebody of noble upbringing, would be able to carry themselves with such grace.{/i}"

    hide betta drink 2
    "{i}Soon after, Kannika finished her drink.{/i}"
    pb "Thank you, that was very refreshing."
    show kannika frown
    pb "Alas, it seems that I must take my leave now. Duty calls."
    mc "Alright, thank you for coming. Please come again!"
    show kannika -frown
    show kannika smile
    pb "Of course!"
    show kannika -smile

    window hide
    show kannika:
        xzoom -1
    show guard neutral:
        xzoom -1
    show kannika at offscreenleft
    with MoveTransition(1.0)
    show guard neutral at offscreenleft
    with easeoutleft

    show kari at center
    with MoveTransition(0.75)
    window show
    mc "..."
    window hide
    "{i}To be continued...{/i}"

    # return to main menu
    $ renpy.full_restart(transition=Fade(0.5,0.5,0.25))

    # transition to next scene
    # hide kari
    # show night bg with Fade(0.5,0.5,0.5)

    # SCENE THREE



    
    

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

