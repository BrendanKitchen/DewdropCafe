# starts with chapter 1
# remaining chapters are in separate .rpy files under the story folder 
# WHEN CREATING NEW CHAPTERS: make sure to add a chapter variable here and mark it false w persistent
# this is for the chapter select


define persistent.ch1 = False 
define persistent.ch2 = False
define persistent.ch3 = False
define persistent.ch4 = False
define persistent.ch5 = False

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
    "{i}You hear a splash in the darkness behind your cafe.{/i}"
    pause 0.5
    
    show night bg with fade
    show kari surprised
    window show

    play sound "Dewdrop_KannikaPanting.mp3" volume 0.7
    mc "...!"
    mc "What was that?"

    menu:
        "Hello? Is someone there?":
            bquestionmark "Shhh! He'll hear you!"
        "(Stay quiet and listen)":
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
    with MoveTransition(1.0)
    pause 0.25
    show kari:
        xzoom 1.0
    pause 0.25
    show kannika neutral at left
    with easeinbottom
    window show

    bquestionmark "You need to help me. I need a place to hide."
    mc "What? Who are you?"
    bquestionmark "No time. Move over."
    "{i}You watch, stunned, as the naga begins to pull herself over the counter and into your cafe.{/i}"

    show kari -surprised
    show kari:
        xzoom 1.0

    menu:
        "Wh- Just hold on a second and tell me what's going on!":
            bquestionmark "Later. Don't let him know I'm here."
            "{i}The strange naga heaves herself over the counter and curls up beneath it, wrapping her tail around herself.{/i}"
            "{i}She meets your eyes and puts a finger to her lips.{/i}"
        "(Try and stop her from climbing over the counter)":
            "{i}As soon as you make contact with the strange naga, you instantly know you're no match.{/i}"
            "{i}She smoothly redirects your shove and you end up spinning around in place as she curls her tail around herself and hides beneath the counter.{/i}"
        "(Help her climb over the counter)":
            "{i}As soon as you make contact with the strange naga, you instantly know she doesn't even need your help. With just her arms, she pulls herself over the counter and curls up beneath it, wrapping her tail around herself."
            "{i}You see the trail of swamp water left behind and quickly grab a towel to blot it up. You glance down and smile reassuringly. She meets your eyes with a look of gratitude and smiles back. {/i}"
        "Uh. Okay. Sure. Yeah.":
            "{i}The strange naga heaves herself over the counter and curls up beneath it, wrapping her tail around herself. She meets your eyes and puts a finger to her lips.{/i}"
        
    hide kannika with easeoutbottom
    pause 0.75
    play sound "Dewdrop_Splash.mp3" volume 0.7
    "{i}Just as she does so, another figure emerges from the swamp.{/i}"
    show luan neutral at left
    with easeinleft
    "{i}Another naga – a man clad in armor and blue finery, an emblem emblazoned across one shoulder. An elegant sword is sheathed at his waist.{/i}"

    g "You there. Foreigner. Have you seen a lady around here?"
    g "Pink hair, blue tail, holding a parasol..."
    "{i}The guard glances down, noticing the swamp water still puddled on the countertop."

    menu:
        "Uh, nope! No sir, haven’t seen anyone like that.":
            mc "I've actually been setting up all day. Welcome to the Dewdrop Cafe!"
            g "..."

        "(Distract him)":
            mc "No, but I do have some drinks with little umbrellas in them!"
            mc "Welcome to the Dewdrop Cafe - tonight's our grand opening, and, uh, you're our first customer! Yay!"
            g "..."
            mc "So, uh, anything I can get for you?"
            g "..."
            g "No, thank you."
            g "There are more pressing matters at hand."

        "Yep. She's hiding under my counter.":
            show kannika with easeinbottom
            bquestionmark "Wh-?!"
            g "My lady. Enough of these games."
            g "You are far too old to be acting this childish."
            bquestionmark "..."
            "{i}The woman stands up from behind the counter. Her face is a roiling mixture of frstration, embarrassment, and betrayal.{/i}"
            "{i}She looks at you with an expression as cold as ice.{/i}"
            bquestionmark "It seems a little trust was too much to ask for."
            bquestionmark "Goodbye."
            "{i}The guard escorts her away, and the two disappear into the darkness of the night.{/i}"
            show luan neutral:
                xzoom -1.0
            show luan neutral at offscreenleft
            with easeoutleft
            show kari at center 
            with move
            pause 0.5
            scene black
            with fade
            pause 0.5
            "{i}The rest of your stay in the Naga Kingdom is pleasant and uneventful, if a bit too humid for your tastes. Eventually, that old itch in the back of your mind returns – it’s time to move on.{/i}"
            "{i}You pack up your cafe and set off on the road once again. No one is waiting to see you off. No one begs for you to stay. You are alone, just as you have been since you left your home almost two years ago.{/i}"
            "{i}Soon, your memories of this place will fade into pretty pastels and wistful impressions. The City of Swans, the Otterman Empire, the Naga Kingdom… all just names on a map, a blurred collection of faces and sounds and smells, bleeding together like watercolors in the rain.{/i}"
            "{i}You never did see that naga woman again. You never even got her name. Sometimes you think about that night, that odd encounter, and wonder what might have happened if things went differently. Time moves ever-forward, however. You have little choice but to turn your thoughts to the road ahead, rather than linger on what you might have left by the wayside.{/i}"
            "{i}Eventually, even she will evaporate into faint recollections of swamp water on a countertop. Your travels will have you meet many new people, experience many new things. This little kingdom will be just another chapter in your tales to tell when you’re sitting at a table with people who love you. {/i}"
            "{i}Right now, however, you are alone. Just you, the road, and whatever the future has in store for you.{/i}"
            "{i}Maybe it’s better this way.{/i}"
            window hide
            pause 1.0
            $ renpy.full_restart(transition=Fade(0.5,0.5,0.25))

    window show
    show luan frown
    g "If you do see her, contact a member of the Halfmoon Guard as soon as you can. It’s dangerous for her to be out alone."
    mc "Yessir. I will definitely do that."
    show luan neutral:
        xzoom -1.0
    window hide
    show luan neutral at offscreenleft
    with easeoutleft
    pause 1.0
    window show

    mc "..."
    mc "I think he's gone. You can come out now."

    window hide
    show kannika:
        xzoom 1.0
    show kannika at left
    with MoveTransition(0.75)
    with easeinleft
    window show 

    bquestionmark "Thank you. I’m glad you were here."
    mc "What was that about? Are you okay?"
    show kannika surprised
    bquestionmark "Yes, I am, it’s… somewhat complicated. I’m…"

    menu:
        "...running away from home?":
            bquestionmark "..."
            bquestionmark "How did you know?"
            mc "Just a hunch."
        "...playing a really intense game of hide-and-seek?":
            bquestionmark "Ha. I wish."
            bquestionmark "I guess it's somewhat similar, though it's much less exciting."
            bquestionmark "A futile game."
            mc "Well, I'm glad you're not in danger."
            mc "Okay are you actually..."
            menu:
                "...running away from home?":
                    bquestionmark "..."
                    bquestionmark "How did you know?"
                    mc "Just a hunch."
                "...a foreign agent here to steal military secrets...":
                    bquestionmark "...what?"
                    mc "...and threaten the hegemonic authority of a glorious regime?"
                    mc "Sorry. When I was a kid we used to hear about that kind of stuff all the time."
                    mc "Everybody liked to guess which of our teachers were secretly spies, but I don't think I've ever actually met one."
                    mc "Not that I'd turn you in if you {i}did{/i} happen to be a spy, of course."
                    mc "I'm no snitch."
                    bquestionmark "...Thank...you?"
                    mc "You're welcome!"
                    mc "Alright. Are you maybe..."
                    menu:
                        "...running away from home?":
                            bquestionmark "..."
                            bquestionmark "How did you know?"
                        mc "Just a hunch."
        "...a foreign agent here to steal military secrets...":
            mc "...and threaten the hegemonic authority of a glorious regime?"
            bquestionmark "...what?"
            mc "Sorry. When I was a kid we used to hear about that kind of stuff all the time."
            mc "Everybody liked to guess which of our teachers were secretly spies, but I don't think I've ever actually met one."
            mc "Not that I'd turn you in if you {i}did{/i} happen to be a spy, of course."
            mc "I'm no snitch."
            bquestionmark "...Thank...you?"
            mc "You're welcome!"
            mc "Alright. Are you maybe..."
            menu:
                "...running away from home?":
                    bquestionmark "..."
                    bquestionmark "How did you know?"
                    mc "Just a hunch."
                "...playing a really intense game of hide-and-seek?":
                    bquestionmark "Ha. I wish."
                    bquestionmark "I guess it's somewhat similar, though it's much less exciting."
                    bquestionmark "A futile game."
                    mc "Well, I'm glad you're not in danger."
                    mc "Okay are you actually..."
                    menu:
                        "...running away from home?":
                            bquestionmark "..."
                            bquestionmark "How did you know?"
                        mc "Just a hunch."


    mc "That's a pretty intense outfit to be running away from home in."
    bquestionmark "What do you mean?"
    mc "All that silk and ribbons and frills… Shouldn’t you have worn something, I dunno, less flashy?"
    bquestionmark "Less flashy? This is the most subtle clothing I have."
    bquestionmark "I’m not joking. My closet looks like a kelp forest made of lace and jewelry."
    mc "Okay, sure, but the parasol?"
    bquestionmark "...it completes the fit."
    "{i}You and the naga dissolve into a fit of giggles.{/i}"
    "{i}Laughter weaves through the humid night air, not quite drowned out by the chirps and calls of the swamp's other denizens.{/i}"
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
    "{i}Before long, the whistle of a teakettle joins the chorus of bugs and frogs in the night. The naga holds the cup between her hands, feeling its warmth. She takes her time as she sips it, savoring the taste."

    menu:
        "Cattail citrus.":
            play sound "Dewdrop_MakeDrink.mp3" volume 0.7
            with Fade(0.5, 0.5, 0.5)
            show drink bg:
                align (0.5, 0.4)
            show :
                align (0.5, 0.4)
            mc "Good, isn't it? My mom used to make it for me all the time."
            bquestionmark "..."
            bquestionmark "It's very good. I can see why it's your favorite."
        "Humming lavender.":
            play sound "Dewdrop_MakeDrink.mp3" volume 0.7
            with Fade(0.5, 0.5, 0.5)
            mc "This was the first drink I learned how to make after I left home. Drinking it is really relaxing, don't you think?"
            bquestionmark "..."
            bquestionmark "It's very good."
        "Moon jelly tea.":
            play sound "Dewdrop_MakeDrink.mp3" volume 0.7
            with Fade(0.5, 0.5, 0.5)
            mc "Cute, right? I learned how to make it in the City of Swans, but I hear it first originated in this region."
            bquestionmark "..."
            bquestionmark "It's good."

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

