label chapter2: 
    $ persistent.ch2 = True
    show day bg
    with dissolve
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
    "{i}Taking a closer look at the princess, Kari now notices the way she holds her cup: fingers poised in the most perfect angle, and drinking the beverage in carefully, calculated amounts.{/i}"
    "{i}If the guard was not proof enough, this certainly was. Only somebody who has done this all their life, somebody of noble upbringing, would be able to carry themselves with such grace.{/i}"
    
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

    scene black
    with fade
    # hide kari with dissolve 
    # hide day bg with Fade(0.5, 0.5, 0.5)

    jump chapter3
    
    