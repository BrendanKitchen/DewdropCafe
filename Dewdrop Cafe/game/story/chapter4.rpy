#"{i}{/i}"
label chapter4:
    $ persistent.ch4 = True

    # Play music
    play music "Dewdrop_Forlorn.mp3" volume 0.7

    # Chapter Card Intro
    window hide
    $ quick_menu = False
    scene black bg
    show ch overlay
    show ch4:
        align (0.5, 0.5)
    with fade
    pause 2
    hide ch4
    hide ch overlay
    with fade
    $ quick_menu = True

    # Following day
    window show
    "{i}The following day...{/i}"
    window hide

    # Scene set up
    show night bg
    with dissolve
    show kari neutral at right, sprite_highlight("kari"):
        xzoom 1
    with easeinright

    # Narration
    window show
    n "{i}A healthy flow of thirsty customers helps wash away the lingering thoughts about your conversation with Kannika last night. You smile and laugh, but on the inside you feel cold and exhausted.{/i}"
    play sound "Dewdrop_BushRustling_2.mp3" volume 0.7
    n "{i}As night falls and you begin to put the chairs away, you hear now-familiar rustling in the bushes. Could it be…?{/i}"
    window hide

    # Luan arrives
    show luan neutral at left, sprite_highlight("luan")
    with easeinleft
    pause 0.5

    window show
    n "{i}No frills or parasols in sight. Instead, you see Luan, looking as stern and proper as always.{/i}"

    # Greeting Luan menu
    window hide
    menu:
        "...Oh. It's you.":
            window show
            lu "Yes, drink-peddler. It's me."
            nn "{i}Luan slithers forward to take a seat at the counter of the cafe. He eyes you up and down, studying your face, but he doesn’t seem to find what he’s looking for.{/i}" (cb_name="luan")
            play sound "Dewdrop_LuanSigh.mp3" volume 0.7
            nn "{i}He sighs, posture relaxing, and leans forward to rest his crossed arms on the countertop.{/i}" (cb_name="luan")
        "...Hi, Luan.":
            window show
            lu "Kari."
            nn "{i}Luan nods in greeting before slithering forward to sit at the counter of the cafe. As soon as he settles onto the barstool his entire posture relaxes.{/i}" (cb_name="luan")
            play sound "Dewdrop_LuanSigh.mp3" volume 0.7
            nn "{i}The naga leans forward to rest his crossed arms on the countertop with a sigh.{/i}" (cb_name="luan")
        "...Hi, Pancake.":
            window show
            nn "{i}Luan stares flatly at you. You half expect him to turn around and leave.{/i}" (cb_name="luan")
            play sound "Dewdrop_LuanSigh.mp3" volume 0.7
            nn "{i}Instead, he sighs and shakes his head before slithering forward to take a seat at the counter of the cafe.{/i}" (cb_name="luan")
    mc "What's up?"

    # Follow-up questions menu
    window hide
    menu:
        "How's Kannika?":
            window show
            mc "Is she doing okay? Last night, things got a little…"
            lu "That’s actually part of why I’m here."
        "Are you finally interested in getting a drink?":
            $ luandrink = True
            window show
            nn "{i}He actually seems to consider it. His eyes flit across the menu at the back of the cafe.{/i}" (cb_name="luan")
            lu "A traveling minstrel once compared the color of a land drink to the queen’s hair, praising its vibrancy and hue."
            lu "I can’t recall the name of the drink, but I remember he hailed from the Bahamacaws…"
            mc "Hmm… I haven’t been there yet…"
            mc "Do you remember the ingredients?"
            lu "Some kind of brewed beverage with pink flowers and sliced apples."
            lu "And ice. It also had ice."
            mc "I’ll give it my best shot."
            n "{i}You get to work gathering ingredients – partially because you’re excited that Luan wants a drink, and partially to take your mind off of how strange it feels to see him here without Kannika.{/i}"

            # Kari makes drink
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

            # Show drink
            show drink bg:
                align (0.5, 0.4)
            show pink lady zorder 3:
                align (0.5, 0.4)
            with dissolve

            n "{i}Finally, you set a glass down in front of the naga. The drink is a soft, warm pink that seems to almost glow in the light of the setting sun.{/i}"
            n "{i}It reminds you of the way the light danced across Kannika’s scales when you first met her.{/i}"
            mc "Here it is! Hibiscus iced tea with apple."
            lu "This color… It’s strikingly accurate."
            lu "What is it called?"
            window hide

            # Drink naming menu
            menu:
                "How about “sunset memory?”":
                    window show
                    mc "Seems fitting, right?"
                    lu "Hm. Quite."
                "“Luan’s First Drink?” I dunno, man.":
                    window show
                    lu "…"
                    lu "That works for now, I suppose."
                "Why don’t you pick the name?":
                    $ pink = True
                    window show
                    mc "I mean, you’re the one who described it. It’s not my invention, it’s yours."
                    lu "…"
                    lu "Its name…"
                    lu "…shall be…"
                    lu "……"
                    lu "The… The pink…"
                    lu "The pink… lady?"
                    show kari smile
                    nn "{i}You have to stifle a giggle at the sight of Luan’s face, brow furrowed and cheeks reddening as he stumbles his way through naming this drink.{/i}" (cb_name="kari")
                    nn "{i}His embarrassment soon fades, however, and he allows himself a polite chuckle.{/i}" (cb_name="luan")
                    show kari -smile
                    lu "I am clearly unpracticed at this."
                    mc "No, no – pink lady’s a great name."
                    mc "You mind if I add it to the menu?"
                    lu "Not at all."

            # Luan sip
            hide pink lady with dissolve
            hide drink bg with dissolve
            play sound "Dewdrop_Sip.mp3" volume 0.7
            nn "{i}Luan picks up the glass and tentatively takes a sip through the straw.{/i}" (cb_name="luan")
            show luan surprised
            nn "{i}His eyes go wide as he savors the taste, but he quickly regains his composure and carefully sets the drink back down on the counter.{/i}" (cb_name="luan")
            show luan -surprised
            mc "How is it?"
            play sound "Dewdrop_LuanThroatClear.mp3" volume 0.7
            lu "…It’s… good."
            lu "But we should turn to more pressing matters."
        "I already told you I don’t have any contraband in here.":
            window show
            mc "Especially not any Great Danish infographics about the tyranny and violence of autocratic systems of governance."
            mc "Nope. None of that here, officer."
            lu "…"
            lu "I will never understand foreign comedy."
            mc "Okay but seriously, what’s up? You don’t seem like the type to just pop in for a friendly chat."
            lu "Actually, I am here for a chat. Of sorts."
    
    # Luan informs Kari of her banishment
    lu "I overheard some parts of your conversation with the princess yesterday, and I can guess at the rest."
    lu "Princess Kannika will soon be completely occupied by her royal obligations, as I’m sure she’s told you."
    lu "The queen is no longer willing to overlook her nightly escapades. Nor does she overlook her fraternization with a commoner."
    lu "As such…"
    nn "{i}Luan produces a stack of abalone shells strung together on a length of twine. There’s something carved into the shells – writing, though you can’t make heads or tails of it.{/i}" (cb_name="luan")
    play sound "Dewdrop_LuanThroatClear.mp3" volume 0.7
    nn "{i}Luan clears his throat and begins to read from the shells.{/i}" (cb_name="luan")
    lu "The queen has ordered your banishment from the Naga Kingdom."
    lu "You have until the end of the week to leave our borders, and you may not return to Naga Kingdom lands for a year and a day."
    show kari surprised
    mc "What?! Why??"
    lu "She has decided that you are too much of a distraction for the young princess, and her attention is better directed towards more important matters."
    lu "…"
    lu "I’m sorry."

    # Kari coping menu
    window hide
    menu:
        "Isn’t there something we can do?":
            window show
            lu "Her Majesty has made up her mind. And the High Elders have been urging her to be more strict with the princess for some time now."
            lu "It is out of our hands."
            mc "Then why are you here?"
        "Does Kannika know about this?":
            window show
            lu "She does."
            lu "She argued quite fiercely against it."
            lu "It’s because of her that you have until the end of the week."
            mc "Did she send you here?"
            lu "She… did not."
            mc "Then… Why {i}are{/i} you here?"
        "Take me to the queen right now.":
            window show
            mc "I’ll give her a piece of my mind myself."
            lu "You know that I cannot do that."
            mc "Then why did you even come here?"

    mc "Was it just to tell me this? That I’m being deported? Er, banished, I guess."
    lu "No. I wanted to thank you."
    lu "And perhaps… explain. Or try to explain."

    # Thank me? Menu
    window hide
    menu:
        "Thank me? For what?":
            window show
            lu "For being a friend to the princess."
            lu "The two of you are close. She hasn’t had someone she felt this comfortable with since she was a little girl."
            lu "It made me happy to see her able to speak her mind and set down her burdens for a while."
            mc "Well, I’m glad I was able to be there for her."
            mc "But are you really okay with how things are turning out?"
            mc "If you care about her that much, don’t you see how stressed and unhappy she’ll be after the marriage?"
            lu "I do."
            mc "Don’t you– wait, what?"
            lu "I do. I see how much she’s going through, and how difficult it is for her."
            lu "I see that better than anyone."
            lu "…"
            lu "Let me start from the beginning."
        "Well you'd better start explaining.":
            window show
            mc "Are you gonna tell me that, actually, this guy she’s gonna have to marry is a pretty swell dude?"
            mc "Or maybe you’ll tell me that this is all {i}my{/i} fault for making Kannika want to run away from home?"
            lu "If you want me to explain, you must first give me a {i}chance{/i} to explain."
            play sound "Dewdrop_LuanSigh.mp3" volume 0.7
            lu "…"
            lu "Let me start from the beginning."
        "I don't want to hear anything from you right now.":
            window show
            lu "…"
            lu "Very well."
            lu "At least answer me this, so that I might pass it on to the princess."
            lu "When do you plan to leave the Naga Kingdom?"

            # Bad ending left menu
            window hide
            menu:
                "Leave? I’m not leaving.":
                    window show
                    mc "I {i}can’t{/i} let things end like this."
                    lu "That isn’t an option."
                    lu "Fraternization is one thing, but openly defying a royal decree…"
                    lu "That {i}will{/i} get you thrown in jail. Or worse."
                    mc "Argh, I know, I know! But I can’t– I can’t just…"
                    mc "…At least let me talk to Kannika again."
                    mc "I have until the end of the week, right? I’ll be here until then."
                    mc "Just give me a chance to talk to her and clear things up."
                    mc "I don’t want to let things end like this."
                    lu "…I’ll see what I can do."

                    # Luan leaves
                    show luan at offscreenleft
                    with easeoutleft
                    pause 0.5

                    # Fade out
                    scene black
                    with fade
                    pause 0.5

                    # SCENE ENDS
                    jump chapter5
                "Right away.":
                    window show
                    jump badendingleft
    
    # Luan monologue
    lu "The princess spent most of her childhood being told what she could and could not do."
    lu "She’s always had a strong desire to make her own decisions."
    lu "At first, the queen entertained her impulses and desires, but her patience grew shorter and shorter as Princess Kannika’s rebellious streak continued past adolescence."
    lu "The princess made a habit of breaking out of the palace to visit nearby towns or see novel sights, but she’d always return – one way or another – after no more than a day or so."
    lu "She’s never seriously attempted to run away from home. Yesterday was the first time she’s brought up such an idea."

    # What changed? menu
    window hide
    menu:
        "What changed?":
            window show
            lu "You."
            lu "Your stories, your drinks, how you ran away from your own home…"
            lu "They inspired her."
            mc "But… I mean…"
            mc "It’s not the same. She can’t just leave her kingdom, right?"
            lu "…No."
            lu "But for her to continue on like this…"
        "Do you think she should stay?":
            window show
            lu "…"
            lu "She cannot leave. She is the sole heir to the throne."
            mc "Yeah. Yeah, she has people relying on her."
            mc "It’s not simple like it was for me, right?"
            lu "But for things to stay like this…"
    
    # What do we do? menu
    window hide
    menu:
        "Why do you care so much?":
            window show
            mc "You’re just her bodyguard, right? Or is there something I’m missing?"
            lu "It’s somewhat more than that."
            lu "I am a member of the Halfmoon Guard – the elite warriors tasked with protecting the royal family – but the princess has been in my personal care since she was quite young."
            lu "The position was my prize. My reward for proving myself and claiming the title of champion in the Dance of Ribbons."
        "Well, then what should she do?":
            window show
            lu "Truthfully, there is no simple answer."
            lu "But I cannot help but hope against all hope that there is a different path."
            lu "I hold no reverence for the Dance of Ribbons, and I would hate to see it warp her life as it did mine."
            mc "Wait, the Dance of Ribbons… What do you mean? How did it affect your life?"
            lu "Before I became a member of the Halfmoon Guard, before I was tasked with protecting the young princess…"
            lu "Before all of that, I was a champion."

    # HOL UP
    mc "Wait, hold on. {i}You{/i} were a champion?"
    lu "I’m not familiar with how elite warriors are selected in your home country, but almost all of the Halfmoon Guard are noble-born warriors who proved themselves in one of these tournaments."
    lu "I – like many others – begin our training when we are very young. The noble matriarchs select the most promising sons to become warriors, fighting to earn acclaim and power for their house."
    lu "In fact, the soon-to-be-champion is a warrior from the very house that raised me."
    mc "You know him?"
    lu "Only in passing."
    lu "His name is Rawi. He’s kind-hearted… if a bit simple."
    lu "He is a powerful fighter, but I know for certain he is taking part in the Dance of Ribbons out of no ambition or desire of his own."
    nn "{i}Luan glances around before leaning in and lowering his voice. He whispers conspiratorially, almost drowned out by the sounds of the swamp’s creatures.{/i}" (cb_name="luan")
    lu "The nobility are the ones who take advantage of these tournaments to siphon influence from each other. And the High Elders are more than happy to let them continue with their games of politics."
    mc "So what you’re saying is, both you and Rawi are just pawns on a chess board. You’re being swept along by things outside of your control…"
    lu "…And so is the princess."
    lu "To a certain extent, I believe the queen is subject to this as well."

    # Kari's crazy ideas menu
    window hide
    $ crazyideastree = {"overthrow": False, "mom": False}
    menu crazyideas:
        "We have to overthrow the nobility." if not crazyideastree["overthrow"]:
            $ crazyideastree["overthrow"] = True
            window show
            lu "What?! No, I didn’t say that."
            mc "Are you sure? I mean, I may or may not have some relevant pamphlets I could start distributing…"
            lu "No. Causing wanton chaos would help no one, least of all the princess."
            mc "Well, then…"
            window hide
            jump crazyideas
        "I guess we’ve gotta help Kannika {i}and{/i} her mom flee the country." if not crazyideastree["mom"]:
            $ crazyideastree["mom"] = True
            window show
            mc "She’s a victim of this too, right?"
            lu "…It frightens me that I can’t tell how serious you are about this."
            lu "Regardless, a power vacuum is the last thing this kingdom needs."
            lu "The princess vanishing would be troublesome enough. If the queen was gone as well? I don’t even want to think about what might happen."
            mc "Okay, then…"
            window hide
            jump crazyideas
        "Why are you telling me all this?":
            window show

    # Luan cannot get over the fact that Kari is a foreigner
    lu "Because you’re a foreigner."
    mc "Back to this bit, huh?"
    lu "No, I’m serious."
    lu "I’m telling you this so that you have context for how things work here."
    lu "But you’ve traveled so far. You’ve seen countless other countries."
    lu "If there’s an answer here that neither the princess nor I can see… Maybe you can."
    lu "If she stays, there won’t be any trouble for the kingdom. But the princess will have to come to terms with the reality of her position."
    lu "If she flees… At least she’ll be happy. If it comes to that, I can’t promise that you’ll be able to escape the rest of the Halfmoon Guard, but I’ll help however I can."
    lu "It’s the least I can do."
    lu "And if there’s another way…"
    lu "I hope you can find it."
    mc "…I’ll try my best."

    # Thanks Luan menu
    window hide
    menu:
        "Thank you, Luan.":
            window show
            show luan smile
            nn "{i}Luan smiles at you, a deep gratitude in his eyes. In the light of the cafe you can almost see a weight being lifted off his shoulders just from talking to you.{/i}" (cb_name="luan")
            show luan -smile
        "Thank you, Pancake.":
            window show
            play sound "Dewdrop_LuanSigh.mp3" volume 0.7
            nn "{i}Luan sighs, but it soon turns into a soft chuckle. He shakes his head, and you can see that an invisible weight has been lifted from his shoulders after talking to you.{/i}" (cb_name="luan")
    
    # Will Kari see Kannika again?
    mc "Am I gonna be able to see her again?"
    mc "Before the end of the tournament, I mean."
    lu "I’ll see what I can do."

    # Luan drink conditional dialogue
    if luandrink:
        lu "Thank you for the drink. Truly."
        lu "The next time you visit the Naga Kingdom, I hope you can make it for me again."

    nn "{i}Luan turns and disappears into the night.{/i}" (cb_name="luan")
    window hide

    # Luan leaves
    show luan:
        xzoom -1
    show luan at offscreenleft
    with easeoutleft
    pause 0.5
    window show
    n "{i}You’re left alone with your thoughts, cleaning glasses and folding up chairs as you prepare to tuck in for the night.{/i}"
    window hide
    
    # Fade out
    scene black
    with fade
    pause 0.5

    # Outro
    window show
    n "{i}You mull over Luan’s words. Ideas and possibilities tumble around in your head in a dizzying swirl of color.{/i}"
    n "{i}You keep thinking about Kannika. About how her scales reflected the light when you first met her. About how tears beaded at the corners of her eyes when you last saw her.{/i}"
    n "{i}Will the next time you see her be your last chance to fix things? Will you even be able to fix things?{/i}"
    n "{i}You toss and turn as you try to fall asleep, plagued with memories of the night you left your own home.{/i}"
    n "{i}Was it really worth it? Are you really better off now than you were then?{/i}"
    n "{i}How long have you been telling yourself that you can go home whenever you want?{/i}"
    n "{i}Eventually, exhaustion overtakes you, and you plunge into the smothering grasp of sleep.{/i}"

    jump chapter5

label badendingleft:
    show kari angry
    mc "Clearly, I… I’ve caused Kannika a lot of trouble."
    mc "I don’t want to make things harder for her."
    mc "Saying goodbye is never easy, so…"
    mc "I’ll be gone by tomorrow."
    lu "Is there anything you wish for me to relay to her?"

    # Last message to Kannika menu
    window hide
    menu:
        "Tell her I’m sorry.":
            window show
            mc "I didn’t mean for things to turn out like this."
            mc "And I know it seems really hard, but things’ll get better."
            mc "And I’m– And I…"
            mc "There’s so much I wish I could say but I just don’t have the words."
            lu "…"
        "Tell her I’ll come back some day.":
            window show
            show kari -angry
            mc "My exile’s not forever, right?"
            mc "I’ll come back someday."
            mc "I’m sure I will."

            # Pink Lady conditional dialogue
            if pink:
                mc "And when I do, the three of us can share some nice, refreshing pink ladies!"
            if not pink:
                mc "And when I do, I’m sure I’ll have some brand new drinks to share with you two!"

            lu "…"

        "No. Just tell her I was already gone.":
            window show
            mc "Tell her you came to the clearing and it was empty."
            mc "No tables or chairs, no cafe, no charming barista."
            mc "I was gone by the time you got here."
            lu "Are you sure?"
            mc "Yes."
            mc "It’s easier this way."
            lu "…"

    lu "Very well."
    lu "Goodbye, Kari."

    # Luan Drink conditional dialogue
    if luandrink:
        lu "The drink you made me… I will remember it."
        lu "Just as the princess will remember you."
    nn "{i}Without waiting for a response, Luan turns and disappears into the night.{/i}" (cb_name="luan")
    window hide

    # Luan leaves
    show luan:
        xzoom -1
    show luan at offscreenleft
    with easeoutleft
    pause 0.5

    # Fade out
    scene black
    with fade
    pause 0.5

    # Outro
    window show
    n "{i}As that now-familiar numbness settles back into the core of your being, you go about packing up the cafe.{/i}"
    n "{i}You disassemble the tables and fold up the chairs. You take down the signs and the decorations. You pack up your cups and ingredients.{/i}"
    n "{i}Just as you have done so many times now, you take out your magic briefcase and unlatch it.{/i}"
    n "{i}With a rushing whirlwind of pastels your quaint cafe folds into itself over and over and disappears into the depths of the briefcase.{/i}"
    n "{i}It snaps shut with a solemn finality and settles onto the ground, waiting for you to pick it up and continue your journey.{/i}"
    n "{i}You travel quickly – it’s certainly not the first time you’ve had to leave a place in a hurry.{/i}"
    n "{i}Soon, you’re out of the swamp and into rolling hills rippling with tall grass. The salty sea air fades away as you leave the Naga Kingdom behind.{/i}"
    n "{i}You can only wonder at what will happen to Princess Kannika.{/i}"
    n "{i}Will she accept her mother’s wishes and become the ruler she was meant to be? Will she do as you once did and leave her home under the cover of night, carving her own path?{/i}"
    n "{i}You don’t know. Perhaps you’ll find out; perhaps you never will.{/i}"
    n "{i}Perhaps she’ll seek you out, and the two of you will travel the world together.{/i}"
    n "{i}Right now, however, you are alone. Just you, the road, and whatever awaits you on your journey.{/i}"
    n "{i}Maybe it’s better this way.{/i}"
    window hide
    pause 1.0
    $ renpy.full_restart(transition=Fade(0.5,0.5,0.25))

# Player item user input unused code
label unusednameitem:
    # PLAYER NAMES THE ITEM WITH USER INPUT
    #python:
        #seamelon_item = renpy.input("{i}Enter a name for the new menu item:", length=64)
        #seamelon_item = seamelon_item.strip()

        # IF THE PLAYER DOESN'T NAME THE THING, HERE'S A DEFAULT NAME TO USE 
        #if not seamelon_item:
            #seamelon_item = "WHY DIDN'T YOU NAME THE THING"
    
    #show kari smile
    #mc "{color=#3AC8A0}[seamelon_item]{/color} is now the newest addition to Dewdrop Cafe!"
    #window hide
    #pause 1.0
    #scene black
    #with fade
    # hide kari
    # hide kannika 
    # with dissolve
    # with Fade (0.5, 1.0, 0.5)