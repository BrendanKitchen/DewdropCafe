# starts with chapter 1
# remaining chapters are in separate .rpy files under the story folder 
# WHEN CREATING NEW CHAPTERS: make sure to add a chapter variable here and mark it false w persistent
# this is for the chapter select

define persistent.ch1 = False 
define persistent.ch2 = False
define persistent.ch3 = False
define persistent.ch4 = False
define persistent.ch5 = False
define karihelpedkannika = False

label start:
    $ persistent.ch1 = True
    play music "pas_de_deuxdrop.mp3"
    pause 0.75
    window show
    mc "Phew!" 
    mc "Alright, I think that looks good."

    window hide
    pause 0.5
    show night bg with fade
    pause 2.0
    show kari neutral at center
    with easeinright
    pause 0.25
    window show

    mc "It’s a little damp, but otherwise this is a great spot – right on the waterfront!"
    mc "I hope the chairs don’t sink into the mud…"
    mc "Still gotta finish unpacking... "

    window hide
    show cg_ch1_1 with dissolve
    pause 2.0
    window show
    play sound "Dewdrop_KariSigh.mp3" volume 0.7
    mc "It’s been, what, two years now?"
    mc "I’m sure you’d be happy to hear I’m doing well."
    mc "The road’s as rough as always, but I think it’s all been going great."
    mc "The cafe was really popular at the last place! At one point I think I was making twelve drinks at the same time."
    mc "…"
    mc "Even after everything, I still miss you guys."
    mc "I’ll come back some day. Probably."

    window hide
    scene black
    with fade
    pause 0.5
    play sound "Dewdrop_Splash.mp3" volume 0.7
    pause 1
    window show
    "{i}You hear a splash in the darkness behind your cafe.{/i}"
    window hide
    pause 0.5
    
    show night bg with fade
    show kari neutral
    show kari surprised
    with easeinright
    window show

    play sound "Dewdrop_KannikaPanting.mp3" volume 0.7
    mc "...!"
    mc "What was that?"

    window hide
    menu:
        "Hello? Is someone there?":
            window show
            bquestionmark "Shhh! He'll hear you!"
        "(Stay quiet and listen)":
            window show
            "{i}The night is abuzz with insects and the croaking of frogs. After a few moments, you hear another splash -{/i}"
            pause 0.25
            play sound "Dewdrop_Splash.mp3" volume 1.0
            pause 0.5
            "{i}- louder than the first.{/i}"
            mc "{i}Uh. That was definitely closer than the last one.{/i}"
    window hide

    show kari:
        xzoom -1.0
        align (1.0, 0.5)
    with MoveTransition(0.75)
    show kari:
        xzoom 1.0
    show kannika neutral
    show kannika surprised at left
    with easeinleft
    window show

    bquestionmark "You need to help me. I need a place to hide."
    mc "What? Who are you?"
    bquestionmark "No time. Move over."
    "{i}You watch, stunned, as the naga begins to pull herself over the counter and into your cafe.{/i}"

    show kari -surprised

    window hide
    menu:
        "Wh- Just hold on a second and tell me what's going on!":
            window show
            bquestionmark "Later. Don't let him know I'm here."
            "{i}The strange naga heaves herself over the counter and curls up beneath it, wrapping her tail around herself.{/i}"
            "{i}She meets your eyes and puts a finger to her lips.{/i}"
        "(Try and stop her from climbing over the counter)":
            window show
            "{i}As soon as you make contact with the strange naga, you instantly know you're no match.{/i}"
            "{i}She smoothly redirects your shove and you end up spinning around in place as she curls her tail around herself and hides beneath the counter.{/i}"
        "(Help her climb over the counter)":
            window show
            "{i}As soon as you make contact with the strange naga, you instantly know she doesn't even need your help. With just her arms, she pulls herself over the counter and curls up beneath it, wrapping her tail around herself."
            "{i}You see the trail of swamp water left behind and quickly grab a towel to blot it up. You glance down and smile reassuringly. She meets your eyes with a look of gratitude and smiles back. {/i}"
            $ karihelpedkannika = True
        "Uh. Okay. Sure. Yeah.":
            window show
            "{i}The strange naga heaves herself over the counter and curls up beneath it, wrapping her tail around herself. She meets your eyes and puts a finger to her lips.{/i}"

    window hide
    hide kannika with easeoutbottom
    pause 0.75
    play sound "Dewdrop_Splash.mp3" volume 0.7

    window show
    "{i}Just as she does so, another figure emerges from the swamp.{/i}"
    show luan neutral at left
    with easeinleft
    "{i}Another naga – a man clad in armor and blue finery, an emblem emblazoned across one shoulder. An elegant sword is sheathed at his waist.{/i}"

    g "You there. Foreigner. Have you seen a lady around here?"
    g "Pink hair, blue tail, holding a parasol..."

    if karihelpedkannika == False:
        "{i}The guard glances down, noticing the swamp water still puddled on the countertop.{/i}"

    window hide
    menu:
        "Uh, nope! No sir, haven’t seen anyone like that.":
            window show
            mc "I've actually been setting up all day. Welcome to the Dewdrop Cafe!"
            g "..."

        "(Distract him)":
            window show
            mc "No, but I do have some drinks with little umbrellas in them!"
            mc "Welcome to the Dewdrop Cafe - tonight's our grand opening, and, uh, you're our first customer! Yay!"
            g "..."
            mc "So, uh, anything I can get for you?"
            g "..."
            g "No, thank you."
            g "There are more pressing matters at hand."

        "Yep. She's hiding under my counter.":
            pause 0.25
            show kannika surprised with easeinbottom
            pause 0.25
            window show
            bquestionmark "Wh-?!"
            g "My lady. Enough of these games."
            g "You are far too old to be acting this childish."
            bquestionmark "..."
            "{i}The woman stands up from behind the counter. Her face is a roiling mixture of frustration, embarrassment, and betrayal.{/i}"
            show kannika angry:
                xzoom 1.0
            "{i}She looks at you with an expression as cold as ice.{/i}"
            bquestionmark "It seems a little trust was too much to ask for."
            bquestionmark "Goodbye."
            "{i}The guard escorts her away, and the two disappear into the darkness of the night.{/i}"
            window hide
            show luan neutral:
                xzoom -1.0
            show luan neutral at offscreenleft
            with MoveTransition(0.75)
            pause 0.25
            show kannika angry:
                xzoom -1.0
            show kannika angry at offscreenleft
            with MoveTransition(0.75)
            show kari neutral at center 
            with move
            pause 0.5
            scene black
            with fade
            pause 0.5
            window show
            "{i}The rest of your stay in the Naga Kingdom is pleasant and uneventful, if a bit too humid for your tastes. Eventually, that old itch in the back of your mind returns – it’s time to move on.{/i}"
            "{i}You pack up your cafe and set off on the road once again. No one is waiting to see you off. No one begs for you to stay. You are alone, just as you have been since you left your home almost two years ago.{/i}"
            "{i}Soon, your memories of this place will fade into pretty pastels and wistful impressions.{/i}"
            "{i}The City of Swans, the Otterman Empire, the Naga Kingdom… all just names on a map, a blurred collection of faces and sounds and smells, bleeding together like watercolors in the rain.{/i}"
            "{i}You never did see that naga woman again. You never even got her name. Sometimes you think about that night, that odd encounter, and wonder what might have happened if things went differently.{/i}"
            "{i}Time moves ever-forward, however. You have little choice but to turn your thoughts to the road ahead, rather than linger on what you might have left by the wayside.{/i}"
            "{i}Eventually, even she will evaporate into faint recollections of swamp water on a countertop.{/i}"
            "{i}Your travels will have you meet many new people, experience many new things. This little kingdom will be just another chapter in your tales to tell when you’re sitting at a table with people who love you. {/i}"
            "{i}Right now, however, you are alone. Just you, the road, and whatever the future has in store for you.{/i}"
            "{i}Maybe it’s better this way.{/i}"
            window hide
            pause 1.0
            $ renpy.full_restart(transition=Fade(0.5,0.5,0.25))

    show luan frown
    g "If you do see her, contact a member of the Halfmoon Guard as soon as you can. It’s dangerous for her to be out alone."
    mc "Yessir. I will definitely do that."
    show luan:
        xzoom -1.0
    window hide
    show luan at offscreenleft
    with MoveTransition(0.75)
    pause 0.5
    
    window show
    mc "..."
    mc "I think he's gone. You can come out now."
    window hide

    show kannika neutral at left
    with easeinbottom
    window show 

    bquestionmark "Thank you. I’m glad you were here."
    mc "What was that about? Are you okay?"
    show kannika surprised
    bquestionmark "Yes, I am, it’s… somewhat complicated. I’m…"
    show kannika -surprised

    window hide
    menu:
        "...running away from home?":
            pass
        "...playing a really intense game of hide-and-seek?":
            window show
            bquestionmark "Ha. I wish."
            bquestionmark "I guess it's somewhat similar, though it's much less exciting."
            bquestionmark "A futile game."
            mc "Well, I'm glad you're not in danger."
            mc "Okay are you actually..."
            window hide
            menu:
                "...running away from home?":
                    pass
                "...a foreign agent here to steal military secrets...":
                    window show
                    bquestionmark "...what?"
                    mc "...and threaten the hegemonic authority of a glorious regime?"
                    mc "Sorry. When I was a kid we used to hear about that kind of stuff all the time."
                    mc "Everybody liked to guess which of our teachers were secretly spies, but I don't think I've ever actually met one."
                    mc "Not that I'd turn you in if you {i}did{/i} happen to be a spy, of course."
                    mc "I'm no snitch."
                    bquestionmark "...Thank...you?"
                    mc "You're welcome!"
                    mc "Alright. Are you maybe..."
                    window hide
                    menu:
                        "...running away from home?":
                            pass
        "...a foreign agent here to steal military secrets...":
            window show
            mc "...and threaten the hegemonic authority of a glorious regime?"
            show kannika surprised
            bquestionmark "...what?"
            mc "Sorry. When I was a kid we used to hear about that kind of stuff all the time."
            mc "Everybody liked to guess which of our teachers were secretly spies, but I don't think I've ever actually met one."
            mc "Not that I'd turn you in if you {i}did{/i} happen to be a spy, of course."
            mc "I'm no snitch."
            bquestionmark "...Thank...you?"
            mc "You're welcome!"
            show kannika -surprised
            mc "Alright. Are you maybe..."
            window hide
            menu:
                "...running away from home?":
                    pass
                "...playing a really intense game of hide-and-seek?":
                    window show
                    bquestionmark "Ha. I wish."
                    bquestionmark "I guess it's somewhat similar, though it's much less exciting."
                    bquestionmark "A futile game."
                    mc "Well, I'm glad you're not in danger."
                    mc "Okay are you actually..."
                    window hide
                    menu:
                        "...running away from home?":
                            pass

    window show
    show kannika surprised
    bquestionmark "..."
    show kannika -surprised
    bquestionmark "How did you know?"
    mc "Just a hunch."
    mc "That's a pretty intense outfit to be running away from home in."
    bquestionmark "What do you mean?"
    mc "All that silk and ribbons and frills… Shouldn’t you have worn something, I dunno, less flashy?"
    bquestionmark "Less flashy? This is the most subtle clothing I have."
    bquestionmark "I’m not joking. My closet looks like a kelp forest made of lace and jewelry."
    mc "Okay, sure, but the parasol?"
    bquestionmark "...it completes the fit."
    show kannika smile
    show kari smile
    "{i}You and the naga dissolve into a fit of giggles.{/i}"
    "{i}Laughter weaves through the humid night air, not quite drowned out by the chirps and calls of the swamp's other denizens.{/i}"
    show kannika -smile
    show kari -smile
    bquestionmark "So... a cafe."
    bquestionmark "It's quite charming."
    mc "Aw, thank you! It's the grand opening of the Dewdrop Cafe!"
    mc "Well, not actually the grand opening. That'll be tomorrow."
    mc "..."
    mc "You know what? You should be my first customer!"
    show kannika surprised
    bquestionmark "Really? I-"
    mc "And don't worry about the cost, this one's on the house! Pick any drink you want."
    mc "As long as it's tea. My other ingredients are still packed away."
    show kannika -surprised
    bquestionmark "Any drink, as long as it’s tea."
    mc "As long as it’s tea."
    bquestionmark "Which one’s your favorite? I’ll have that one."
    mc "Excellent choice, madam."
    "{i}Before long, the whistle of a teakettle joins the chorus of bugs and frogs in the night."
    "{i}The naga holds the cup between her hands, feeling its warmth. She takes her time as she sips it, savoring the taste."
    bquestionmark "What is this?"

    window hide
    menu:
        "Cattail citrus.":
            play sound "Dewdrop_MakeDrink.mp3" volume 0.7
            with Fade(0.5, 0.5, 0.5)
            show drink bg:
                align (0.5, 0.4)
            show cattail citrus:
                align (0.5, 0.4)
            with dissolve
            pause 2.0
            play sound "Dewdrop_Sip.mp3" volume 0.8
            pause 2.0
            hide cattail citrus with dissolve
            hide drink bg with dissolve
            window show
            mc "Good, isn't it? My mom used to make it for me all the time."
            bquestionmark "..."
            bquestionmark "It's very good. I can see why it's your favorite."
        "Humming lavender.":
            play sound "Dewdrop_MakeDrink.mp3" volume 0.7
            with Fade(0.5, 0.5, 0.5)
            show drink bg:
                align (0.5, 0.4)
            show seamelon:
                align (0.5, 0.4)
            with dissolve
            pause 2.0
            play sound "Dewdrop_Sip.mp3" volume 0.8
            pause 2.0
            hide seamelon with dissolve
            hide drink bg with dissolve
            window show
            mc "This was the first drink I learned how to make after I left home. Drinking it is really relaxing, don't you think?"
            bquestionmark "..."
            bquestionmark "It's very good."
        "Moon jelly tea.":
            play sound "Dewdrop_MakeDrink.mp3" volume 0.7
            with Fade(0.5, 0.5, 0.5)
            show drink bg:
                align (0.5, 0.4)
            show seamelon:
                align (0.5, 0.4)
            with dissolve
            pause 2.0
            play sound "Dewdrop_Sip.mp3" volume 0.8
            pause 2.0
            hide seamelon with dissolve
            hide drink bg with dissolve
            window show
            mc "Cute, right? I learned how to make it in the City of Swans, but I hear it first originated in this region."
            bquestionmark "..."
            bquestionmark "It's good."
    bquestionmark "Thank you."

    "{i}You watch contentedly as Kannika sips her drink. Her fins and scales shine in the lights from your cafe, glimmering with iridescent hues.{/i}"
    "{i}This cozy moment is interrupted by the faint sound of shouting. Loud voices, far off but approaching, calling out to each other.{/i}"

    bquestionmark "Hm. It seems that he's brought reinforcements."
    bquestionmark "I should be going. I don’t want my own issues to bring you any more trouble."
    "{i}The voices draw closer. The naga woman places her cup back on the counter – there’s still a little left – and glances back at you.{/i}" 
    "{i}She holds your gaze for a heartbeat before pushing away from the counter and disappearing into the darkness.{/i}"

    show kari surprised
    #Kannika leaves the scene
    window hide
    show kannika -smile
    show kannika:
        xzoom -1.0
    show kannika at offscreenleft
    with easeoutleft
    pause 0.25
    show kari at center
    with MoveTransition(0.75)
    window show
    mc "Wait, You forgot your-"
    window hide
    pause 0.5
    play sound "Dewdrop_Splash.mp3" volume 0.7
    pause 1.0
    window show
    mc "...parasol."
    "{i}Just as suddenly as she appeared, the naga is gone. The voices grow more distant until all you can hear are the sounds of the swamp around you.{/i}"
    "{i}You can faintly smell the sea on the wind, but it’s a foreign one, nothing like the ocean of your childhood.{/i}"
    "{i}Once again, you’re alone.{/i}"
    show kari -surprised
    mc "..."
    mc "Running away from home, huh..."
    mc "At least she has people looking after her."
    mc "People who want her to come home."
    "{i}You take the frilly parasol and run your fingers across it.{/i}"
    "{i}It’s wonderfully made – the quality is far beyond anything you’ve seen before, even in your extensive travels.{/i}"
    mc "..."
    mc "Souvenirs! Aw, they’d love stuff like this. I’ve gotta get my hands on one of these…"
    mc "Other than this one, I mean. I should probably give this back."
    mc "I hope I get to give it back to her…"

    window hide
    scene black
    with fade

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

