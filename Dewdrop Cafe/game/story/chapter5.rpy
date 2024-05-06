label chapter5:
    $ persistent.ch5 = True

    # Chapter Card Intro
    window hide
    $ quick_menu = False
    scene black bg
    show ch5 with fade:
        align (0.5, 0.5)
    pause 2
    hide ch5 with fade
    $ quick_menu = True
    window show

    show night bg
    with dissolve
    show kari neutral at right
    with dissolve
    "{i}A few days later, Kari is cleaning up her station, when an annoyed Kannika slithers up to the counter and angrily rings the bell.{/i}"
    window hide 

    show kannika angry at left
    with easeinleft
    show kannika neutral

    play sound "Dewdrop_Bell_Mashing.mp3" volume 0.8
    
    show kari surprised
    pause 3.0
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
    scene black
    with fade
    # hide kari with dissolve
    # scene black with dissolve

    # jump chapter6

    # move this to the next 'last' chapter
    "{i}To be continued...{/i}"
    # return to main menu
    $ renpy.full_restart(transition=Fade(0.5,0.5,0.25))