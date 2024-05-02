label chapter3:
    $ persistent.ch3 = True
    scene black

    # Several days later
    "{i}The cafe is bustling. News of a strange shop serving exotic beverages travels swiftly, and more and more curious customers have been finding their way to the Dewdrop Cafe.{/i}"
    "{i}You’ve been whisked away by the frenzy of recent activity, and each night you collapse into bed exhausted and satisfied.{/i}"
    "{i}Kannika hasn’t stopped by since that night. Every evening as you close up shop and take inventory, you catch yourself glancing towards the line where the water and the mud bleed into one another, looking for a glimpse of pearlescent scales.{/i}"
    "{i}The closest you’ve gotten was a brief visit from Luan, who came to retrieve the princess’ forgotten parasol.{/i}"
    "{i}Your questions and attempts at polite conversation were met with terse responses, though he seemed much less hostile than he was during your previous interactions.{/i}"
    "{i}You don’t have too much time to dwell on these thoughts, however. The endless tide of eager patrons ebbs and flows, but rarely stops.{/i}"
    "{i}The few moments you have in between rushes are spent scrambling to and from the back of the cafe, cleaning dishes and restocking ingredients.{/i}"
    window hide

    # Switch to Kari
    show day bg with fade
    pause 0.5
    show kari neutral at right
    with easeinright
    pause 0.5

    # Who is being so noisy?
    window show
    mc "For a kingdom that’s mostly underwater, these people sure are thirsty…"
    play audio "Dewdrop_Bell_Mashing.mp3" volume 0.7
    show kari surprised
    "{i}Your momentary respite is shattered by the frantic ringing of the counter bell.{/i}"
    mc "...!"
    mc "Coming! One moment, I’ll be right with you."
    "{i}You rush to the front of the cafe to see a pair of familiar faces waiting for you.{/i}"

    # Kannika and Luan arrive
    window hide
    show kari -surprised
    with move
    show kannika neutral zorder 1:
        xzoom 1.0
        align (0.2, 0.5)
    with easeinleft
    show luan neutral zorder 2:
        xzoom 1.0
        align (-0.1, 1.0)
    with easeinleft
    pause 0.5

    # It's been awhile...
    window show
    b "Ah, there she is."
    b "I was afraid you had closed up early today."
    mc "Kannika! It’s great to see you again."
    mc "I thought you could only come after sunset, though..."

    # whatdomenu
    window hide
    $ whatdotree = {"patrons": False, "kandl": False}
    menu whatdo:
        "(Glance around at the other patrons)" if not whatdotree["patrons"]:
            $ whatdotree["patrons"] = True
            window show
            "{i}Your regulars have retreated to the periphery of the clearing in which you’ve set up shop. They seem surprised at Kannika’s presence – their postures are torn between deference and wariness.{/i}"
            "{i}Perhaps they fear a breach of conduct for being too close to the princess. Perhaps they simply wish to give her some space.{/i}"
            "{i}Regardless of the reason, they are quietly slipping away – drinks left half-finished on the tables.{/i}"
            window hide
            jump whatdo
        "(Look more closely at Kannika and Luan)" if not whatdotree["kandl"]:
            $ whatdotree["kandl"] = True
            window show
            "{i}Kannika’s face is once again that practiced mask of regal neutrality you’ve seen her don before. Her jaw is clenched and her posture is stiff, though both seem to be relaxing as she speaks to you.{/i}"
            "{i}Luan, meanwhile, seems to be the same as when you last saw him.{/i}"
            "{i}His expression is a blend of suspicion, imperiousness, and mild disdain, all aimed at you as if they were polished blades – more of a reminder than a threat.{/i}"
            window hide
            jump whatdo
        "(Offer the pretty lady a drink)":
            window show
    mc "Anyways, can I get you something to drink?"
    b "Please."
    "{i}You busy yourself with beverage creation. Kannika sits stiffly at the counter, watching you work. It’s clear there’s something on her mind.{/i}"

    # Kari is uncomfortable menu
    window hide
    menu:
        "(Let the awkward silence linger)":
            window show
            b "..."
            mc "...."
            lu "....."
            mc "So-"
        "How've you been?":
            window show
            b "These past few days have been... trying."
            b "I’m sorry I haven’t been able to come by sooner."
            mc "Aw, that's okay."
            mc "I’m sure you must be pretty busy, being a princess and all."
        "What’s the matter? Cat got your tongue?":
            window show
            b "...Who’s the cat here?"
            window hide
            menu:
                "(Infodump)":
                    window show
                    mc "Did you know that’s actually a Catistani idiom?"
                    mc "Well, technically Micelandic, but Miceland’s been a Catistani colony since, like, forever."
                    mc "Anyways, back during the Great War a lot of people didn’t agree with the reasons why we were fighting."
                    mc "They did protests, they held rallies, they gave speeches… It was all across the colonies, particularly in Miceland."
                    mc "It was really hurting morale on the frontlines, so the government took a pretty hardline stance against it."
                    mc "Most people just got some jail time for seditious activities, but the loudest dissidents had it worse."
                    mc "When they got caught, it was a pretty common punishment to cut out their tongues."
                    mc "I think I read that one out of every ten people in Miceland lost their tongue during those days."
                    mc "Gnarly, right?"
                    b "..."
                    mc "..."
                    mc "Sorry, I don’t really know why I said all that."
                    mc "What were we talking about?"
                    b "It’s good to see you too, Kari."
                "Wait, do they have that saying around here?":
                    window show
                    mc "Would “catfish got your tongue” be better?"
                    b "It’s good to see you too, Kari."
        "What about you, Luan?":
            window show
            mc "Finally gonna order something?"
            lu "..."
            lu "No, I don't think I will."
            mc "You’re missing out, you know."
    b "Actually, there’s something I wish to speak with you about, Kari."
    b "Panc– …Luan, could we have some privacy, please?"
    "{i}Luan gives a long, hard look at you before bowing and retreating away from the cafe. He’s still in sight, but mostly out of earshot. You and Kannika are alone together.{/i}"

    # Luan leaves 
    window hide
    show luan neutral at offscreenleft
    with easeoutleft
    play sound "Dewdrop_Slither.mp3" volume 0.7

    # Adjust Kannika placement
    show kannika neutral at left
    with MoveTransition(0.75)

    # Kari and Kannika chat in private *blush*
    mc "...Is this serious? Are you in danger?"
    b "Not quite that serious."
    b "But it’s something that’s been weighing heavily on me for a while now."
    b "You’ve been nothing but kind to me, and you have an outsider’s perspective on this, and..."
    b "I don’t really have anyone else I can talk to about this."
    b "It would mean a lot to me if you could hear me out. Please."
    mc "I would love to, Kannika."
    "{i}You walk out from behind the counter and place a mug of warm hot chocolate – it seemed right for the situation – in front of Kannika. She looks at you with gratitude as you sit next to her and smile reassuringly at her.{/i}"
    mc "Whenever you're ready."
    "{i}Kannika takes a deep breath and begins to speak.{/i}"

    # Cattail Citrus or no Cattail Citrus branch
    if not pickedcitrus:
        b "This question is a bit forward, but..."
        b "Why did you decide to open a traveling cafe?"

        # Kari trauma menu
        window hide
        menu:
            "(Tell the truth)":
                window show
                mc "I… My parents and I had a bit of a disagreement."
                mc "Things were really tense and uncomfortable and I…"
                mc "I just had to get out of the house for a little bit."
                mc "I felt like I couldn’t be myself. I couldn’t be my own person."
                mc "I was being buried alive under all these expectations and traditions and “shoulds” and “should-nots” and they just…"
                mc "They didn’t get it."
                mc "I know they love me, and they have my best interests at heart, but it was just… too much."
                mc "We all needed some space. Me {i}and{/i} them."
            "(Tell a partial truth)":
                window show
                mc "I wanted to see the world."
                mc "My home – the PDRC, I mean – always felt a little… I dunno, stifling?"
                mc "I wanted to see what it was like in other places."
                mc "If it was the same, if it was worse… or if it was better."
                mc "So far, it’s been nothing but better."
                b "How did you do it?"
                b "Your parents… Did they let you go, or did you have their blessing?"
                mc "..."
                mc "My parents and I were actually having a bit of a disagreement."
                mc "We all needed a bit of space, and I had already been thinking about traveling for a while…"
            "(Lie)":
                window show
                mc "It’s always been my dream!"
                mc "I get to make delicious drinks, see amazing sights…"
                mc "And I get to meet amazing people."
                b "How did you do it?"
                b "How did you get from just having a vision to… to actually achieving it?"
                b "To being the person you wanted to be, in the world you wanted to make?"
                mc "Oh, it’s simple, I just…"
                mc "..."
                mc "It’s actually not that simple."
                mc "Ever since I was a kit, I knew who I wanted to be, but…"
                mc "My parents had their own idea of who I was supposed to be."
                mc "That’s the real reason why I left home."
                mc "It’s not that I didn’t want to open the Dewdrop Cafe! That was also a big part of it."
                mc "…But a lot of it was because I needed some space for a bit."
                mc "They needed some space. Just for a little while, so they can cool off a bit."
        mc "So I left."
    if pickedcitrus:
        b "You said you left your home because you were fighting with your parents."
        b "Do you regret that choice?"

        # Kari trauma menu 2
        window hide
        menu:
            "No, not at all!":
                window show
                mc "I love the Dewdrop Cafe!"
                mc "Getting to travel and see the world, getting to meet amazing people and make drinks for them…"
                mc "It’s a dream come true."
                mc "And it’s not like I’ll be gone forever."
                mc "Once they’ve had enough time to calm down, I’ll come back with all these amazing stories to share…"
                mc "They’ll understand."
                mc "Things will go back to the way they were."
            "I get homesick sometimes...":
                window show
                mc "But it’s not like I’ll be gone forever. I’ll go back eventually."
                mc "You know, once things have calmed down a little and we’ve all had some time to breathe."
                mc "They’ll understand."
                mc "Things will be able to go back to the way they were."
        mc "But at the time, I needed to get out of there."
        mc "It wasn’t doing anyone any good for me to just… stay there and push through it."
        mc "So I left."

    # Branches over, back to intimate convo
    b "That’s a very brave thing to do."
    b "With how things have been going, I have half a mind to do the same."
    mc "What do you mean? Kannika, what’s going on?"
    b "Would you prefer the short version or the long version?"

    # Short or long version menu
    window hide
    menu longorshort:
        "The long version.":
            call longversion
        "The short version.":
            window show
            mc "You seem pretty stressed, so let’s get straight to the important stuff"
            b "Very well."
            b "In short, I am all but betrothed to a man whom I have never spoken to."
            b "A man chosen not by any input of mine, or even from my mother, but simply for his fighting skill."
            b "The entirety of my life has been dictated by the whims of others, and in less than a week I will be forced to surrender the remainder of my few freedoms."
            b "I will be consigned to a role as a figurehead, an icon of this kingdom bereft of any agency of her own."
            b "All for the sake of time-honored {i}tradition.{/i}"

            # Long version instead? menu
            window hide
            menu:
                "Uh... Can we do the long version, actually?":
                    window show
                    mc "Sorry, that’s just a lot to wrap my head around."
                    mc "Why is this happening? What kind of tradition is this?"
                    mc "And who is this {i}guy{/i} you’re supposed to get engaged with?"
                    b "Sorry, this is my first time ever really… explaining this situation I’m in."
                    b "Where should I even begin?"
                    call longversion
                "I'm so sorry.":
                    window show
                    mc "Is there anything you can do? Any way to stop it?"
    mc "What about your mom? Have you talked to her about this?"
    b "My mother and I have spoken at length on this subject, and she has made her position clear."
    b "The legitimacy of her reign depends on the support of the nobility and the High Elders, and by extension the observance of traditions such as this one."
    b "She is a ruler first and foremost. Motherhood is a distant second."

    # High elders menu code
    window hide
    $ highelderstree = {"elders": False}
    menu highelders:
        "Real quick, who are these “High Elders”?" if not highelderstree["elders"]:
            $ highelderstree["elders"] = True
            window show
            mc "How is your mother the queen if even she has people who can tell her what to do?"
            b "The High Elders are a council of nine immortal water dragons. They are the progenitors of our people, and the creators of this country."
            b "Their timeless wisdom and millennia of observation is supposed to help guide our queens during their rule and keep the kingdom prosperous…"
            b "…But what that really means is they insist we cling to the old rules and traditions that {i}they{/i} originally put in place."
            mc "I can’t say I’ve met many dragons before, but I think I get the gist."
            window hide
            jump highelders
        "I think your mom’s just trying to look out for you.":
            window show
            mc "Maybe she’s just having a hard time saying it right, but... (pending dialogue)"

    b "It seems that, in the coming days, I will not be able to visit you as freely as I have been."
    b "In fact, it may be quite a while before I am able to leave the castle."
    b "You might move on by then, so…"
    b "I wanted to see you at least once more before then."
    mc "What?!"

    window hide
    menu:
        "Hold on. Start from the beginning.":
            window show
            "(Dialogue pending)"
        "(Option pending)":
            window show
            "(Dialogue pending)"

    # kannika leaves the scene
    show kannika:
        xzoom -1
    show kannika at offscreenleft
    with MoveTransition(2.0)

    scene black
    with fade
    # hide kari with dissolve
    # with Fade(0.5, 0.5, 0.5)
    
    jump chapter4

label longversion:
    window show
    mc "Just take a deep breath and start from the beginning."
    b "Very well."
    b "There are a number of festivals, ceremonies, and rituals that I, as an heiress, am obligated to participate in."
    b "One such ritual is the Dance of Ribbons, a tournament that will conclude at the end of the week."
    b "The victor – the most capable warrior among the champions of the noble houses – is to become my husband, regardless of my wishes otherwise."
    b "Yet another of my few scraps of freedom stripped away in the name of tradition."

    #anything you can do menu code
    window hide
    $ anythingtree = {"ribbon": False, "prize": False, "no": False}
    menu anything:
        "What does a ribbon dance have to do with warriors?" if not anythingtree["ribbon"]:
            $ anythingtree["ribbon"] = True
            window show
            b "It is a contest of martial prowess. Two skilled fighters trading blows, striving to outlast the other in an artful dance of combat."
            b "Its name – the Dance of Ribbons – refers to the flowing garments worn by the warriors."
            b "At the start of a bout, both are adorned in pure white fabric. By the end, their outfits will be stained multicolored hues from each other’s blood and war paint."
            mc "That’s a lot more violent than I expected."
            b "They used to be to-the-death, but these days the matches end when one fighter yields."
            b "These sorts of competitions are central to many of our oldest traditions, and skill in combat is expected of anyone in the nobility."
            mc "Does that mean you can fight too?"
            b "My mother had me trained in wrestling, tail-boxing, and dueling spears."
            mc "What if you joined the tournament as your own champion? Could that work?"
            b "As if I would ever be allowed to fight for the right to make any sort of decision about my own life."
            window hide
            jump anything
        "So the prize is that the winner gets to marry you?" if not anythingtree["prize"]:
            $ anythingtree["prize"] = True
            window show
            b "As with so many things in this kingdom, it’s not quite that simple."
            b "The winner of the Dance is lauded with accolades, and his patron house receives a favored status until the next Dance is held."
            b "However, {i}tradition{/i} dictates that victory earns the winner the right to be {i}considered{/i} as a partner for an unwedded heiress who has come of age."
            b "And it would be completely unheard of for such an accomplished warrior to be rejected without basis."
            mc "So it’s not even an actual rule or anything, it’s just…"
            b "Yes. Expectation, propriety, and the centuries-old song-and-dance of the nobility."
            window hide
            jump anything
        "Can’t you just… say no?" if not anythingtree["no"]:
            $ anythingtree["no"] = True
            window show
            mc "You’re the princess, right? Can’t you just do what you want?"
            b "Kari, I don’t even have the dignity of deciding what I eat for breakfast."
            b "These traditions have been like this for generations. Trying to fight them would be like trying to fight the tides themselves."
            window hide
            jump anything
        "Isn’t there anything you can do?":
            window show
    return