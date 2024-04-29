#   "{i}{/i}"
label chapter2: 
    $ persistent.ch2 = True

    # Intro
    pause 0.25
    window show
    "{i}The following day...{/i}"
    window hide
    pause 0.5
    show day bg
    with dissolve
    show kari neutral at center
    with easeinright
    show kari smile 
    window show
    mc "Thank you for coming! Have a nice day!"
    show kari -smile
    show kari:
        xzoom -1.0
    mc "Whew, glad to see the cafe's already pretty popular."
    mc "Traveling can be fun, but talking to all these new people is just so nice after being on the road."

    if karihelpedkannika == True:
        "{i}It doesn’t take long before you’re all tidied up. You glance over the front of the shop, one last check before you go into the back and take inventory for tomorrow.{/i}"
        "{i}As you pick your way through the stacks of boxes, you wonder when you’ll have the time to go to a market…{/i}"
    else:
        "{i}Out of the corner of your eye, you see that your counter’s suffered a particularly stubborn stain. Scrubbing it with a rag isn’t enough…{/i}"
        "{i}Maybe you have some cleaning solution left over. You go into the back storage and start digging through boxes, trying to remember where you put it…{/i}"
    
    window hide
    pause 0.25
    play sound "Dewdrop_DoubleSplash.mp3" volume 0.8
    with fade
    pause 0.5
    play sound "Dewdrop_DoubleSplash.mp3" volume 0.8
    pause 0.5
    window show
    "{i}A pair of splashes announces the arrival of two more customers. It’s only moments before you hear the ring of the counter bell.{/i}"
    "{i}As she finishes counting, splashing noises resound from behind the cafe, and a sense of deja vu washes over her.{/i}"
    show kari -smile
    show kari surprised
    play sound "Dewdrop_Bell.mp3" 
    bquestionmark "Excuse me, are you still open?"
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
    show luan neutral:
        align (0.04, 1.0)
    with move
    pause 1.0
    show luan:
        align (-0.1, 1.0)
    with move

    menu:
        "…What can I get for you two tonight?":
            show kannika smile
            "{i}The woman flashes you a quick smile.{/i}"
            g "..."
        "You came back!":
            show kannika smile
            show luon angry
            "{i}The woman smiles at you. The guard’s jaw clenches as he stares coldly at you, but he closes his eyes and takes a deep breath before he speaks.{/i}"
            show luon -angry
        "Uh, hello, strange woman whom I have never met before.":
            "{i}The woman coughs into her hand. The guard just sighs, a look of mild disappointment on his face.{/i}"
        "Officer, I think I found the person you're looking for.":
            show kannika angry
            "{i}The woman looks at you with an expression of mock outrage. The guard stares flatly at you, unamused.{/i}"
            show kannika -angry
    
    g "Drink-peddler. My lady says she misplaced her parasol somewhere around here last night."
    show kannika -smile
    bquestionmark "Pancake, please. It’s past sundown, there’s no one else around – I can speak for myself."
    pancake "Princess, it’s a miracle already that your mother is willing to, for the most part, overlook your escapades."
    pancake "It is my duty to act as your sword and veil, so you do not have to stoop so low so as to speak to these commoners."
    pancake "A foreigner, no less."
    show kannika angry
    princess "That is {i}enough{/i}, Luan."
    princess "I already told you what she did for me last night."
    princess "This woman was willing to offer aid to a complete stranger in an unfamiliar land. The least she deserves is respect."
    lu "...Forgive me, your highness."
    lu "..."
    "Luan looks you up and down. After a moment, he gives you a very shallow bow – more of a nod, really – and moves back."

    # luan leaves 
    window hide
    show luan neutral:
        xzoom -1.0
    show luan neutral at offscreenleft
    with easeoutleft
    play sound "Dewdrop_Slither.mp3" volume 0.7
    pause 0.25

    # princess discussion
    $ princesstree = {"sorry": False, "wait": False, "foreigner": False}
    princess "My apologies. Pancake is... very diligent. He means no personal offense."
    mc "..."
    window hide
    menu princessdiscussion:
        "Uh huh. Sorry, did he call you {i}princess{/i}??" if not princesstree["sorry"]:
            $ princesstree["sorry"] = True
            princess "Yes. He did."
            mc "...And?"
            princess "And what?"
            mc "Are you? An actual princess, I mean."
            princess "Yes. I am."
            mc "..."
            princess "..."
            mc "Cool!"
            jump princessdiscussion
        "Wait, is his name Pancake or Luan?" if not princesstree["wait"]:
            $ princesstree["wait"] = True
            princess "It's Luan. Pancake is a nickname I gave him when I was a small child."
            princess "You can call him Pancake too, if you want."
            princess "I'm sure he wouldn't mind."
            jump princessdiscussion
        "Oh, the 'foreigner' stuff? It's okay, I get it." if not princesstree["foreigner"]:
            $ princesstree["foreigner"] = True
            mc "Honestly, I kinda expected him to be a little more intense."
            princess "...More intense?"
            mc "Yeah. He didn't ask for my identification papers. He didn’t accuse me of being an enemy of the state."
            mc "He didn’t even search my cafe for any seditious writings or materials that would threaten the security or moral character of the nation."
            mc "Not that I have anything like that in here."
            mc "Nope. No siree."
            princess "I'm not even going to try to unpack all of that right now."
            jump princessdiscussion
        "You know what, let's just start over.":
            mc "Hi! I'm Kari."
            princess "It's wonderful to meet you, Kari. My name is Kannika."
            mc "Princess Kannika?"
            b "Please, just Kannika."

    # parasol discussion
    mc "Oh! Right! Your parasol..."
    mc "Wait a minute. You have a parasol right now."
    b "..."
    b "This is my backup parasol."
    mc "Uh huh."
    mc "Anyways, can I get you anything to drink?"

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
    
    