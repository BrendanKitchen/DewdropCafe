define mc = Character("Kari", color="#B6F9C4", window_background=Image("gui/textboxes/textbox_kari.png", style="window"))
define b = Character("Kannika", color="#FFA3CA", window_background=Image("gui/textboxes/textbox_pbf.png", style="window"))
define pb = Character("Princess Kannika", color="#FFA3CA", window_background=Image("gui/textboxes/textbox_pbf.png", style="window"))
define bquestionmark = Character("???", color="#FFA3CA", window_background=Image("gui/textboxes/textbox_pbf.png", style="window"))
define g = Character("???", color="#4DE5BA", window_background=Image("gui/textboxes/textbox_pbf.png", style="window"))
define lu = Character("Luan", color="#4DE5BA", window_background=Image("gui/textboxes/textbox_pbf.png", style="window"))

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
#image guard neutral:
#    im.Scale("kingdom_guard.png", 944, 1334)
#    yoffset(300)
image luan = Live2D("images/Luan", top=-0.01, base=0.75, default_fade=0.0, loop=True)

#Food images
image betta drink = im.Scale("BettaDrink.png", 960, 540)
image starfruit sunset = im.Scale("BettaDrink2.png", 960, 540)
image cattail citrus = im.Scale("BettaDrink3.png", 960, 540)
image drink bg = "drink_bg.png"

#Backgrounds
image night bg = im.Scale("night_background.png", 1920, 1080)
image inside bg = im.Scale("inside_background.png", 1920, 1080)
image day bg = im.Scale("dewdrop_day_background.png", 1920, 1080)
image photo frame = im.Scale("s1_photo_frame.png", 1920, 1080)

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

    # ----------------------------- SCENE TWO -----------------------------
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

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

    play sound "Dewdrop_DoubleSplash.mp3" volume 0.9
    "{i}As she finishes counting, splashing noises resound from behind the cafe, and a sense of deja vu washes over her.{/i}"
    show kari -smile
    show kari surprised
    play sound "Dewdrop_Bell.mp3" 
    bquestionmark "Excuse me, is anyone there?"
    show kari -surprised
    show kari smile
    show kari:
        xzoom 1.0
    mc "Coming! What can I get for-"

    # KANNIKA AND LUAN ENTER THE SCENE
    show kari -smile
    show kari surprised at right
    with move
    show kannika neutral zorder 1:
        xzoom 1.0
        align (0.2, 0.5)
    with easeinleft
    show luan neutral zorder 2:
        xzoom 1.0
        align (-0.1, 1.0)
    with easeinleft

    mc "Oh!"
    show kari -surprised
    mc "Well, hello there."
    show luan neutral:
        align (0.04, 1.0)
    with move
    g "Hello miss, my lady seems to have misplaced her parasol around here. Have you by chance seen it around?"
    show kannika angry
    bquestionmark "I am capable of speaking on my own, thank you very much."
    show luan frown
    g "..."
    window hide
    show luan -frown
    pause 1.0
    show luan:
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
            bquestionmark "However, this is my daytime parasol."
            show kari surprised
            bquestionmark "I was looking for my night-time parasol. The coloring is different!"
            "{i}Kari blinks at her, visibly confused.{/i}"
            "{i}In her eyes, the two parasols have absolutely zero difference in color. Perhaps the Nagai simply have more color receptors?{/i}"
            mc "Right..."
            show kari -surprised
            mc "Anyways, I do have your parasol, let me get it for you."
            show kannika smile
    
    mc "Could I offer you -- well, you and your... friend? -- anything to drink or eat?"
    bquestionmark "Oh, how I would love to!"
    show kannika -smile
    bquestionmark "So many options! Oh, what to choose?"
    bquestionmark "..."
    show kannika smile
    bquestionmark "The Starfruit Sunset looks very appetizing. I'll gladly take one of those."
    mc "Good choice. And for you, sir?"
    show kannika -smile
    bquestionmark "Oh, he can't, he's on a strict diet that forbids him from consuming anything that wasn't prepared specifically for him."
    mc "Lovely... well, if I could have you wait over by the side, I'll have your drink out for you shortly, Miss..."
    show kannika smile
    b "Kannika. My name is Kannika."
    mc "Thank you, Miss Kannika. I'll have it ready in a moment."

    # Kari goes to make the drink
    window hide
    show kari:
        xzoom -1.0
        align (1.1, 0.5)
    with move
    pause 0.25
    play sound "Dewdrop_MakeDrink.mp3" volume 0.7
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
    mc "Yeah, I'm sorry, Miss, but it looks like I am out of starfruits."
    mc "I didn't expect the Starfruit Sunset to be so popular."
    mc "I was supposed to go find some last night, I guess it slipped my mind."
    b "Oh, don't worry about that, I'll just have my guard go get them for you."
    show kari -frown
    show kari surprised
    mc "Are you sure? It's no big deal, I could always-"
    b "Luan, go and find some starfruit."
    b "I'm sure you can find a fruit merchant in one of the quaint little markets around here."
    show luan neutral:
        align (0.0, 1.0)
    with move
    show luan frown
    lu "Your Highness, you know I cannot leave you unattended. Your mother-"
    show kannika angry
    b "My mother {i}what?{/i}"
    b "I do not recall {i}suggesting{/i} that you go, I am {i}ordering{/i} you to go and find some."
    show luan -frown
    lu "..."
    show luan neutral:
        align (-0.1, 1.0)
    with move
    lu "Yes, Your Highness, I'll see to it."
    show kannika -angry

    # luan leaves 
    window hide
    show luan neutral:
        xzoom -1.0
    show luan neutral at offscreenleft
    with easeoutleft
    play sound "Dewdrop_Slither.mp3" volume 0.7
    pause 0.25

    window show
    "{i}...{/i}"
    window hide
    show kannika at left
    with move
    show kari -surprised
    window show
    mc "Your Highness?"
    b "Ah, you caught that?"
    show kannika frown
    b "Pardon my tone, but I just had to get rid of him."
    b "Especially after yesterday, he's been constantly stuck to me like a remora."

    mc "May I ask what all of that commotion yesterday was about?"
    show kannika -frown
    b "Ah yes, I suppose I should properly introduce myself."
    play sound "Dewdrop_SmoothSkirt.mp3" 
    "{i}Kannika smooths out her skirt and straightens her back.{/i}"
    "{i}Clearing her throat, she speaks out in a clear, sharp voice, {/i}"

    pb "I am Princess Kannika of the Naga Kingdom, the reigning dynasty in these lands."
    show kari surprised
    window hide

    menu:
        "I didn't realize I was in the presence of royalty.":
            show kannika frown
            window show
            pb "Oh please, I'm here to speak to you, not watch you grovel at my feet."
            show kari -surprised
        "Ah, so that's what the guard was about.":
            show kari -surprised
            window show
            pb "Yes. Unfortunately, I am required to have him with me at all times."
            mc "That sounds very annoying."
            show kannika frown
            pb "It truly is, especially since he always tries to speak up for me."
    
    pb "But yes, I am next in line for the throne."
    pb "The High Elders have always been very strict about my life."
    pb "Countless classes on mannerisms and etiquette, language, politics... it gets overwhelming at times."
    pb "They want me to be prepared for when it's my time to rule. Or so they say."
    window hide

    menu: 
        "High elders?":
            show kannika surprised
            window show
            pb "Oh! You're not aware of our form of governance, are you?"
            show kannika -surprised
            pb "Alongside the throne, we have the High Elders. They're similar to a council who help with behind-the-scenes work of ruling the kingdom."
            pb "They also help manage the different factions within the nobility."
            mc "They sound important."
            pb "They are."
            pb "The people of my kingdom are descendants from them, which is why they are revered and respected."
            pb "They are immortal water dragons dedicated to ensuring the prosperity of our people, working in tandem with the royal family."
            pb "However, they aren't quite as benign as they would like others to believe."
            show kannika angry
            pb "{i}Especially when they try to tell someone how she should run her own kingdom.{/i}"
            show kannika -angry
        "That sounds rough.":
            window show
            pb "It can be."
            pb "I usually don't mind them much as I know it is my duty to one day rule, but sometimes their nagging gets under my scales."
            show kannika -frown
    
    mc "So then, what was going on last night?"
    pb "Last night, I was getting away from the castle."
    show kannika frown
    pb "I just needed a bit of a breather, but of course, the guards were stationed right outside."
    show kannika -frown

    play sound "Dewdrop_BushRustling.mp3" volume 0.8
    "{i}A faint rustling is heard coming from the nearby bushes, interrupting the conversation.{/i}"
    pb "Ah, it seems Luan is back."
    pb "I do hate to cut our conversation short."

    # Luan enters the scene
    show kannika zorder 1:
        align (0.2, 0.5)
    with move
    show luan neutral zorder 2:
        xzoom 1
        align (-0.1, 1.0)
    with easeinleft

    lu "Your Highness, I managed to find a couple of starfruits."

    # kannika turns to luan then back to kari
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
    play sound "Dewdrop_MakeDrink.mp3" volume 0.7
    with Fade(0.5, 0.5, 0.5)
    pause 0.25
    show kari:
        xzoom 1.0
        align (1.0, 0.5)
    with move

    show drink bg:
        align (0.5, 0.4)
    show starfruit sunset zorder 3:
        align (0.5, 0.4)
    with dissolve
    window show
    mc "And here you go, one Starfruit Sunset."
    pb "Thank you."
    play sound "Dewdrop_Sip.mp3" volume 0.8
    hide drink bg
    hide starfruit sunset
    with dissolve
    "{i}Like the day before, the Nagai elegantly brings the glass to her lips and takes a slow sip.{/i}"
    "{i}Taking a closer look at the princess, Kari now notices the way Princess Kannika holds her cup. Fingers poised in the most perfect angle, and drinking the beverage in carefully, calculated amounts.{/i}"
    "{i}If the guards were not proof enough, this certainly was. Only somebody who has done this all their life, somebody of noble upbringing, would be able to carry themselves with such grace.{/i}"
    
    "{i}Placing down her cup, Kannika begins to speak, snapping Kari out of her trance.{/i}"
    pb "You know, we rarely see new people here, especially one such as yourself."
    pb "May I ask what you're doing around here?"

    show luan frown
    lu "Your Highness, you shouldn't intrude on someone's personal matters like that."
    lu "Especially someone who we don't know if they are a friend or foe yet."

    mc "Oh, I don't mind."
    mc "And I can assure you that I am, in fact, a friend. At least I hope so."
    show luan -frown
    mc "And to answer your question, I'm just a wandering cafe owner."
    mc "I set up my little cafe shop in different areas and offer different treats for the people."
    show kari smile
    mc "In fact, the drink you ordered was a concoction that I learned how to make while in the {b}Floral Kingdom{/b}!"
    show kannika smile
    pb "That's fascinating! Oh, please tell me more!"

    # fade to black for the passing of time
    with Fade(0.5, 0.5, 0.5)

    "{i}After some idle chit-chat, Kannika finishes her drink, causing Luan to gently nudge her and let her know that it is time to leave.{/i}"
    show kannika -smile
    pb "Ah, it seems I must leave now to return to the kingdom."
    show kannika smile
    pb "I quite enjoyed your drink, I'll be sure to come back again!"
    mc "Thank you for coming. I look forward to seeing you next time!"
    show kannika smile
    pb "Of course!"
    show kannika -smile
    show kari -smile

    window hide
    show kannika:
        xzoom -1
    show luan neutral:
        xzoom -1
    show kannika at offscreenleft
    with MoveTransition(1.0)
    show luan neutral at offscreenleft
    with easeoutleft

    show kari at center
    with MoveTransition(0.75)
    window show
    mc "..."
    window hide

    hide kari with dissolve 
    hide day bg with Fade(0.5, 0.5, 0.5)


    # ----------------------- SCENE TWO POINT FIVE? -----------------------
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    "{i}A few days later...{/i}"
    show kari neutral at right
    with dissolve
    show kannika neutral:
        xzoom 1
        align (0.0, 0.5)
    with dissolve
    show kannika smile

    mc "You know, I've noticed you've been coming here more frequently without your guard."

    "{i}Taking a sip from her cup, Kannika smiles sadly.{/i}"
    show kannika -smile
    show kannika frown
    pb "Oh how I wish that were true." 
    show kannika -frown
    pb "Luan is still around here, just a lot further now that he knows I won't go anywhere further than your cafe."

    mc "Well, good to know he doesn't see me as a threat."
    show kari smile
    mc "Wouldn't want him scaring away my customers now."

    show kannika smile
    pb "You know, for how frequently I visit, I don't seem to know anything about you. Well, aside from you being a wandering cafe owner."
    window hide

    menu:
        "You know my name.":
            show kannika -smile
            window show
            pb "Well, yes, but I mean aside from that."
            mc "Haha, well, what would you like to know?"
        "What would you like to know?":
            show kannika -smile
            pass

    window show
    pb "You mentioned previously that you are a traveling cafe owner. How did that come about?"

    show kari -smile
    mc "Well, for starters, I'm a {b}Purrson{/b} -- if the ears and tail weren't already a giveaway."
    mc "I was born in the PRDC and spent the majority of my life there."

    pb "PRDC?"
    show kannika smile
    pb "Oh! The {b}Purrsons' Democratic Republic of Catistan{/b}! I recall being taught about that country."
    show kannika -smile
    pb "But isn't that on the opposite side of the continent? Why are you venturing so far?"

    mc "Haha, well... let's just say I had a bit of a disagreement with my parents."
    pb "Oh, I'm sorry to hear that. What was the disagreement if you don't mind me asking?"

    mc "Before I get into that, how much do you know about the PRDC?"
    pb "Not much if I'm being honest. I only know it's quite a distance away and that it's a country of Purrsons."

    mc "Pretty accurate description."
    show kari smile
    mc "The land is quite nice there: not too cold, not too hot, and the scenery is beautiful."
    show kari -smile
    show kari frown
    mc "Politically, however, they are very conservative."
    mc "They don't particularly take kind to people who aren't 'normal,' if that makes sense."

    pb "Normal? I'm not quite sure I understand."
    window hide

    menu:
        "Don't fret about it too much.":
            show kari -frown
            mc "Don't fret about it too much, just know that they have a very old-school mindset."
            pb "Ah, I see, gender constructs."
            mc "Close enough."
        "People who don't follow what they believe in.":
            pb "Again, I'm still not quite sure I follow."
            mc "Think romantic interests, identity, stuff like that."
            pb "Ah, I see now."

    pb "So, what was the reason?"

    mc "It played a role, but it wasn't necessarily the reason for my departure."
    mc "My parents have always been a little too overprotective of me."
    mc "I was someone very different growing up, someone who isn't the person you see me as."

    pb "Hard to believe someone as optimistic as you wasn't like that from the start."
    show kari smile
    window hide

    menu:
        "Haha, you'd be surprised...":
            pass
        "I try my best, y'know?":
            pass
        "What's not to be happy about?":
            mc "Well, now I get to travel, make delicious drinks, and meet amazing people. What's not to be happy about?"

    window show
    pb "So then you left because you were different?"
    show kari -smile

    mc "Kind of."
    mc "I told my parents that I wasn't the person they thought I was."
    show kari frown
    mc "They had trouble seeing things the way I saw them and we got into a big argument."
    mc "A lot of things were said at the moment that I'm sure they feel bad about now."

    show kannika angry
    pb "That's absurd! How could they just throw you out like that?"

    show kari -frown
    mc "No, they didn't throw me out."
    show kannika -angry
    mc "I left of my own accord because I didn't want to worsen things between me and my parents."
    mc "In fact, being on my own made me realize that they were caring for me, they just had a hard time showing it."

    show kannika frown
    pb "That doesn't sound like caring to me."

    mc "Well... I thought so too at first, but they were trying to protect me from the society that is the PRDC."
    mc "As much as I would like to change the PRDC's way of thinking, there's only so much I can do."

    show kannika -frown
    pb "Do you plan on going back?"
    window hide

    menu:
        "Eventually, just not right now.":
            window show
            mc "I want to give my parents some time before I decide to face them again."
            pb "That's brave of you. Admirable."
            mc "Thank you, but I promise it's not that brave."
            mc "It just feels like the right thing to do."
            mc "I'm just hoping that when I return, the tension between me and my parents will dissipate."
        "I'm not quite sure yet.":
            window show
            mc "My original plan was to leave for a bit and then return."
            mc "However, I like being on my own and traveling around the continent."
            pb "Oh, that sounds delightful."
            show kannika frown
            pb "Much better than being cooped up in a castle all day listening to politicians argue back and forth."
            show kari smile
            mc "You're only listening to the good parts, but there are a lot of dangers that come with camping in an unfamiliar territory alone."
            show kannika -frown
            show kari -smile

    pb "..."
    mc "..."

    pb "Do you resent them?"
    show kari surprised
    mc "Hm?"
    pb "Your parents."
    show kari -surprised

    mc "Resent isn't the word I would use."
    mc "I understand where they are coming from, and that is something that I choose to respect about them."
    mc "I'm more frustrated than mad at them, but eventually, they'll come around."

    show kannika frown
    pb "..."
    pb "You know, sometimes I wish I could walk away from the palace. Sometimes I wonder what my life would've been like if I wasn't of royal descent."

    show kari smile
    mc "Well, I'm always here to listen to you, {i}Your Highness{i}."

    show kannika -frown
    show kannika smile
    "{i}Kannika rolls her eyes at Kari's playful jab. While not the best attempt, she can tell that the blue haired Purrson is doing her best to lighten the heavy mood.{/i}"

    pb "You know I despise everything about that."

    mc "I kid, I kid."

    "{i}Looking up from the glasses she is cleaning, Kari notices that the sky has gotten considerably darker.{/i}"
    show kari -smile

    mc "Isn't it getting late now? Don't you have to go back to your kingdom?"
    show kannika -smile
    pb "Ugh, don't remind me."
    show kari smile
    mc "Well, as much as I enjoy your company, I don't want Luan to start attacking me on sight for holding his beloved princess captive for too long."
    show kannika smile
    pb "Unless they want to face my disappointment, I doubt that will happen."
    show kannika -smile
    pb "But you are correct, I shall take my departure now."
    pb "Goodbye, Kari."
    window hide

    # kannika leaves the scene
    show kannika:
        xzoom -1
    show kannika at offscreenleft
    with MoveTransition(2.0)

    hide kari with dissolve
    with Fade(0.5, 0.5, 0.5)

    # ---------------------------- SCENE THREE ----------------------------
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    show kari neutral:
        xzoom -1
        align (1.0, 0.5)
    with dissolve
    "{i}One week later...{/i}"

    show kannika neutral:
        xzoom 1
    show kannika at left
    with MoveTransition(1.5)
    play sound "Dewdrop_Bell.mp3" volume 0.8

    show kari:
        xzoom 1

    show kari smile
    mc "Ah, Kannika! Always nice to see you."
    show kannika smile
    pb "Well, aren't you the charmer?"
    show kari -smile
    mc "Your usual, I'm presuming?"
    pb "Actually, I was considering trying something new."
    pb "I always get the same drink, and while it's delicious, I'm feeling a bit adventurous today."
    pb "Something fruity, but not too sweet."
    pb "What do you suggest?"
    window hide

    menu:
        "One of my personal favorites is the Cattail Citrus.":
            window show
            pb "That sounds intriguing, what kind of drink is it?"
            mc "It's a tea that can be served hot or cold -- it's citrus fruit infused in cattail tea."
            mc "It's a bit on the medicinal side because the tea helps soothe the stomach and the citrus helps with digestion, making it easy for the body to consume, which is is why it's popular amongst the older folks."
            mc "I will warn you, however, that the tea is quite strong, which is why the citrus is added, to help reduce the bold flavor of the tea."
            show kannika -smile
            pb "Ooh, that sounds interesting... and healthy."
            pb "How did you come up with such a concoction?"
            show kari smile
            "{i}At the question, Kari smiles fondly, reminiscing about her childhood.{/i}"
            mc "This is something that my mother used to make for me a lot when I was a child."
            mc "Every morning, she'd have me drink cattail tea because, in her words, 'It's good for your body.'"
            mc "I despised the taste of it so much that sometimes I would run away from her whenever she tried to make me drink it."
            show kannika smile
            play sound "Dewdrop_KannikaLaugh.mp3" 

            pb "Oh my, that is hilarious."
            pb "Just imagining baby Kari running around."
            "{i}Kari shoots a playful glare at Kannika{/i}."
            mc "Yeah, yeah, laugh all you want, but it was traumatizing for me as a kid."
            mc "I'd have to hold my breath while I drank it just so I wouldn't have to deal with the taste of it."
            mc "And even then, it was still strong enough for me to taste!"
            mc "Though I will say, she was indeed correct about it being good for you."
            mc "I don't recall ever getting sick for a large portion of my childhood."
            mc "Eventually, my mother started adding citrus fruit to it because citrus fruit is good for your body as well."
            show kari -smile
            mc "{i}And also because she wanted me to drink the tea without the hassle of trying to get me to drink it."
            pb "That's sweet that you decided to keep the drink that tormented you as a child."
            mc "As traumatic as it was, I decided to add it as an homage to my mother."
            mc "Though, I was very surprised by the amount of elderly folks that ordered it."
            mc "Definitely something I was not expecting."
            show kannika -smile
            play sound "Dewdrop_MakeDrink.mp3" volume 0.8

            with Fade(0.5, 0.5, 0.5)
            show drink bg zorder 3:
                align (0.5, 0.4)
            show cattail citrus zorder 3:
                align (0.5, 0.4)
            with dissolve

            "{i}Finished making the drink, Kari places it on the counter in front of Kannika, who is seated in her usual spot.{/i}"
            mc "Well, here you go."
            mc "I'm curious to see what you think of it."
            hide drink bg
            hide cattail citrus
            with dissolve

            "{i}Kannika picks up the glass and inspects the drink from different angles.{/i}"
            pb "Well, it certainly doesn't look daunting and it smells quite delectable."
            pb "..."
            "{i}Bringing the glass to her lips, she takes a cautious sip.{/i}"
            show kari smile
            "{i}To Kari's delight, once the liquid hits her tongue, the princess's face quickly scrunches up from the sourness of the beverage.{/i}"
            pb "Well, that is... quite the taste."
            mc "Haha! I told you it was strong."
            pb "Yes, I can see why you would despise this as a kid."
            mc "It definitely takes some getting used to."
            pb "The more you drink it, the more you'll get accustomed to it."
            show kari -smile
        "The Pink Lady is quite popular with the customers.":
            window show
            pb "Oooh, with a name like that, it's hard to go wrong."
            mc "It's a wapple-infused, lotus iced tea with wapple slices."
            pb "Sounds delicious."
            show kannika -smile
            play sound "Dewdrop_MakeDrink.mp3" volume 0.8 

            # with Fade(0.5, 0.5, 0.5)
            # show drink bg:
            # [ASSET] show Pink Lady:
            # with dissolve
            
            # "{i}Kari quickly makes a Pink Lady and sets in in front of Kannika.{/i}"
            # hide drink bg
            # [ASSET] hide Pink Lady: 
            # with dissolve

            pb "Where did this drink come from?"
            mc "I want to say it was one of the original drinks I made when I was first starting my cafe."
            mc "At that time, I was around the {b}Phibiman Kingdom{/b} and I only had about a few customers."
            mc "While walking around one of the temples, I decided to do one of the tea ceremonies that they offered."
            mc "They brewed a pot of lotus tea and served some wapple slices with it."
            mc "The sweetness from the wapple complimented the subtle floral taste of the tea -- I made sure to bring extras for my cafe."
            pb "That sounds like a wonderful experience."
        "Nothing quite fits what you're looking for.":
            window show
            show kari frown
            mc "I don't think I have anything that quite fits what you're looking for."
            show kannika -smile
            show kannika frown
            pb "Aw, that's unfortunate."
            show kannika -frown
            pb "Well, my usual it is then."
            show kari -frown
            mc "Coming right up!"
            play sound "Dewdrop_MakeDrink.mp3" volume 0.8

            with Fade(0.5, 0.5, 0.5)
            show starfruit sunset zorder 3:
                align (0.5, 0.4)
            "{i}Finished making her usual, Kari sets the Starfruit Sunset down in front of Kannika{/i}."
            hide starfruit sunset
            pb "I remember you mentioned that this drink was something you created from the Floral Kingdom."
            mc "Wow, I'm surprised you remembered that."
            mc "It's a sweet story actually of how I made it."
            show kannika smile
            pb "Oooh, do tell."
            show kari smile
            mc "Well, it was just as I was beginning to close the shop for the day."
            mc "One of my regulars came with her child trotting behind her."
            mc "Cute little guy he was."
            mc "She handed me a basket of starfruit as a thank-you gift."
            mc "She told me that starfruits were their native fruits and she thought that they would make for a good drink."
            mc "I think in total I tried about... seven? eight? different recipes."
            mc "Amongst all of them, the one you're drinking was the most liked."
            mc "A starfruit puree with a hint of mint, combined with cream soda, and topped with starfruit slices, blueberries, and mint leaf garnish."
            mc "The next time I saw her, I let her name the drink and she called it 'Starfruit Sunset' because of the coloring."
            pb "Aw, that's such a lovely story."
            show kannika -smile
            show kari -smile

    pb "I've noticed that the drinks you make are based on your travels."
    mc "That is correct."
    mc "I try to make a drink based on each of the different regions that I visit."
    show kannika surprised
    pb "Does that mean that you will make something based on the Naga Kingdom as well?"
    show kari smile
    mc "That's the plan!"
    show kari -smile
    show kannika -surprised
    show kari frown
    mc "Though, I don't know much about your kingdom aside from what you've told me."
    mc "And I haven't been able to explore your kingdom that much because I've been getting quite the amount of customers."
    show kannika smile
    pb "Oh, allow me!"
    show kari -frown
    show kannika -smile
    window hide

    # kannika leaves the scene for a few seconds, then returns
    show kannika:
        xzoom -1
    show kari surprised
    show kannika at offscreenleft
    with MoveTransition(0.5)
    pause 2.5
    show kannika:
        xzoom 1
    show kannika at left
    with MoveTransition (1.0)

    # [ASSET] show fruits
    # with dissolve

    show kannika smile
    window show
    pb "Here! I think these should work!"
    # [ASSET] hide fruits
    # with dissolve

    mc "Oh my Lanta, they're ginormous!"
    show kari -surprised
    mc "What are they!?"

    pb "They're seamelons, my kingdom's native fruit!"
    pb "They're also one of my favorite fruits."
    pb "They have a soft crunch to them and have plenty of juice inside of them, making them perfect for drinks!"
    pb "Here, cut one open!"

    "{i}Taking a seamelon from Kannika's hand, Kari pulls out a small knife and slices the fruit in half."

    show kari surprised
    mc "Oh wow, that color is just..."
    pb "Gorgeous right?"
    show kari -surprised
    mc "I've never seen anything like it."
    "{i}Kari cuts the fruit into smaller pieces and eats a slice, her eyes lighting up as the flavors erupt in her mouth.{/i}"
    show kari surprised
    mc "!"
    mc "Wow, this tastes amazing!"
    
    pb "Joy! I'm so glad you like it!"

    show kari -surprised
    show kari smile
    mc "This will be perfect for my menu!"
    mc "Would you like to help me make a drink?"

    "{i}Kannika's fins perk up from the suggestion as she quickly slides out of her seat.{/i}"

    pb "I would love to!"

    mc "Here, I'll show you how to prepare fruit for drink making."

    show kari -smile
    show kannika -smile
    "{i}Kannika makes her way around the counter and stands beside Kari.{/i}"
    "{i}Kari hands Kannika the knife and moves to stand behind her, grasping one of the princess' hands in each of her own as she guides her through the motion.{/i}"
    show kannika surprised
    mc "Once you cut them into sections, you'll run the knife along the edge to separate the flesh from the rind."
    show kannika -surprised
    "{i}Together, they begin to cut the seamelon, with Kari carefully guiding Kannika along the way.{/i}"
    show kari smile
    mc "Yeah, just like that."
    show kannika smile
    pb "This is so fun!"
    mc "I'm glad you're enjoying this."
    show kari -smile
    show kannika -smile
    pb "What do we do now?"
    mc "Next is the part where me mix the fruit with different bases to see how they taste with them."
    window hide

    $ seamelon_tested = {"cattail": False, "lotus": False, "soda": False}
    menu seamelon_test:
        "Let's try the cattail tea." if not seamelon_tested["cattail"]:
            $ seamelon_tested["cattail"] = True
            window show 
            "{i}The seamelon steeps with the cattail tea before Kari pours the liquid out into two cups.{/i}"
            mc "..."
            pb "..."
            show kari surprised
            show kannika surprised
            mc "Ahem, I..."
            pb "Wow, uhm..."
            show kannika -surprised
            pb "I do not think that was a success."
            show kari -surprised
            mc "No, that definitely was not a success."
            pb "That tasted as if a tilapia had gone wrong."
            mc "Not quite sure I understand what that means, but I do agree it doesn't taste right."
            mc "The melon probably didn't have a strong enough flavor to compliment the taste of the cattail which is why it tasted like that."
            jump seamelon_test
        "Let's try the lotus tea." if not seamelon_tested["lotus"]:
            $ seamelon_tested["lotus"] = True
            window show 
            "{i}The seamelon steeps with the lotus tea before Kari pours the liquid out into two cups.{/i}"
            pb "Oh, this tastes marvelous."
            mc "I agree, the flavors seem to go well with each-"
            pb "Ew, my Lanta! What is this!?"
            "{i}Sour faces appear on both Kari and Kannika's faces as the taste of the beverage begins to devolve into something repulsive.{/i}"
            show kari frown
            mc "That started fine... but that aftertaste..."
            show kannika frown
            pb "It tasted like an undercooked mackerel."
            show kari -frown
            show kannika -frown
            mc "Nope, not this one then."
            pb "Agreed."
            jump seamelon_test
        "Let's try the cream soda." if not seamelon_tested["soda"]:
            $ seamelon_tested["soda"] = True
            window show 
            "{i}Kari pours cream soda over a bowl of cut-up seamelon.{/i}"
            pb "This looks like... a combination."
            mc "That's one way to put it."
            mc "A little scared, not going to lie."
            "{i}Apprehensively, both Kari and Kannika eat a piece of the fruit that is soaked with the cream soda."
            show kari surprised
            show kannika surprised
            mc "...!"
            pb "...!"
            pb "That is quite good."
            mc "I'm shocked, myself."
            show kari -surprised
            show kannika -surprised
            show kari smile
            show kannika smile
            mc "The sweetness from the soda goes well with the melon and the carbonation helps make the crunch more satisfying."
            pb "It's as if I'm eating freshly cut salmon."
            mc "Well, I'll say that one is a success."
            pb "As do I."
            show kari -smile
            show kannika -smile
    
    pb "However, it still feels as if it's missing something."
    mc "You're right. Though I'm not sure what exactly."
    pb "How about we try adding another fruit?"
    pb "Maybe that will help."
    mc "Hmm..."
    mc "I have extra wapples and starfruit we could try."
    window hide

    menu:
        "Let's try the wapple":
            window show
            "{i}Kari adds the wapples to the bowl of the cream soda and seamelon mixture.{/i}"
            pb "I thought the melon with the cream soda was weird enough, but the wapple slices certainly don't make it look any better."
            mc "Well, the odd one ended up being the best one, so I'm hoping that this will produce similar results."
        "Let's try the starfruit":
            window show
            "{i}Kari adds the starfruit to the bowl of the cream soda and seamelon mixture.{/i}"
            mc "Theoretically, this should be fine because I use the same cream soda in Starfruit Sunsets."
            "{i}Kari and Kannika each take a bite of the new concoction, but their faces quickly scrunch up in disgust.{/i}"
            pb "{i}Blegh!{/i}"
            pb "That did not taste nearly as good as it was when they were separated."
            mc "That's so weird that they don't go together."
            mc "I think it's because the two fruits have such a different taste that they clash with each other."
            show kannika frown
            pb "That's so disappointing."
            mc "Let's try the wapples."
            mc "I think we'll have better success with that."
            show kannika -frown
            "{i}Taking the other seamelon that Kannika brought, Kari prepares a new bowl of seamelon, cream soda, and wapple slices.{/i}"
            pb "This doesn't look nearly as appetizing as the starfruit."
            mc "A shame, really. But anything ought to be better than what we just tasted."
    
    "{i}Taking a deep breath, both Kari and Kannika take a bite of the melon and wapple together.{/i}"
    show kari surprised
    show kannika surprised
    
    pb "Mmmm!"
    mc "It's perfect."
    pb "Splendid!"
    show kari -surprised
    show kannika -surprised
    mc "With a little more tampering, I think this is ready to be served."
    show kannika smile
    pb "Really? do you mean it?"
    mc "Of course! All it's missing now is a name."
    show kari smile
    mc "For giving me the melon, would you like to do the honors of naming it?"
    "{i}At the offer, Kannika's face lights up and her smiles grows even wider than it already was.{/i}"
    pb "I would love to!"
    show kari -smile
    pb "How about we name it..."

    # PLAYER NAMES THE ITEM WITH USER INPUT
    python:
        seamelon_item = renpy.input("How about we name it...", length=64)
        seamelon_item = seamelon_item.strip()

        # IF THE PLAYER DOESN'T NAME THE THING, HERE'S A DEFAULT NAME TO USE 
        if not seamelon_item:
            seamelon_item = "WHY DIDN'T YOU NAME THE THING"
    
    show kari smile
    mc "{color=#3AC8A0}[seamelon_item]{/color} is now the newest addition to Dewdrop Cafe!"
    window hide
    pause 1.0
    hide kari
    hide kannika 
    with dissolve
    with Fade (0.5, 0.5, 0.5)

    # ---------------------------- SCENE FOUR -----------------------------
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    show kari neutral at right
    with dissolve
    "{i}A few days later, Kari is cleaning up her station, when an annoyed Kannika slithers up to the counter and angrily rings the bell.{/i}"
    window hide 

    show kannika angry at left
    with easeinleft
    show kannika neutral

    play sound "Dewdrop_Bell_Mashing.mp3" volume 0.8


    show kari surprised
    pause 0.5
    show kari -surprised
    mc "Well, hello to you too. What's got you all worked up?"

    pb "I am very irritated towards my mother right now."
    pb "All I had requested was to have a civil conversation regarding my future, but what ended up happening was a heated argument and an unnecessary amount of fighting."
    pb "It's like, why do I even bother trying when I can predict the outcome?"
    show kannika -angry
    show kannika frown
    pb "..."
    pb "What if I just left the kingdom and traveled the world like you?"
    window hide

    menu:
        "Oof, that bad huh?":
            window show
            pb "Bad doesn't even begin to cover it."
            mc "Why don't you go sit down and I'll make you something while we talk about it?"
            pb "I'd very much appreciate that."
            pb "{i}Unlike a certain caretaker.{/i}"
        "Let's not get too hasty here":
            window show
            mc "Why don't you go and sit down and I'll make you something while we talk about it?"
            pb "Thank you."
            pb "I would very much like something after what just happened."

    play sound "Dewdrop_MakeDrink.mp3" volume 0.8

    with Fade (0.5, 0.5, 0.5)
    show drink bg:
        align (0.5, 0.4)
    show betta drink:
        align (0.5, 0.4)
    with dissolve
    "{i}Kari quickly mixes up a calming cup of tea and sets it down in front of the sulking Kannika.{/i}"
    hide drink bg
    hide betta drink
    with dissolve
    mc "So, why don't you start from the beginning? What exactly happened?"

    pb "As you know already, I am next in line for the throne after my mother is no longer able to rule."
    window hide 

    menu:
        "What about your father?":
            window show
            mc "I've noticed you've mentioned your mother a lot, what about your father?"
            pb "My father has nothing to do with the kingdom."
            pb "Well, not as much as my mother."
            pb "The Naga Kingdom is a matriarchy, as the High Elders have decreed since the beginning."
            mc "So, what exactly sparked this conflict?"
        "I do recall you telling me about that.":
            window show
            mc "So what exactly sparked this conflict?"

    window show
    pb "Marriage, societal rule, politics, all that stuff."
    window hide

    $ conflict_topics={"marriage":False, "societal":False, "politics":False}
    menu conflict_menu:
        "Marriage?" if not conflict_topics["marriage"]:
            $ conflict_topics["marriage"] = True
            window show
            pb "It is tradition for suitors to compete in arenas in order to be considered a possible candidate for marriage."
            show kari surprised
            pb "However, I absolutely despise the arena and all the fanfare that happens in the pits."
            show kari -surprised
            window hide
            menu: 
                "I never knew your kind could be so... violent.":
                    window show
                    pb "It is within our blood."
                    pb "Violent tendencies have always been common within my kingdom."
                    pb "However, leaving my possible spouse up to the results of a battle royale?"
                    pb "Not for me."
                    pb "Not how I want to spend the rest of my life."
                    window hide
                    jump conflict_menu
                "What happens in the arenas?":
                    window show
                    pb "A bloodbath, for lack of a better term."
                    pb "All candidates are put into matches against each other in front of the whole society, including the High Elders."
                    show kari surprised
                    pb "It's a big event that lasts over a week, sometimes even a month of brawls."
                    mc "Oh my Lanta, that's so... brutal..."
                    pb "Unfortunately, the High Elders use it as their form of entertainment, which transferred over to the rest of society."
                    show kari -surprised
                    window hide
                    jump conflict_menu
        "Societal Rule?" if not conflict_topics["societal"]:
            $ conflict_topics["societal"] = True
            window show
            pb "My mother wants me to think about what kind of leader I would like to be for my people."
            pb "That in and of itself is fine. However, the incessant mentions of the High Elders are enough to drive me insane."
            show kannika -frown
            show kannika angry
            pb "High Elders this, High Elders that, I just don't understand why they still get to dictate how I should rule."
            window hide
            menu:
                "What exactly do the High Elders do?":
                    window show
                    pb "They act like a council to determine the structure of the kingdom."
                    pb "They pretty much decide how things are run while the royal family relays that to the kingdom."
                    show kannika -angry
                    show kannika frown
                    pb "Think of it like a game of chess, where the High Elders are the players and the royal court are the pieces of the game."
                    window hide
                    jump conflict_menu
                "Sounds like a bunch of old people pushing their ideals":
                    window show
                    pb "Because that is precisely what it is."
                    pb "The High Elders are the progenitors of my people."
                    pb "We are all their descendants, yet they still decide to rule over us while idly watching and having the royal family be pawns in their games."
                    mc "Kind of sounds like a certain democratic republic I know a little too well..."
                    show kannika -angry
                    show kannika frown
                    pb "Well, I guess we both have something in common."
                    window hide
                    jump conflict_menu
        "Politics" if not conflict_topics["politics"]:
            $ conflict_topics["politics"] = True
            window show 
            pb "Don't even get me started on that."
            pb "I could go on for hours, and I doubt you'd want to listen to me ramble about every single issue with that."
            window hide
            menu:
                "What if I want you to?":
                    window show
                    pb "Trust me, it's better that I don't, otherwise, you'd be deaf by the time I finish."
                    jump conflict_menu
                "{i}continue{/i}":
                    jump conflict_menu
        "{i}Continue{/i}":
            pass
    
    window show
    pb "The High Elders are very assertive and hard-headed when it comes to traditions and ideals."
    show kannika -frown
    show kannika angry
    pb "In fact, calling them a frenzy of bull sharks would be more appropriate."
    window hide

    menu:
        "A frenzy of bull sharks? Princess, your language!":
            window show 
            "{i}Kannika shoots Kari a disapproving glare, sending chills down her spine.{/i}"
            show kari surprised
            "{i}Never has the princess looked at her with such coldness in her eyes before.{/i}"
            pb "Must you still tease me while I'm talking?"
            pb "Mind you, you were the one who asked."
            show kari -surprised
            show kari frown
            mc "Sorry, I just never would've thought you would say something so vulgar."
            "{i}Annoyed, Kannika rolls her eyes.{/i}"
            show kari -frown
        "{i}Silently gesture for her to continue{/i}":
            pass
    
    window show
    "{i}Kannika sits silently for a moment, gathering her thoughts.{/i}"
    show kannika -angry
    show kannika frown
    pb "The whole ordeal started with me informing my mother that I would like to propose a different type of suitor selection."
    pb "Instead of the tournaments, I'd like to be able to have a say in who I court before I spend the rest of my life with them."
    window hide 

    menu:
        "That makes sense.":
            window show
            mc "That makes sense. I mean, I wouldn't want to be with a total stranger."
            show kannika -frown
            pb "Exactly!"
            show kannika frown
            pb "If only my mother saw it that way."
            pb "But alas, she is nothing but a pawn to the High Elders' wishes and I'm just a 'weak and soft princess.'"
        "But isn't it a part of your cultural tradition?":
            window show
            show kannika -frown
            show kannika angry
            pb "God, you're starting to sound like them."
            show kari surprised
            mc "No no, I didn't mean it like that!"
            show kari -surprised
            mc "But I'm just saying, if it's been in your culture's tradition for a long time, then you knew eventually it would happen to you."
            show kannika -angry
            show kannika frown
            pb "Exactly, which is why I wanted to take preventative measures because I cannot fathom spending my life with a partner who is consistently driven by bloodlust and violence."
            pb "However, my mother keeps insisting that it must be done via the tournaments, as the High Elders have always done it like that."
            pb "They reason that the royal blood needs to be strong and maintained for future generations."
            pb "They say it'll make us look weak and I won't be taken seriously."

    show kari frown
    mc "A little harsh, don't you think?"
    pb "Trust me, they've said worse."
    pb "My mother isn't any better considering she keeps following their orders like a dogfish."
    pb "You'd think that during her reign, she'd have used her voice to do something, yet she always cedes to the High Elders."
    play sound "Dewdrop_KannikaAggressiveSigh.mp3" volume 0.8

    "{i}Kannika lets out a heavy sigh before continuing.{/i}"
    pb "I want to leave -- swim away from my kingdom and not look back."
    show kannika -frown
    pb "Like you did."

    show kari -frown
    show kari surprised
    mc "Now what exactly do you mean by that?"

    pb "What I mean is that you made a choice for yourself and chose to put your past behind you to start a new life."
    pb "To have that kind of courage and bravery to do so... I want to be able to do that."
    
    show kari -surprised
    show kari frown
    mc "I don't know where you got that idea from, but that is certainly not what happened, nor is it what I consider being brave."
    mc "I couldn't bear to keep arguing with my parents, which is why I left."

    pb "Which is what I admire about you."
    show kannika smile
    pb "You decided to leave on your own-"
    window hide

    menu:
        "Because I was afraid.":
            window show
            mc "I'm not as strong as you paint me to be."
            mc "I'm still afraid of going back to face them."
            mc "I'm not ready to see the look on my parents' faces or imagine what they would say if I were to show up after how I left."
        "I didn't leave because I wanted to.":
            window show
            mc "I left because I knew that they weren't going to be able to process what I told them."
            mc "I left because I feared that I had broken the already-strained relationship that I had with them."
            mc "Sure, I learned a lot being on my own, but that's because I couldn't stand to face the disappointment and judgement that my parents had on their faces."

    show kari -frown
    mc "At least you have the potential to change your society from the old traditions that the High Elders set in place."

    show kannika -smile
    show kannika angry

    pb "And how exactly do you propose I do that?"
    pb "In case you were not listening or {i}chose not to care{/i} about what I was saying, the High Elders are the ones who make the decisions, not me."
    window hide 

    menu:
        "Weren't you wishing for more decision in your ruling?":
            window show
            mc "Weren't you the one who was also saying you wish you could have more of a decision in your ruling?"
            show kari angry
            mc "Aside from slacking in your studies, maybe you could spend more time trying to pressure the High Elders into Changing."
        "Fight back.":
            window show
            show kari angry
            mc "Start a petition, attend rallies and protests, talk to the other members of the royal court or something."
            mc "Show them that you want to go against their traditionalist ideals because you disagree with them."

    mc "In the end, you're the one who is going to rule the kingdom-"
    
    pb "Ah yes, the kingdom, because that's all everyone talks about."
    pb "I'm {i}sick{/i} of hearing it from my mother, from the High Elders, and now {i}you{/i}?"
    window hide

    menu:
        "I don't mean-":
            show kari -angry
            show kari surprised
            window show
            pb "Then what else could you possibly have meant?"
            show kari -surprised
        "You know what I meant":
            pb "What are you, a High Elder?"
        
    show kari frown
    pb "I get that I was born with my status and that I must live up to it, but what about {i}my{/i} needs?"
    pb "What about how {i}I{/i} feel?"
    pb "I mean, out of everyone, I thought that you would be the one who understands the most, considering your relationship with your family."
    window hide

    menu:
        "Which is exactly why I'm saying it.":
            window show
            show kari -frown
            show kari angry
            mc "My relationship with my family is strained because I am different and they don't know how to process it."
            mc "I can't force my society or parents to accept me."
            mc "But you, on the other hand, have a relationship with your mother as well as a direct influence on the political side of your kingdom."
            mc "Even if you think of your mother as a puppet to the High Elders, you are her daughter and she is your mother."
        "My relationship with my family has nothing to do with this.":
            window show
            show kari -frown
            show kari angry
            mc "Yes, my relationship with them isn't the greatest, but I told you this already."
            mc "I chose to respect them because they just wanted to protect me."
            mc "I can't force them to change, nor can I force my society to."
            mc "You still have a good enough relationship with your mother as well as a direct connection to the High Elders that you can make an influence."
        
    pb "And what I'm trying to tell you is that I don't have as much power as you think I do!"
    mc "Even if you don't, you are still an important part of the kingdom! Even if your purpose is to be a bridge between the High Elders and the population."
    mc "So why can't you do something about that?"
    play sound "Dewdrop_KannikaAggressiveSigh.mp3" volume 0.8
    "{i}Kannika sighs aggressively, running her hand through her hair and grabbing it, as if wanting to pull her hair out.{/i}"
    pb "We are just going in circles with this and I am getting tired of it."

    # kannika turns around to leave
    show kannika:
        xzoom -1

    pb "You've already said enough. I'm leaving."
    show kari -angry
    show kari surprised
    mc "Kannika, wait-"
    pb "Goodbye, Kari."
    show kannika -smile at offscreenleft
    with easeoutleft 
    play sound "Dewdrop_Slither.mp3" volume 0.8
    "{i}With her mouth full of venom, Kannika bitterly spits out a farewell before quickly slithering away, leaving behind a speechless Kari.{/i}"
    window hide
    show kari -surprised
    show kari frown
    pause 1.0
    hide kari with dissolve
    scene black with dissolve
    "{i}To be continued...{/i}"

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

