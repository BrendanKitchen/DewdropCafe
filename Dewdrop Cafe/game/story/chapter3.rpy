label chapter3:
    $ persistent.ch3 = True

    # Play music
    play music "Dewdrop_Forlorn.mp3" volume 0.6

    # Chapter Card Intro
    window hide
    $ quick_menu = False
    scene black bg
    show ch overlay
    show ch3:
        align (0.5, 0.5)
    with fade
    pause 2
    hide ch3
    hide ch overlay
    with fade
    $ quick_menu = True

    # Several days later
    n "{i}The cafe is bustling. News of a strange shop serving exotic beverages travels swiftly, and more and more curious customers have been finding their way to the Dewdrop Cafe.{/i}"
    play sound "Dewdrop_KariSigh.mp3" volume 0.7
    n "{i}You’ve been whisked away by the frenzy of recent activity, and each night you collapse into bed exhausted and satisfied.{/i}"
    n "{i}Kannika hasn’t stopped by since that night. Every evening as you close up shop and take inventory, you catch yourself glancing towards the line where the water and the mud bleed into one another, looking for a glimpse of pearlescent scales.{/i}"
    play sound "Dewdrop_LuanThroatClear.mp3" volume 0.7
    n "{i}The closest you’ve gotten was a brief visit from Luan, who came to retrieve the princess’ forgotten parasol.{/i}"
    play sound "Dewdrop_LuanSigh.mp3" volume 0.7
    n "{i}Your questions and attempts at polite conversation were met with terse responses, though he seemed much less hostile than he was during your previous interactions.{/i}"
    n "{i}You don’t have too much time to dwell on these thoughts, however. The endless tide of eager patrons ebbs and flows, but rarely stops.{/i}"
    play sound "Dewdrop_Clatter.mp3" volume 0.7
    n "{i}The few moments you have in between rushes are spent scrambling to and from the back of the cafe, cleaning dishes and restocking ingredients.{/i}"
    window hide

    # Switch to Kari
    show day bg with fade
    pause 0.5
    show kari neutral at center, sprite_highlight("kari")
    with easeinright
    pause 0.5

    # Who is being so noisy?
    window show
    show kari sweatdrop
    mc "For a kingdom that’s mostly underwater, these people sure are thirsty…"
    play audio "Dewdrop_Bell_Mashing.mp3" volume 0.7
    show kari exclamation
    n "{i}Your momentary respite is shattered by the frantic ringing of the counter bell.{/i}"
    mc "...!"
    mc "Coming! One moment, I’ll be right with you."
    show kari surprised
    n "{i}You rush to the front of the cafe to see a pair of familiar faces waiting for you.{/i}"
    show kari -surprised at sprite_highlight("kari")
    window hide
    pause 0.25

    # Kannika and Luan arrive
    show kari neutral at right, sprite_highlight("kari")
    with move
    show kannika neutral zorder 1 at sprite_highlight("kannika"):
        xzoom 1.0
        align (0.2, 0.5)
    with easeinleft
    show luan neutral zorder 2 at sprite_highlight("luan"):
        xzoom 1.0
        align (-0.1, 1.0)
    with easeinleft
    pause 0.5

    # It's been awhile...
    window show
    show kannika smile at sprite_highlight("kannika")
    b "Ah, there she is."
    show kannika -smile
    b "I was afraid you had closed up early today."
    show kari smile
    mc "Kannika! It’s great to see you again."
    show kari -smile
    mc "I thought you could only come after sunset, though..."

    # whatdomenu
    window hide
    $ whatdotree = {"patrons": False, "kandl": False}
    menu whatdo:
        "(Glance around at the other patrons)" if not whatdotree["patrons"]:
            $ whatdotree["patrons"] = True
            window show
            n "{i}Your regulars have retreated to the periphery of the clearing in which you’ve set up shop. They seem surprised at Kannika’s presence – their postures are torn between deference and wariness.{/i}"
            n "{i}Perhaps they fear a breach of conduct for being too close to the princess. Perhaps they simply wish to give her some space.{/i}"
            show kari sweatdrop
            n "{i}Regardless of the reason, they are quietly slipping away – drinks left half-finished on the tables.{/i}"
            show kari -sweatdrop
            window hide
            jump whatdo
        "(Look more closely at Kannika and Luan)" if not whatdotree["kandl"]:
            $ whatdotree["kandl"] = True
            window show
            nn "{i}Kannika’s face is once again that practiced mask of regal neutrality you’ve seen her don before. Her jaw is clenched and her posture is stiff, though both seem to be relaxing as she speaks to you.{/i}" (cb_name="kannika")
            nn "{i}Luan, meanwhile, seems to be the same as when you last saw him.{/i}" (cb_name="luan")
            nn "{i}His expression is a blend of suspicion, imperiousness, and mild disdain, all aimed at you as if they were polished blades – more of a reminder than a threat.{/i}" (cb_name="luan")
            window hide
            jump whatdo
        "(Offer the pretty lady a drink)":
            window show
    show kari sparkle
    mc "Anyways, can I get you something to drink?"
    show kari -sparkle
    b "Please."
    n "{i}You busy yourself with beverage creation.{/i}"
    
    # Kari makes drink for Kannika
    window hide
    show kari neutral:
        xzoom -1.0
        align (1.1, 0.5)
    with move
    pause 0.25
    play sound "Dewdrop_MakeDrink.mp3" volume 0.7
    with Fade(0.5, 0.5, 0.5)
    pause 0.25
    show kari at sprite_highlight("kari"):
        xzoom 1.0
        align (1.0, 0.5)
    with move

    window show
    n "{i}Kannika sits stiffly at the counter, watching you work. It’s clear there’s something on her mind.{/i}"

    # Kari is uncomfortable menu
    window hide
    menu:
        "(Let the awkward silence linger)":
            window show
            b "..."
            show kari sweatdrop at sprite_highlight("kari")
            mc "...."
            lu "....."
            mc "So-"
            show kari -sweatdrop
        "How've you been?":
            window show
            show kannika frown at sprite_highlight("kannika")
            b "These past few days have been... trying."
            b "I’m sorry I haven’t been able to come by sooner."
            mc "Aw, that's okay."
            mc "I’m sure you must be pretty busy, being a princess and all."
        "What’s the matter? Cat got your tongue?":
            window show
            show kannika speechless at sprite_highlight("kannika")
            b "...Who’s the cat here?"
            show kannika -speechless
            window hide
            menu:
                "(Infodump)":
                    window show
                    show kari sparkle at sprite_highlight("kari")
                    mc "Did you know that’s actually a Catistani idiom?"
                    mc "Well, technically Micelandic, but Miceland’s been a Catistani colony since, like, forever."
                    mc "Anyways, back during the Great War a lot of people didn’t agree with the reasons why we were fighting."
                    show kannika sweatdrop at sprite_highlight("kannika")
                    mc "They did protests, they held rallies, they gave speeches… It was all across the colonies, particularly in Miceland."
                    mc "It was really hurting morale on the frontlines, so the government took a pretty hardline stance against it."
                    mc "Most people just got some jail time for seditious activities, but the loudest dissidents had it worse."
                    mc "When they got caught, it was a pretty common punishment to cut out their tongues."
                    mc "I think I read that one out of every ten people in Miceland lost their tongue during those days."
                    mc "Gnarly, right?"
                    b "..."
                    show kari -sparkle
                    mc "..."
                    show kari sweatdrop
                    mc "Sorry, I don’t really know why I said all that."
                    mc "What were we talking about?"
                    show kannika smile
                    b "It’s good to see you too, Kari."
                    show kari -sweatdrop
                    show kannika -smile
                "Wait, do they have that saying around here?":
                    window show
                    mc "Would “catfish got your tongue” be better?"
                    show kannika smile
                    b "It’s good to see you too, Kari."
                    show kannika -smile
        "What about you, Luan?":
            window show
            show kari sparkle at sprite_highlight("kari")
            mc "Finally gonna order something?"
            show kari -sparkle
            lu "..."
            lu "No, I don't think I will."
            show kari gloom
            mc "You’re missing out, you know."
            show kari -gloom
    b "Actually, there’s something I wish to speak with you about, Kari."
    play sound "Dewdrop_KannikaClearThroat.mp3" volume 0.7
    b "Panc– …Luan, could we have some privacy, please?"
    n "{i}Luan gives a long, hard look at you before bowing and retreating away from the cafe. He’s still in sight, but mostly out of earshot. You and Kannika are alone together.{/i}"

    # Luan leaves 
    window hide
    show luan neutral at offscreenleft
    with easeoutleft
    play sound "Dewdrop_Slither.mp3" volume 0.7

    # Adjust Kannika placement
    show kannika neutral at left, sprite_highlight("kannika")
    with MoveTransition(0.75)

    # Kari and Kannika chat in private *blush*
    show kari exclamation at sprite_highlight("kari")
    mc "...Is this serious? Are you in danger?"
    show kari surprised
    b "Not quite that serious."
    b "But it’s something that’s been weighing heavily on me for a while now."
    b "You’ve been nothing but kind to me, and you have an outsider’s perspective on this, and..."
    show kannika frown at sprite_highlight("kannika")
    b "I don’t really have anyone else I can talk to about this."
    show kannika -frown
    b "It would mean a lot to me if you could hear me out. Please."
    show kari blush at sprite_highlight("kari")
    mc "I would love to, Kannika."
    show kari -blush

    # Random drink
    $ choice = renpy.random.choice(['cattail', 'lavender', 'coffee', 'affogato']) 
    if choice == 'cattail': 
        nn "{i}You walk out from behind the counter and place a freshly-steeped cup of cattail citrus tea – it seemed right for the situation – in front of Kannika.{/i}" (cb_name="kari")
        show kari smile
        play sound "Dewdrop_SetGlass1.mp3" volume 0.7
        show drink bg zorder 2:
            align (0.5, 0.4)
        show cattail citrus zorder 3:
            align (0.5, 0.4)
        with dissolve
        pause 2.0
        hide cattail citrus with dissolve
        hide drink bg with dissolve
        n "{i}She looks at you with gratitude as you sit next to her and smile reassuringly.{/i}"
        show kari -smile
    elif choice == 'lavender': 
        nn "{i}You walk out from behind the counter and place a cup of humming lavender with honey – it seemed right for the situation – in front of Kannika.{/i}" (cb_name="kari")
        show kari smile
        play sound "Dewdrop_SetGlass1.mp3" volume 0.7
        show drink bg zorder 2:
            align (0.5, 0.4)
        show humming lavender zorder 3:
            align (0.5, 0.4)
        with dissolve
        pause 2.0
        hide humming lavender with dissolve
        hide drink bg with dissolve
        n "{i}She looks at you with gratitude as you sit next to her and smile reassuringly.{/i}"
        show kari -smile
    elif choice == 'coffee': 
        nn "{i}You walk out from behind the counter and place a hot cup of otterkish coffee – it seemed right for the situation – in front of Kannika.{/i}" (cb_name="kari")
        show kari smile
        play sound "Dewdrop_SetGlass1.mp3" volume 0.7
        show drink bg zorder 2:
            align (0.5, 0.4)
        show otterkish coffee zorder 3:
            align (0.5, 0.4)
        with dissolve
        pause 2.0
        hide otterkish coffee with dissolve
        hide drink bg with dissolve
        n "{i}She looks at you with gratitude as you sit next to her and smile reassuringly.{/i}"
        show kari -smile
    elif choice == 'affogato':
        nn "{i}You walk out from behind the counter and place an affogato al signo – it seemed right for the situation – in front of Kannika.{/i}" (cb_name="kari")
        show kari smile
        play sound "Dewdrop_SetGlass1.mp3" volume 0.7
        show drink bg zorder 2:
            align (0.5, 0.4)
        show affogato zorder 3:
            align (0.5, 0.4)
        with dissolve
        pause 2.0
        hide affogato with dissolve
        hide drink bg with dissolve
        n "{i}She looks at you with gratitude as you sit next to her and smile reassuringly.{/i}"
        show kari -smile
    
    mc "Whenever you're ready."
    play sound "Dewdrop_KannikaSigh.mp3" volume 0.7
    nn "{i}Kannika takes a deep breath and begins to speak.{/i}" (cb_name="kannika")

    # Cattail Citrus or no Cattail Citrus branch
    if not pickedcitrus:
        b "This question is a bit forward, but..."
        b "Why did you decide to open a traveling cafe?"
        window hide

        # Kari trauma menu
        menu:
            "(Tell the truth)":
                window show
                show kari sweatdrop at sprite_highlight("kari")
                mc "I… My parents and I had a bit of a disagreement."
                mc "Things were really tense and uncomfortable and I…"
                show kari gloom
                mc "I just had to get out of the house for a little bit."
                show kari frown
                mc "I felt like I couldn’t be myself. I couldn’t be my own person."
                mc "I was being buried alive under all these expectations and traditions and “shoulds” and “should-nots” and they just…"
                mc "They didn’t get it."
                mc "I know they love me, and they have my best interests at heart, but it was just… too much."
                mc "We all needed some space. Me {i}and{/i} them."
            "(Tell a partial truth)":
                window show
                show kari sparkle at sprite_highlight("kari")
                mc "I wanted to see the world."
                show kari -sparkle
                mc "My home – the PDRC, I mean – always felt a little… I dunno, stifling?"
                mc "I wanted to see what it was like in other places."
                mc "If it was the same, if it was worse… or if it was better."
                show kari smile
                mc "So far, it’s been nothing but better."
                show kari -smile
                b "How did you do it?"
                b "Your parents… Did they let you go, or did you have their blessing?"
                show kari sweatdrop
                mc "..."
                mc "My parents and I were actually having a bit of a disagreement."
                mc "We all needed a bit of space, and I had already been thinking about traveling for a while…"
                show kari -sweatdrop
            "(Lie)":
                window show
                show kari sparkle at sprite_highlight("kari")
                mc "It’s always been my dream!"
                mc "I get to make delicious drinks, see amazing sights…"
                mc "And I get to meet amazing people."
                show kari smile
                b "How did you do it?"
                b "How did you get from just having a vision to… to actually achieving it?"
                b "To being the person you wanted to be, in the world you wanted to make?"
                mc "Oh, it’s simple, I just…"
                show kari sweatdrop
                mc "..."
                mc "It’s actually not that simple."
                mc "Ever since I was a kit, I knew who I wanted to be, but…"
                show kari gloom
                mc "My parents had their own idea of who I was supposed to be."
                show kari frown
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
                show kari sparkle at sprite_highlight("kari")
                mc "I love the Dewdrop Cafe!"
                mc "Getting to travel and see the world, getting to meet amazing people and make drinks for them…"
                mc "It’s a dream come true."
                show kari smile
                mc "And it’s not like I’ll be gone forever."
                mc "Once they’ve had enough time to calm down, I’ll come back with all these amazing stories to share…"
                mc "They’ll understand."
                mc "Things will go back to the way they were."
                show kari -smile
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
    show kari exclamation at sprite_highlight("kari")
    mc "What do you mean? Kannika, what’s going on?"
    show kari surprised
    b "Would you prefer the short version or the long version?"

    # Short or long version menu
    window hide
    menu longorshort:
        "The long version.":
            call longversion from _call_longversion
        "The short version.":
            window show
            mc "You seem pretty stressed, so let’s get straight to the important stuff."
            b "Very well."
            show kannika frown at sprite_highlight("kannika")
            b "In short, I am all but betrothed to a man whom I have never spoken to."
            show kari exclamation
            $ alreadysurprised = True
            b "A man chosen not by any input of mine, or even from my mother, but simply for his fighting skill."
            show kari surprised
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
                    show kari angry
                    mc "And who is this {i}guy{/i} you’re supposed to get engaged with?"
                    show kari surprised
                    b "Sorry, this is my first time ever really… explaining this situation I’m in."
                    b "Where should I even begin?"
                    call longversion from _call_longversion_1
                "I'm so sorry.":
                    window show
                    show kari frown
                    mc "Is there anything you can do? Any way to stop it?"
    mc "What about your mom? Have you talked to her about this?"
    b "My mother and I have spoken at length on this subject, and she has made her position clear."
    b "The legitimacy of her reign depends on the support of the nobility and the High Elders, and by extension the observance of traditions such as this one."

    # Check to see if Kannika knows Kari's familial ties to the PDRC's government
    if askedaboutgovernment:
        b "You mentioned your father worked for your government. I’m sure you know as well as I do what happens when other responsibilities take priority over parenting."
        b "That’s how my mother is."

    b "She is a ruler first and foremost. Motherhood is a distant second."

    # High elders menu code
    window hide
    $ highelderstree = {"elders": False, "marry": False}
    menu highelders:
        "Real quick, who are these “High Elders?”" if not highelderstree["elders"]:
            $ highelderstree["elders"] = True
            window show
            show kari sweatdrop
            mc "How is your mother the queen if even she has people who can tell her what to do?"
            show kari frown
            b "The High Elders are a council of nine immortal water dragons. They are the progenitors of our people, and the creators of this country."
            b "Their timeless wisdom and millennia of observation is supposed to help guide our queens during their rule and keep the kingdom prosperous…"
            b "…But what that really means is they insist we cling to the old rules and traditions that {i}they{/i} originally put in place."
            show kari sweatdrop
            mc "I can’t say I’ve met many dragons before, but I think I get the gist."
            show kari frown
            window hide
            jump highelders
        "What about the guy you’re going to marry?" if not highelderstree["marry"]:
            $ highelderstree["marry"] = True
            window show
            mc "Could you convince him to call it off after he wins?"
            mc "Actually, wait, do you even know who it’s going to be?"
            show kannika gloom
            b "I do. There are only a handful of bouts left in the tournament, and the victor is all but certain."
            show kannika frown
            b "But it’s not about him, just as it’s not about me. It’s about the balance of power between the nobility, the monarchy, and the High Elders."
            b "Not that I can imagine any of the contestants objecting to this tradition."
            window hide
            jump highelders
        "Maybe we can convince your mom to listen to you.":
            window show
            show kari sweatdrop
            mc "Sure, she’s a queen, but she’s still your mom."
            show kari frown
            mc "If you can find a time to just sit down with her and talk it out, heart-to-heart, I’m sure she’d understand where you’re coming from."
            show kannika angry
            b "But I {i}have.{/i} I’ve {i}tried.{/i}"
            show kannika gloom
            b "It’s not that she doesn’t understand me. It’s that she won’t listen to me."
            show kannika frown
            b "To her, I’m still a naive little girl who doesn’t understand how the world works."
            b "And it would be unthinkable for a naive little girl to dare to contradict the queen."
            b "So I hope you can understand why I have such a difficult time believing that another talk is all I need."
            mc "But you can’t just do nothing, right?"
            mc "I really do think you should try to explain how you’re feeling to her, just one more time."
            mc "Because if you can’t even talk to her…"
        "I think your mom’s just trying to look out for you.":
            window show
            show kari -frown
            mc "She might be having a hard time showing it, but I’m sure she has your best interests at heart."
            show kari sparkle
            mc "Yeah. Yeah! She’s just looking out for you in the long run."
            show kari frown
            show kannika angry
            b "{i}Looking out for me?{/i}"
            b "Maybe she’s looking out for Kannika, the future queen."
            b "But in doing so, she is turning a blind eye to the current Kannika."
            b "To {i}me.{/i}"
            show kannika frown
            b "Just as she has been doing my entire life. Her kingdom takes priority. Her daughter can wait."
            b "She’s shown me that, time and time again."
            b "So it’s very difficult for me to share your optimism about her."
            show kari sweatdrop
            mc "She probably just has a different perspective than you."
            mc "I’m sure she cares about you."
            mc "You need to trust her, because if you don’t…"
            show kari frown
    
    # Kannika wants to run away from home
    mc "What else is there to do? What else {i}can{/i} you do?"
    b "I can leave."
    show kari exclamation
    b "Just like you did, Kari."
    show kari surprised
    nn "{i}You freeze in shock. You had a sneaking suspicion this was where the conversation was headed, but to hear her say it out loud…{/i}" (cb_name="kari")
    nn "{i}When she says those words, a torrent of memories and emotions wash over you.{/i}" (cb_name="kari")
    show kari gloom
    nn "{i}The anguish and anxiety that consumed you in the days before you made the choice to leave.{/i}" (cb_name="kari")
    show kari angry
    nn "{i}The simultaneous frustration and catharsis as you wrote that farewell note to your parents.{/i}" (cb_name="kari")
    show kari sweatdrop
    nn "{i}The paranoia as you stole a magic briefcase from your dad’s collection of confiscated foreign items.{/i}" (cb_name="kari")
    show kari smile
    nn "{i}The bittersweet uncertainty of your first night in the cold, sleeping under the stars.{/i}" (cb_name="kari")
    show kari frown

    # Kari warns Kannika menu
    window hide
    menu:
        "Are you serious?":
            window show
            mc "That’s a big decision to make."
            b "I know. I’ve been thinking about it a lot."
            b "It’s what you did, right? When you had no other option, you left."
            b "And look where you are now."
            show kari sweatdrop
            mc "Kannika… It’s not that simple."
            show kannika angry
            b "What do you mean? It {i}is{/i} that simple."
            show kannika frown
            mc "It’s not."
            mc "Where will you go? How will you get by?"
            mc "Will you go back? Or are you leaving forever?"
            mc "Are you okay with never seeing your mom again?"
            show kari frown
            mc "I know when I talked about it, I made it sound simple."
            mc "But it wasn’t."
            mc "It wasn’t easy to make the decision, and it wasn’t easy to make it to the point I’m at now."
            show kannika angry
            b "I can’t believe this."
            b "I thought you’d support my choice in this."
            show kari surprised
            mc "Kannika, I support {i}you.{/i}"
            mc "I just want to make sure you know what making this choice will mean."
            b "I know that staying will change nothing."
            mc "Right, but just packing up and leaving is…"
            b "Is what, Kari? Not that simple?"
            b "Because it seems pretty simple to me."
        "There has to be another option.":
            window show
            mc "We can figure something out. Together."
            show kannika angry
            b "Another option?"
            b "I don’t {i}have{/i} any other options."
            b "My mother won’t do anything. The High Elders would never make an exception. The nobility won’t care."
            b "The only two people who {i}do{/i} care, it seems, are you and me."
            b "Your only choice was to leave. It’s the same for me."
            show kari surprised
            mc "There’s gotta be {i}something{/i} you can do."
            b "Like {i}what,{/i} Kari?"

            # Kari ideas menu
            window hide
            $ ideastree = {"mom": False, "nobility": False, "rebellion": False, "pickedany": False}
            menu ideas:
                "We could talk to your mom together." if not ideastree["mom"]:
                    $ ideastree["mom"] = True
                    $ ideastree["pickedany"] = True
                    window show
                    mc "Maybe if I’m there to help explain, she’ll understand how much this means to you."
                    show kari sweatdrop
                    b "You would never be granted an audience with her! I’m not even supposed to be coming out to see you!"
                    b "I keep telling you, there’s nothing we can do to make her change her mind."
                    show kari frown
                    window hide
                    jump ideas
                "What if you got the nobility to support you?" if not ideastree["nobility"]:
                    $ ideastree["nobility"] = True
                    $ ideastree["pickedany"] = True
                    window show
                    mc "If they’re this interested in gaining power and influence, maybe you could offer them something for when you do take the throne."
                    show kannika exclamation
                    show kari sweatdrop
                    b "Take the throne?!"
                    show kannika angry
                    b "Kari, this place is {i}suffocating me.{/i} I can’t stand it here."
                    b "And who knows how long it would take to convince the noble houses to do something? Weeks? Months?"
                    b "I only have days."
                    show kari frown
                    window hide
                    jump ideas
                "Start a rebellion." if not ideastree["rebellion"]:
                    $ ideastree["rebellion"] = True
                    $ ideastree["pickedany"] = True
                    window show
                    mc "The system sucks, right? Just throw out the system."
                    show kannika exclamation
                    show kari sweatdrop
                    b "Are you even taking this seriously?"
                    show kannika angry
                    b "My only ounce of authority comes from my mother and the fact that the High Elders approve of her rule."
                    b "There is nothing I can do to change the way things are."
                    show kari frown
                    window hide
                    jump ideas
                "I don’t know." if ideastree["pickedany"]:
                    window show
                    mc "I just…"
                    show kari gloom
                    mc "Clearly you can’t stay."
                    show kari frown
                    mc "But you can’t just leave."
                    mc "There’s gotta be another way…"
        "Don’t. You’d be making a big mistake.":
            window show
            mc "What about your mom? Are you just going to leave her behind?"
            b "Why shouldn’t I? She hasn’t been a mother to me. Why should I need to be a daughter for her?"
            show kari sweatdrop
            mc "Kannika, please. Listen to what you’re saying."
            mc "You only get one family. Are you willing to throw all that away right now?"
            show kannika angry
            b "I can’t believe this."
            b "Out of all the people who would try and convince me to stay in this… this {i}cage…{/i}"
            mc "I know it’s hard, Kannika. I know."
            mc "But just because it’s worked out for me so far doesn’t mean it’s what you should do, too."
            mc "There are people here who are depending on you. The people of this kingdom, but also your mom."
            show kannika speechless
            b "If this turns into a lecture about responsibility, I am going to lose my mind."
            show kari exclamation
            mc "No, what I’m trying to say is that when I decided to leave home, I didn’t have to worry about an entire nation falling into chaos when I left!"
            show kari frown
            show kannika angry
            b "I’m just a symbol. A figurehead. If I’m not there, the High Elders will find someone else to sit on the throne."
            mc "But your mom–"
            b "I don’t care."

    # Kannika is NOT having it
    show kannika angry
    show kari exclamation
    play sound "Dewdrop_Clatter.mp3" volume 0.7
    nn "{i}With a clatter, Kannika stands up and pushes away from the counter. Her skin is flushed, brow furrowed and fins flared, and her shoulders are hunched as if bracing for a blow.{/i}" (cb_name="kannika")
    show kari frown
    nn "{i}She meets your eyes for just a moment, but in those orange pools you see frustration, betrayal, and a hint of desperation. The princess turns away from you, hugging her arms around herself.{/i}" (cb_name="kannika")
    show kannika:
        xzoom -1
    b "This is going nowhere."
    b "I had hoped coming here would bring me some clarity."
    b "Or, at the very least, I would be reassured that I’m not alone."
    mc "Kannika, I–"
    b "Thank you for the drink."
    window hide

    # Kannika leaves the scene
    show kannika at offscreenleft
    with easeoutleft
    pause 0.25
    show kari exclamation at center
    with move
    play sound "Dewdrop_Splash.mp3" volume 0.7
    window show
    n "{i}Kannika storms off and dives into the water. Luan spares you only a quick glance before following behind her.{/i}"
    play sound "Dewdrop_Splash.mp3" volume 0.7
    pause 0.5
    show kari frown
    n "{i}You are alone.{/i}"

    # Fade out
    scene black
    with fade

    # Kari depression menu
    window hide
    menu:
        "(Close up early)":
            window show
            n "{i}Almost in a daze, you go about closing up the Dewdrop Cafe for the day.{/i}"
            n "{i}Your mind lingers on the conversation you just had, replaying those moments over and over.{/i}"
        "(Go about the rest of your day as normal)":
            window show
            n "{i}You pull yourself together and keep on going. You have a cafe to run, after all.{/i}"
            n "{i}Eventually customers return, and soon you lose yourself in the comfortable chaos of taking orders and making drinks.{/i}"
            n "{i}But in the slower moments between rushes, you catch your mind lingering on the conversation with Kannika.{/i}"

    # Kari thinks about what she's done
    n "{i}You keep seeing the expression Kannika had on her face before she left. The betrayal.{/i}"
    n "{i}Why couldn’t you just support her decision to run away? It’s what you did, isn’t it?{/i}"
    n "{i}You think about your family. Your mom, your dad. Their smiling faces at the door, welcoming you home after all these years.{/i}"
    n "{i}Everything going back to normal.{/i}"
    n "{i}You’ve never even considered the possibility that things can’t go back to normal. That the bonds of family, once broken, might not ever heal.{/i}"
    n "{i}Kannika likely hasn’t thought about it like that. You were just looking out for her.{/i}"
    n "{i}She’ll understand you had the best intentions.{/i}"
    n "{i}You hope she’ll understand.{/i}"
    n "{i}For now…{/i}"
    n "{i}You are alone.{/i}"
    window hide

    jump chapter4

label longversion:
    window show
    mc "Just take a deep breath and start from the beginning."
    b "Very well."
    b "There are a number of festivals, ceremonies, and rituals that I, as an heiress, am obligated to participate in."
    b "One such ritual is the Dance of Ribbons, a tournament that will conclude at the end of the week."
    show kannika frown
    b "The victor – the most capable warrior among the champions of the noble houses – is to become my husband, regardless of my wishes otherwise."

    # Check to see if Kari has already been surprised about the marriage
    if alreadysurprised == False:
        show kari exclamation

    b "Yet another of my few scraps of freedom stripped away in the name of tradition."
    show kari surprised

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
            show kari exclamation
            mc "That’s a lot more violent than I expected."
            show kari surprised
            b "They used to be to-the-death, but these days the matches end when one fighter yields."
            b "These sorts of competitions are central to many of our oldest traditions, and skill in combat is expected of anyone in the nobility."
            mc "Does that mean you can fight too?"
            b "My mother had me trained in wrestling, tail-boxing, and dueling spears."
            mc "What if you joined the tournament as your own champion? Could that work?"
            show kannika gloom
            b "As if I would ever be allowed to fight for the right to make any sort of decision about my own life."
            show kannika frown
            window hide
            jump anything
        "So the prize is that the winner gets to marry you?" if not anythingtree["prize"]:
            $ anythingtree["prize"] = True
            window show
            show kannika sweatdrop
            b "As with so many things in this kingdom, it’s not quite that simple."
            show kannika frown
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
            show kannika angry
            b "Kari, I don’t even have the dignity of deciding what I eat for breakfast."
            show kannika gloom
            b "These traditions have been like this for generations. Trying to fight them would be like trying to fight the tides themselves."
            show kannika frown
            window hide
            jump anything
        "Isn’t there anything you can do?":
            show kari frown
            window show
    return