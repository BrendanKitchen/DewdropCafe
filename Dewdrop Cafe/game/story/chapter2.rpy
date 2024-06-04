#   "{i}{/i}"
label chapter2: 
    $ persistent.ch2 = True

    # Play music
    play music "Pas de Deuxdrop.mp3" volume 0.6

    # Chapter Card Intro
    window hide
    $ quick_menu = False
    scene black bg
    show ch overlay
    show ch2:
        align (0.5, 0.5)
    with fade
    pause 2
    hide ch2
    hide ch overlay
    with fade
    $ quick_menu = True

    # Intro - Kari's finishing up the day at the cafe
    pause 0.25
    window show
    n "{i}The following day...{/i}"
    window hide
    pause 0.5
    show night bg
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

    # Conditional dialogue based off of helping Kannika in chapter 1
    if karihelpedkannika == True:
        n "{i}It doesn’t take long before you’re all tidied up. You glance over the front of the shop, one last check before you go into the back and take inventory for tomorrow.{/i}"
        n "{i}As you pick your way through the stacks of boxes, you wonder when you’ll have the time to go to a market…{/i}"
    else:
        n "{i}Out of the corner of your eye, you see that your counter’s suffered a particularly stubborn stain. Scrubbing it with a rag isn’t enough…{/i}"
        n "{i}Maybe you have some cleaning solution left over. You go into the back storage and start digging through boxes, trying to remember where you put it…{/i}"
    
    # More splashes
    window hide
    pause 0.25
    play sound "Dewdrop_DoubleSplash.mp3" volume 0.7
    pause 0.5
    window show
    n "{i}A pair of splashes announces the arrival of two more customers. It’s only moments before you hear the ring of the counter bell.{/i}"
    show kari -smile
    play sound "Dewdrop_Bell.mp3" 
    show kari exclamation
    bquestionmark "Excuse me, are you still open?"
    show kari -surprised
    show kari smile
    show kari:
        xzoom 1.0
    mc "Coming! What can I get for-"

    # KANNIKA AND LUAN ENTER THE SCENE
    show kari at right, sprite_highlight("kari")
    with move
    show kannika neutral zorder 1 at sprite_highlight("kannika"):
        xzoom 1.0
        align (0.2, 0.5)
    with easeinleft
    show luan neutral zorder 2 at sprite_highlight("luan"):
        xzoom 1.0
        align (-0.1, 1.0)
    with easeinleft
    show kari surprised
    mc "Oh!"
    show kari -surprised

    # Kari decides whether or not to reveal that she knows Kannika
    window hide
    menu:
        "…What can I get for you two tonight?":
            window show
            show kannika smile at sprite_highlight("kannika")
            nn "{i}The woman flashes you a quick smile.{/i}" (cb_name="kannika")
            show luan glance_down at sprite_highlight("luan")
            g "..."
            show luan -glance_down
            show kannika -smile
        "You came back!":
            window show
            show kannika smile at sprite_highlight("kannika")
            show luan angry at sprite_highlight("luan")
            nn "{i}The woman smiles at you. The guard’s jaw clenches as he stares coldly at you, but he closes his eyes and takes a deep breath before he speaks.{/i}" (cb_name=["kannika", "luan"])
            show luan -angry
            show kannika -smile
        "Uh, hello, strange woman whom I have never met before.":
            window show
            play sound "Dewdrop_KannikaClearThroat.mp3" volume 0.7
            show kannika sweatdrop at sprite_highlight("kannika")
            nn "{i}The woman coughs into her hand.{/i}" (cb_name="kannika")
            play sound "Dewdrop_LuanSigh.mp3" volume 0.7
            show luan frown at sprite_highlight("luan")
            nn "{i}The guard just sighs, a look of mild disappointment on his face.{/i}" (cb_name="luan")
            show luan -frown
            show kannika -sweatdrop
        "Officer, I think I found the person you're looking for.":
            window show
            show kannika speechless at sprite_highlight("kannika")
            nn "{i}The woman looks at you with an expression of mock outrage. The guard stares flatly at you, unamused.{/i}" (cb_name=["kannika", "luan"])
            show kannika -speechless
    
    # Drink peddler?? Luan is a meanie ;(
    g "Drink-peddler. My lady says she misplaced her parasol somewhere around here last night."
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
    show luan neutral
    show luan glance_down
    nn "{i}Luan looks you up and down. After a moment, he gives you a very shallow bow – more of a nod, really – and moves back.{/i}" (cb_name="luan")
    show luan -glance_down
    show kannika -angry

    # Luan leaves 
    window hide
    show luan neutral at offscreenleft
    with easeoutleft
    play sound "Dewdrop_Slither.mp3" volume 0.7

    # Adjust Kannika placement

    show kannika neutral at left, sprite_highlight("kannika")
    with MoveTransition(0.75)

    # Princess discussion
    $ princesstree = {"sorry": False, "wait": False, "foreigner": False}
    window show
    princess "My apologies. Pancake is... very diligent. He means no personal offense."
    window hide
    menu princessdiscussion:
        "Uh huh. Sorry, did he call you {i}princess{/i}??" if not princesstree["sorry"]:
            window show
            $ princesstree["sorry"] = True
            princess "Yes. He did."
            mc "...And?"
            princess "And what?"
            show kari surprised
            mc "Are you? An actual princess, I mean."
            princess "Yes. I am."
            mc "..."
            princess "..."
            show kari smile
            mc "Cool!"
            show kari -smile
            window hide
            jump princessdiscussion
        "Wait, is his name Pancake or Luan?" if not princesstree["wait"]:
            window show
            $ princesstree["wait"] = True
            princess "It's Luan. Pancake is a nickname I gave him when I was a small child."
            princess "You can call him Pancake too, if you want."
            princess "I'm sure he wouldn't mind."
            show kari speechless
            mc "If you say so..."
            show kari -speechless
            window hide
            jump princessdiscussion
        "Oh, the 'foreigner' stuff? It's okay, I get it." if not princesstree["foreigner"]:
            window show
            $ princesstree["foreigner"] = True
            mc "Honestly, I kinda expected him to be a little more intense."
            show kannika exclamation
            princess "...More intense?"
            mc "Yeah. He didn't ask for my identification papers. He didn’t accuse me of being an enemy of the state."
            show kari smile
            mc "He didn’t even search my cafe for any seditious writings or materials that would threaten the security or moral character of the nation."
            show kari sunglasses
            mc "Not that I have anything like that in here."
            mc "Nope. No siree."
            show kari smile
            show kannika speechless
            princess "I'm not even going to try to unpack all of that right now."
            show kannika -speechless
            show kari -smile
            window hide
            jump princessdiscussion
        "You know what, let's just start over.":
            window show
            show kari smile
            mc "Hi! I'm Kari. Welcome to the Dewdrop Cafe!"
            show kannika smile
            princess "It's wonderful to meet you, Kari. My name is Kannika."
            mc "Princess Kannika?"
            show kannika blush
            b "Please, just Kannika."
            show kannika -blush
            show kari -smile

    # Parasol discussion
    show kari exclamation
    mc "Oh! Right! Your parasol..."
    show kari surprised
    mc "Wait a minute. You have a parasol right now."
    b "..."
    show kannika sweatdrop
    b "This is my backup parasol."
    show kari speechless
    mc "Uh huh..."
    show kari -speechless
    show kannika -sweatdrop
    mc "Anyways, can I get you anything to drink?"

    # Kari chooses whether or not to call Luan "Pancake"
    window hide
    menu:
        "Oh, and what about you, Luan? Would you like a drink?":
            window hide
            pause 0.25
            show luan neutral zorder 2:
                xzoom 1.0
                align (-0.1, 1.0)
            with MoveTransition(0.75)
            pause 0.25
            window show
            lu "No, thank you."
            window hide
            show luan neutral at offscreenleft
            with MoveTransition(0.75)
            pause 0.25
            window show
        "Oh, and what about you, Pancake? Would you like a drink?":
            window hide
            show luan neutral zorder 2:
                xzoom 1.0
                align (-0.1, 1.0)
            with MoveTransition(0.75)
            pause 0.25
            window show
            show luan glance_down
            lu "..."
            show luan -glance_down
            lu "No."

            window hide
            show luan neutral at offscreenleft
            with MoveTransition(0.75)
            pause 0.25
            window show

    # Check which drink player picked during scene 1
    if pickedcitrus == False and pickedlavender == False and pickedjelly == False:
        nn "Kannika puts a hand thoughtfully to her chin and peruses the menu." (cb_name="kannika")
        b "Let's see... I've already tried the..."
        window hide
        menu:
            "Cattail citrus.":
                $ pickedcitrus = True
                window show
                b "Yes!"
                # Next line: "I couldn't stop thinking about the tea you gave me last night."
            "Humming lavender.":
                $ pickedlavender = True
                window show
                b "Yes."
                # Next line: "The tea you gave me last night was quite nice."
            "Moon jelly tea.":
                $ pickedjelly = True
                window show
                b "Hmm..."
                # Next line: "What other kinds of drinks do you serve?"
    if pickedcitrus:
        call cattailcitrustree from _call_cattailcitrustree
    if pickedlavender:
        call humminglavendertree from _call_humminglavendertree
    if pickedjelly:
        call moonjellytree from _call_moonjellytree

    play sound "Dewdrop_Giggles.mp3" volume 0.7
    n "{i}The moon crawls higher in the sky. The night sounds of the swamp have returned in full force, though they now must compete with the lively chatter and laughter emanating from the Dewdrop Cafe.{/i}"
    n "{i}Eventually, Luan clears his throat and steps (or rather, slithers) forward.{/i}"

    # Luan enters the scene
    window hide
    show night bg
    show kannika neutral zorder 1 at sprite_highlight("kannika"):
        align (0.2, 0.5)
    show kari neutral zorder 1 at sprite_highlight("kari"), right
    with fade
    play sound "Dewdrop_Slither.mp3" volume 0.7
    show luan neutral zorder 2 at sprite_highlight("luan"):
        xzoom 1
        align (-0.1, 1.0)
    with easeinleft
    pause 1.25
    play sound "Dewdrop_LuanThroatClear.mp3" volume 0.9
    pause 0.75
    window show

    # Luan and Kannika chat
    lu "Your highness. We should return to the castle."
    b "In a bit, Pancake."
    lu "Princess Kannika. It is late. I believe we should be going on our way."
    b "In a bit, {i}Luan.{/i} Mother hardly even notices I’m gone – she won’t care if I’m an hour later than usual."
    show luan angry at sprite_highlight("luan")
    nn "{i}Luan’s expression darkens. His hands clench into fists, and his fins rise and flare out slightly.{/i}" (cb_name="luan")
    play sound "Dewdrop_LuanSigh.mp3" volume 0.7
    nn "{i}He closes his eyes and takes a measured breath, inhaling through his nose and exhaling out his mouth.{/i}" (cb_name="luan")
    show luan -angry
    lu "Princess. Her Majesty’s patience, while generous, is not infinite."
    lu "The tournament is coming to an end. There are only a handful of bouts remaining."
    lu "Soon you will not have time for these frivolous outings anymore."
    lu "I do not think I need to remind you of the responsibilities you have."
    lu "Not just to your mother, but to your people."
    lu "And to the High Elders."
    show kannika angry at sprite_highlight("kannika")
    nn "{i}The exasperation on Kannika’s face curdles into barely-repressed rage. It passes in an instant, vanishing behind a practiced mask of pleasant ambivalence.{/i}" (cb_name="kannika")
    show kannika -angry
    nn "{i}She sets down her cup and smoothly rises from her seat.{/i}" (cb_name="kannika")
    b "Your point is made, Pancake. We shall take our leave."
    b "Thank you, Kari."
    show kannika smile
    nn "{i}The mask cracks as she smiles at you. You can see a deep and genuine gratitude in her eyes, and you wonder how long it’s been since she last talked like this to another person.{/i}" (cb_name="kannika")
    show kannika -smile

    # Kari response menu
    window hide
    menu:
        "Of course!":
            window show
            mc "Hope I see you again soon!"
            mc "Oh, uh, you too..."

            # Luan or Pancake menu part 2
            window hide
            menu:
                "...Luan.":
                    window show
                    lu "..."
                "...Pancake.":
                    window show
                    lu "..."

        "Wish you could stay longer, but you should probably get going.":
            window show
            mc "I still need to clean up and prep for tomorrow..."
            b "I appreciate you keeping the shop open for me."
            b "It means a lot."
        "Thank you too, Kannika.":
            window show
            show kannika smile
            nn "{i}She beams at you. As she turns to leave, her movements seem to have a little more pep.{/i}" (cb_name="kannika")
            show kannika -smile
    nn "{i}Luan holds out an arm as Kannika lightly rests a hand on it. As he begins to escort her away, she turns to look over her shoulder at you and the cafe, catching one last glimpse before she disappears into the night.{/i}" (cb_name=["kannika", "luan"])

    # Kannika turns to luan then back to kari
    window hide
    show kannika neutral:
        xzoom -1
    pause 0.5
    show kannika neutral:
        xzoom 1
    pause 0.5

    # Kannika and Luan leave
    show luan neutral:
        xzoom -1
    pause 0.25
    show kannika neutral:
        xzoom -1
    pause 0.25
    show luan neutral at offscreenleft
    with MoveTransition(0.75)
    pause 0.25
    show kannika neutral at offscreenleft
    with MoveTransition(0.75)

    # Outro
    window show
    n "{i}You slump forward, leaning against the counter, mind reeling with everything that’s happened in the past two days. You think about the stories you told Kannika, and wonder how you’ll ever manage to sum up your time in the Naga Kingdom.{/i}"
    n "{i}A princess! A real, actual princess was sitting at your humble little cafe, drinking the tea you made for her.{/i}"
    n "{i}Still buzzing with a thousand different trains of thought, you absentmindedly go about cleaning the counter and getting ready to wash the cups. You step outside to put the chairs away – and stop dead in your tracks.{/i}"
    n "{i}Kannika’s parasol is still resting against the front of the counter.{/i}"

    # Forgotten parasol part 2 menu
    window hide
    menu:
        "Again?!":
            window show
            play sound "Dewdrop_KariLaugh.mp3" volume 0.7
            n "{i}You chuckle to yourself at the forgetfulness of this princess. You’ll just have to hold onto the parasol until you see her again.{/i}"
            n "{i}Hopefully, you won’t have to wait too long...{/i}"
        "She must’ve really been in a hurry...":
            window show
            n "{i}Your thoughts turn to Kannika’s departure. What was Luan talking about? What sort of tournament? And surely Kannika doesn’t see a visit to your cafe as frivolous, right?{/i}"
            n "{i}Hopefully she’ll have time to visit at least once more...{/i}"
        "Wait a minute… Was that on purpose?":
            window show
            mc "No, it can't be..."
            mc "...unless?..."
            n "{i}You shake your head and clap your hands on your cheeks. Can’t think about that now. You have things to do.{/i}"
            n "{i}Tomorrow’s likely going to be even busier than today, and you have to give it your all for the sake of your customers.{/i}"
            n "{i}Maybe Kannika will be among them...{/i}"

    # Kari takes center stage
    window hide
    show kari at center
    with MoveTransition(0.75)
    window show
    mc "..."
    window hide
    pause 0.5

    scene black
    with fade
    # hide kari with dissolve 
    # hide day bg with Fade(0.5, 0.5, 0.5)

    jump chapter3
    
# Cattail citrus branching dialogue
label cattailcitrustree:

    # Intro
    b "I couldn't stop thinking about the tea you gave me last night."
    show kannika sparkle
    b "Could I have that again? Please?"
    show kari blush
    mc "Oh, I'm so glad you liked it!"
    mc "One cattail citrus tea, coming right up."
    show kannika blush
    b "I'd never tasted anything quite like it."
    show kannika smile
    show kari smile
    b "I was quite sad that I wasn't able to finish my cup from last night..."
    b "It was delicious."
    mc "If you think this is good, you should try the one my mom makes."
    mc "I used to ask her for it all the time as a kit. Probably drove her crazy..."
    show kannika frown
    show kari -smile
    b "..."
    nn "{i}As you work on putting together another cattail citrus tea, a flash of melancholy crosses the naga princess’ face. She opens her mouth as if to say something, but stops herself, instead looking out into the night.{/i}" (cb_name="kannika")
    nn "{i}Her scales and eyes shine in the light from your cafe, glimmering and iridescent.{/i}" (cb_name="kannika")
    show kannika -frown

    # Opening of discussion with Kannika about life
    window hide
    menu:
        "What about you? What’s your favorite childhood drink?":
            window show
            b "Nothing as good as what you made for me last night."
            b "Most naga drinks are... well, not quite the same as the ones you have on land."
            mc "You know, I was wondering about that."
            b "The ocean isn't very conducive to tea-making, sadly."
            b "Most of our finer traditional drinks are brines or layered oil jiggers."
            show kari exclamation
            mc "Did you say 'layered oil??'"
            show kari surprised
            b "Yes. We layer different kinds of oil - infused with other flavors - in a sort of inverted shot glass. It looks pretty, but actually drinking it..."
            show kannika speechless
            b "Let's just say I much prefer your tea."
            show kari smile
            show kannika -speechless
            mc "Aw, I'm glad you like it so much!"
            n "{i}Humming to yourself, you put the finishing touches on the cattail citrus and place the softly steaming glass in front of Kannika. {/i}"

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

            # Show Cattail Citrus
            show drink bg:
                align (0.5, 0.4)
            show cattail citrus zorder 3:
                align (0.5, 0.4)
            with dissolve

            # Kannika enjoys drink
            show kannika sparkle
            window show
            nn "{i}Her face immediately lights up as she blows on it before sipping delicately.{/i}" (cb_name="kannika")
            window hide
            pause 0.25
            play sound "Dewdrop_Sip.mp3" volume 0.75
            pause 1.0
            hide cattail citrus
            hide drink bg
            with dissolve
            show kannika -sparkle

            window show
            show kari -smile at sprite_highlight("kari")
            mc "So were {i}all{/i} of your meals prepared by chefs? Your mom never made anything for you?"
            b "Such is the way of nobility, I'm afraid."
            b "Besides, my mother is much too busy to do anything as nice as that."
            mc "I take it the two of you aren’t on the best of terms, then?"
            b "…not as such, no."
            show kari frown
            mc "Sorry. I know how tough that can be."
            b "It’s alright."
            show kannika frown
            b "We just… disagree on how some things are, and how some things should be."
            window hide

            # Discussing Kannika and her mom menu
            menu:
                #"At the end of the day, " cut
                "All that matters is that she loves you, right?":
                    window show
                    mc "That’s what parents are for."
                    mc "At least, that’s what they should be for."
                    b "I… Yes, you’re right."
                    b "Our disagreements don’t revolve around purely personal issues, however."
                    b "There’s not much room for any motherly affection to factor in when it comes to royal tradition."
                #"Sometimes it can be hard to see, " cut
                "I’m sure she has your best interests at heart.":
                    window show
                    mc "Sure, she’s a queen, but she’s also your mom. That’s gotta count for something, right?"
                    b "Usually, it would."
                    b "However, our most recent disagreements aren’t quite as… domestic."
                    b "I’m not just fighting her, but generations of royal tradition as well."
                #"Hold on. " cut
                "This isn’t, like, disagreements over government policies, right?":
                    window show
                    mc "Er, I guess they would be “royal decrees” here instead."
                    b "Somewhat, I suppose you could say."
                    b "Although I must admit that I have a personal issue with an admittedly impersonal tradition."

            # Kari consoles Kannika menu
            window hide
            menu:
                "Eesh, that’s tough.":
                    window show
                    "Kannika stares flatly at you. Her eyes flit across your face, seemingly searching for something."
                    play sound "Dewdrop_KannikaSigh.mp3"
                    "Then she sighs and slumps forward, elbows on the counter."
                    b "I guess this isn’t exactly something you can relate to after all…"
                    mc "No, really."
                    mc "That sort of thing can be really difficult to deal with."
                "I know exactly what you mean.":
                    window show
                    b "It’s okay if you don’t. I’m really just venting."
                    mc "No, I’m serious."
                    mc "I was in a really similar situation at one point."
            mc "It’s kind of the whole reason I started traveling in the first place."
            mc "Backwards cultural norms, stuffy expectations…"
            mc "I couldn’t stand it."
            mc "And my parents… well, they were really just trying to protect me."
            mc "I’m sure they’ll understand my side of things once I go back home."
            mc "But for now, I’m just taking a little break from all of that."
            b "..."
            show kannika -frown
            b "What was your home like?"
            b "My knowledge of the purrson nation is only superficial."
            b "The Purrsons’ Democratic Republic of Catistan, yes?"
            show kari -frown
            mc "Most people just call it the PDRC."
            mc "But yeah, sure, I can tell you about it."

            # PDRC menu
            window hide
            $ pdrctree = {"city": False, "geography": False, "government": False}
            menu pdrc:
                "(Focus on your city)" if not pdrctree["city"]:
                    $ pdrctree["city"] = True
                    window show
                    mc "It’s super modernized. Almost every major city has plumbing, and the streets are all paved."
                    mc "The market districts are fully patrolled, so there’s no crime."
                    show kari sparkle
                    mc "I wish I could show you the fish markets, they’re so fun to shop in!"
                    show kari smile
                    mc "Oh, and the city I grew up in has the biggest printing house in the country."
                    mc "Newspapers, pamphlets, posters, they make all sorts of things there. Lots of government materials, too."
                    mc "My dad did an inspection there once, and he brought back one of the little letter stamps for me."
                    mc "I think I still have it somewhere in here…"
                    show kari -smile
                    window hide
                    jump pdrc
                "(Focus on the geography)" if not pdrctree["geography"]:
                    $ pdrctree["geography"] = True
                    window show
                    mc "I grew up on the coast, so there were lots of ships going in and out all the time."
                    mc "We had this amazing view of the ocean from our house."
                    show kari blush
                    mc "When I was a kit, my dad would make little paper warships for me to stick to the window and pretend like they were actual ships on the bay."
                    show kari -blush
                    mc "There are a lot of mountains, too. They protect the PDRC from its enemies."
                    mc "Apparently there used to be big forests, but they got cut down to make room for more factories."
                    window hide
                    jump pdrc
                "(Focus on the government)" if not pdrctree["government"]:
                    $ pdrctree["government"] = True
                    $ askedaboutgovernment = True
                    window show
                    mc "My dad works for the Committee for Cultural Autonomy and Technology. Basically, his job is making sure nothing bad is being smuggled into the country, particularly when it comes to new inventions from other nations."
                    mc "Like when our city’s first telegraph line got set up, he was in charge of making sure it couldn’t be tampered with by foreign agents."
                    mc "There’s a bunch of different branches in the government. Sometimes it’s hard to keep track of all of them."
                    mc "The {color=#48B5A1}M{/color}inistry of {color=#48B5A1}E{/color}ducation, {color=#48B5A1}O{/color}rder, and {color=#48B5A1}W{/color}elfare… The {color=#48B5A1}P{/color}eaceful {color=#48B5A1}U{/color}nited {color=#48B5A1}R{/color}esource {color=#48B5A1}R{/color}eallocation {color=#48B5A1}D{/color}epartment… The {color=#48B5A1}C{/color}ouncil of {color=#48B5A1}L{/color}aw, {color=#48B5A1}A{/color}uthority, and {color=#48B5A1}W{/color}arfare…"
                    mc "The PDRC has a lot of moving parts, but day-to-day life is pretty normal overall. "
                    window hide
                    jump pdrc
                "(Focus on the few happy memories you have)":
                    window show
                    show kari blush
                    mc "I remember my mom and my dad taking me down the road to get ice cream at a little shop."
                    mc "I remember swimming in the ocean with my dad."
                    mc "I remember drinking tea with my mom."
                    mc "We would all go and watch the parades together."
                    mc "And then we’d go down to the beach and watch the sunset…"
                    show kari -blush
                    mc "..."
            b "Those are wonderful memories."
            mc "Yeah, I mean, it's not {i}all{/i} sunshine and catnip."
            show kari frown
            mc "The people there are… pretty set in their ways."
            mc "New ideas usually come across as ridiculous at best."
            mc "At worst… dangerous."
            mc "It was hard to see back then, but once I started traveling I realized how different things can be."
            mc "I’ll go home eventually."
            show kari -frown
            mc "But for now, I’m planning on seeing all the amazing things this world has to offer, things that I never could have even imagined if I had stayed home."
        "You know, that’s probably what got me into making drinks in the first place.":
            window show
            mc "Sometimes, if Mom was busy, I’d try and make cattail citrus for the two of us."
            show kari sweatdrop
            mc "Except I wasn’t tall enough to put the kettle on the stove."
            mc "And I had no clue how to properly steep the tea."
            mc "And I would always add too much sugar."
            show kari blush
            mc "So my mom would come into the kitchen to see me in the middle of a huge mess, holding two cups of cold, sugary water."
            mc "With just a hint of citrus."
            show kannika blush
            play sound "Dewdrop_KannikaLaugh.mp3" volume 0.7
            nn "{i}Over the course of the story, Kannika’s expression changes from bemusement to uncontrollable laughter. She unsuccessfully tries to cover her mouth with her hands to restrain her giggles before they burst out of her as entirely un-princesslike guffaws.{/i}" (cb_name="kannika")
            nn "{i}She wipes the tears from the corners of her eyes just in time to see you place a cup of softly steaming cattail citrus tea in front of her.{/i}" (cb_name="kannika")
            show kari smile
            show kannika smile
            mc "Here you go! One cattail citrus tea."
            window hide
            show drink bg:
                align (0.5, 0.4)
            show cattail citrus zorder 3:
                align (0.5, 0.4)
            with dissolve
            pause 1.5
            hide drink bg
            hide cattail citrus
            with dissolve
            pause 0.25
            b "This is… truly incredible. Thank you."
            mc "What a coincidence! Whenever my mom drank that “tea” I made for her, she would say exactly the same thing."
            show kannika blush
            b "She sounds like a wonderful mother."
            window hide
            menu:
                "She really is.":
                    window show
                "(Smile, but stay silent)":
                    window show
                "Even when we get into our little disagreements, I know she’ll come around in the end.":
                    window show
                    b "You’re very lucky, to have a parent so understanding."
                    show kari -smile
                    mc "..."
                    mc "Yeah."
                    mc "Understanding."
                    show kannika -blush
                    b "I’m sorry, I didn’t mean to bring up any bad memories."
                    mc "No, no, it's okay."
                    b "..."
                    b "If you don't mind me asking..."
                    mc "..."
                    window hide
                    menu:
                        "Go ahead.":
                            window show
                        "(Nod while avoiding eye contact)":
                            window show
                        "Wow, the swamp is really swampy tonight!":
                            window show
                            b "It’s oka–"
                            show kari sweatdrop
                            mc "Craaazy weather we’ve been having, huh?"
                            show kannika surprised
                            b "Kari–"
                            show kari sunglasses
                            mc "Hey, check out this cool birthmark I’ve got on my–"
                            show kannika gloom
                            b "KARI."
                            show kari exclamation
                            play sound "Dewdrop_Clatter.mp3" volume 0.7
                            n "{i}Cups clatter against the countertop. You blink to see that Kannika has stood up from her seat to grab your shoulder, snapping you out of your deflection spiral.{/i}"
                            show kari surprised
                            show kannika frown
                            n "{i}You become immediately aware of how close she is to you, the warmth of her hand through your shirt, somehow both firm and gentle.{/i}"
                            n "{i}Your eyes refocus on hers – vibrant orange like cups of honey, lit by lamplight and fireflies.{/i}"
                            show kannika surprised
                            n "{i}Kannika blushes and takes her hand off your shoulder. The two of you stand awkwardly on opposite sides of the counter, not quite making eye contact.{/i}"
                            play sound "Dewdrop_Sip.mp3" volume 0.7
                            n "{i}After a few moments, Kannika gently sits back in her chair and picks up her cup, bringing it to her lips and sipping deeply.{/i}"
                            show kannika frown
                            b "I'm sorry."
                            show kari frown
                            mc "It's okay-"
                            b "No, it's not."
                            b "I know how it feels to fight with a parent."
                            b "I leave the castle to get away from that feeling. I came {i}here{/i} to get away from that feeling."
                            b "It’s not fair of me to drag you into those feelings with me."
                            mc "No, it’s not your fault."
                            mc "It’s really not that big of a deal, either."
                            b "At the very least, I shouldn’t have grabbed you like that."
                            window hide
                            menu:
                                "I didn't mind it.":
                                    window show
                                    play sound "Dewdrop_KannikaClearThroat.mp3" volume 0.7
                                    show kannika exclamation
                                    n "{i}Flustered, Kannika coughs into her hand.{/i}"
                                    show kannika -exclamation
                                "Hey. It's okay.":
                                    window show
                            show kari -frown
                            mc "Honestly, it just makes me happy to know that the Dewdrop Cafe is somewhere you can get away from all that."
                            mc "In a lot of ways, it’s the same for me."
                            mc "But it’s been just about two years since then."
                            mc "I’ve had plenty of time to think about what happened."
                            mc "And if there’s anything I can do to help you out with whatever kind of argument you’ve been having with your mom..."
                            mc "I’m here for you to talk to."
                            show kannika -frown
                            b "..."
                    b "Is that why you left home?"
                    b "Fighting with your mom, I mean."
                    mc "My mom and my dad – both of them."
                    show kari frown
                    mc "And it wasn’t a fight! We just… couldn’t see eye to eye, I guess."
                    mc "I had to get out of the house for a bit."
                    show kari sweatdrop
                    mc "So I decided… might as well start a cafe, right?"
                    show kannika surprised
                    b "Just like that? You just walked away?"
                    mc "I mean, yeah, kind of."
                    mc "It’s not like I’ll be gone forever."
                    mc "Just, y’know… until they come around to things."
                    b "Do you think that’s possible?"
                    show kari smile
                    mc "Of course!"
                    show kari -smile
                    mc "It might just take some time, that’s all."
            show kannika frown
            b "I wish I could say the same for my own mother."
            nn "{i}Kannika sips her tea, gazing into its warm floral depths. The light from the evening’s fireflies dances along her lashes and the scales on her neck.{/i}" (cb_name="kannika")
            nn "{i}In this moment it’s easy to forget that she’s a princess. All you see in front of you is a melancholic young woman finding momentary solace in a warm cup of tea.{/i}" (cb_name="kannika")
            nn "{i}After all, it wasn’t too long ago that you were just the same.{/i}" (cb_name="kari")
            mc "..."

            # Talk about it menu
            window hide
            $ talkaboutittree = {"nottonight": False}
            menu talkaboutit:
                "Want to talk about it?" if not talkaboutittree["nottonight"]:
                    $ talkaboutittree["nottonight"] = True
                    window show
                    b "..."
                    b "Not tonight."
                    b "Thank you, though."
                    b "I’d rather pair this exquisite tea with happier conversation topics."
                    window hide
                    jump talkaboutit
                "(Change the subject)":
                    window show
            mc "You know, when I first started traveling, I used to make cattail citrus for myself a lot."
            mc "Whenever I drink it, I think of home."
            mc "Of the ocean, the cobbled streets, the banners and flags…"
            mc "But once I went beyond the border and started learning new recipes, trying new drinks, I realized I wasn’t making cattail citrus as much."
            mc "Instead, whenever I feel down or homesick, I make myself something from one of the places I’ve traveled through."
            mc "They help me think of the good parts of my journey, instead of the bad ones."
            mc "They remind me of all the amazing experiences I’ve had because I left home."
    n "{i}As the memories recede, you blink back to the present. Kannika is watching you with keen interest.{/i}"
    show kari blush
    n "{i}You blush slightly as you realize just how much you’d been rambling. How long have you been talking for??{/i}"
    show kannika blush
    b "More, please."
    mc "..."
    window hide
    menu:
        "Whuh?":
            window show
        "Uh-":
            window show
        "(Blink in confusion)":
            window show
    show kari exclamation
    n "{i}You glance down and realize that Kannika has finished off her cup of tea. She nudges the empty cup towards you, smiling.{/i}"
    show kari surprised
    b "More, please. Both the tea and the stories."
    b "I want to hear about everywhere you’ve gone to."
    mc "...!"
    show kari blush
    mc "Another cattail citrus tea, coming right up!"
    window hide

    # Fade out
    pause 0.25
    scene black
    with fade
    pause 0.25
    show kannika smile with dissolve
    play sound "Dewdrop_MakeDrink.mp3" volume 0.7
    window show
    n "{i}You make the naga princess her tea and spend the next half-hour regaling her with descriptions of the many places you’ve been.{/i}"
    n "{i}You tell her about your journey and the wonders you’ve seen – the waterways in the City of Swans, the grand domes of the Otterman Empire, the vibrant flower fields of the Sun Bearony, and even the magnificent parades of your home.{/i}"

    return

# Humming lavender branching dialogue
label humminglavendertree:

    # Intro
    b "The tea you gave me last night was quite nice."
    b "Where did you learn to make it?"
    show kari smile
    mc "Oh, the humming lavender? That’s a drink from the Sun Bearony!"
    mc "They’re famous for their gigantic beehives, and they plant these huge fields of flowers..."
    mc "In the spring, it’s just bright colors as far as you can see in every direction."
    show kannika blush
    b "That sounds breathtaking."
    show kannika smile
    b "My tutors often speak of other countries, but I don’t recall the Sun Bearony among them."
    show kari -smile
    mc "..."

    # Sun Bearony menu
    window hide
    menu:
        "To be fair, it’s not a particularly important country in the first place.":
            window show
            mc "More of a city state, really. It’s mostly farms and orchards."
            b "The tea alone makes me want to learn more."
            show kari smile
            mc "You have quite the discerning palate, my lady."
            show kari -smile
        "Maybe if they try some of this humming lavender, they’ll add it to your curriculum.":
            window show
            show kannika -smile
            b "Would that it were so simple."
            b "Those fusty old crabs do everything by the books."
            b "Except those books were written a few hundred years ago."
            mc "That’s terrible! Think of all the wonderful drinks that the history books have tragically overlooked..."
            show kannika smile
            b "You’ll have to start catching me up to speed."
            mc "It would be my honor to do so, my lady."
        "Really? You should visit sometime!":
            window show
            mc "Genuine Sun Bearony honeycomb is {i}the best.{/i}"
            b "I would love to travel..."
            b "Unfortunately, I have many duties as an heiress."
            b "Maybe in the future I’ll be able to go traveling like you."
            mc "If you would have me, my lady, I would be honored to guide you in your quest for exotic drinks."
        "Dozing off in class, eh? Some things are the same no matter where you travel.":
            window show
            show kari smile
            show kannika surprised
            b "I– What–"
            b "I don’t doze off in class! I–"
            mc "I’m joking, I’m joking."
            mc "I’m sure you’re a star pupil."
            b "..."
            show kannika -surprised
            show kannika smile
            b "Okay, there was {i}one time{/i} I lost my focus during a lesson."
            b "But only once."
            mc "Good heavens! My lady, how scandalous!"
            show kannika -smile
            show kari -smile
    show kannika -smile
    nn "{i}Something passes across Kannika’s face like a cloud on an otherwise clear day. Her posture stiffens, and her dimpled grin fades to a practiced close-lipped smile.{/i}" (cb_name="kannika")
    nn "{i}After a moment she seems to realize you were speaking in exaggerated formality as a joke, and she forces a chuckle.{/i}" (cb_name="kannika")
    b "Please, none of those honorifics while I’m here."
    b "I have to be a princess all day. Right now, I just want to enjoy some tea from fantastical, far-off lands."
    mc "One glass of fantastical, coming right up!"
    window hide

    # Fade out
    pause 0.25
    scene black
    with fade
    pause 0.25

    play sound "Dewdrop_MakeDrink.mp3" volume 0.7
    window show
    n "{i}You spend the next half-hour mixing various drinks for the naga princess, treating her to a medley of beverages from your travels across the land.{/i}"
    n "{i}You tell her about your journey and the wonders you’ve seen – the waterways in the City of Swans, the grand domes of the Otterman Empire, and many more.{/i}"
    return
    
# Moon jelly branching dialogue
label moonjellytree:
    
    # Intro
    b "What other kinds of drinks do you serve?"
    mc "Well, I’ve got a bunch of teas, some fruit juices, and a couple different coffees."
    b "Is each one from a different place you’ve traveled through?"
    mc "Yeah! It’s one of my favorite parts about traveling."
    mc "Every new drink I add to the menu is like my own little piece of that place."
    mc "For example..."

    # Drinks from different places menu
    window hide
    $ differentdrinkstree = {"cattail": False, "humming": False, "otterkish": False, "affogato": False, "lastone": 0}
    menu differentdrinks:
        "Cattail citrus tea, from my home country." if not differentdrinkstree["cattail"]:
            $ differentdrinkstree["cattail"] = True
            $ differentdrinkstree["lastone"] += 1
            window show
            mc "You’re supposed to infuse it with sliced cattail root, but you can’t really taste it in the end."
            mc "It’s mostly citrus."
            mc "At least, that’s the way I learned how to make it."

            # Check to see if this is the last drink
            if differentdrinkstree["lastone"] != 4:
                window hide

            jump differentdrinks
        "Humming lavender tea, from the Sun Bearony." if not differentdrinkstree["humming"]:
            $ differentdrinkstree["humming"] = True
            $ differentdrinkstree["lastone"] += 1
            window show
            mc "Bearony flower fields are always humming with bees. Hence the name."
            mc "It’s floral and sweet and it kinda makes you want to just lie down and take a nap somewhere sunny."
            mc "Whether that’s a positive or a negative is up to you."

            # Check to see if this is the last drink
            if differentdrinkstree["lastone"] != 4:
                window hide
            
            jump differentdrinks
        "Otterkish coffee, from the Otterman Empire." if not differentdrinkstree["otterkish"]:
            $ differentdrinkstree["otterkish"] = True
            $ differentdrinkstree["lastone"] += 1
            window show
            mc "Traditionally they bring it to a boil with sand that’s been heated over a fire, but I just use a hotplate."
            mc "Oh, and they add a pinch of sea salt."
            mc "I’m not a huge coffee person, but Otterkish coffee is pretty good."

            # Check to see if this is the last drink
            if differentdrinkstree["lastone"] != 4:
                window hide
            
            jump differentdrinks
        "Affogato al signo, from the City of Swans." if not differentdrinkstree["affogato"]:
            $ differentdrinkstree["affogato"] = True
            $ differentdrinkstree["lastone"] += 1
            window show
            mc "It’s a scoop of gelato in a cup of espresso! How genius is that?!"
            mc "I honestly can’t decide if it’s a drink or if it’s a dessert."
            mc "Don’t tell anyone, but when I first tried it I was definitely having it for the gelato and not for the coffee."

            # Check to see if this is the last drink
            if differentdrinkstree["lastone"] != 4:
                window hide
            
            jump differentdrinks

    mc "Any of those appeal to you?"
    b "Those all sound incredible."
    b "If I pick one, will you tell me about the place it comes from?"
    mc "Of course!"
    b "One of each, then."
    b "I’m looking forward to hearing these stories."
    play sound "Dewdrop_KariLaugh.mp3" volume 0.7
    mc "Ha! You got me!"
    mc "It’s a good thing I can talk while I work."
    mc "One of everything, coming right up!"
    window hide

    # Fade out
    pause 0.25
    scene black
    with fade
    pause 0.25

    play sound "Dewdrop_MakeDrink.mp3" volume 0.7
    window show
    n "{i}You spend the next half-hour mixing various drinks for the naga princess, treating her to a medley of beverages from your travels across the land.{/i}"
    n "{i}You tell her about your journey and the wonders you’ve seen – the grand parades of your home country, the vibrant flower fields of the Sun Bearony, and many more.{/i}"
    return

# TO BE USED LATER

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
    show starfruit sunset zorder 3:
        align (0.5, 0.4)
    with dissolve