label chapter5:
    $ persistent.ch5 = True

    # Play music
    play music "Recollection.mp3" volume 0.6

    # Chapter Card Intro
    window hide
    $ quick_menu = False
    scene black bg
    show ch overlay
    show ch5:
        align (0.5, 0.5)
    with fade
    pause 2
    hide ch5
    hide ch overlay
    with fade
    $ quick_menu = True

    window show
    n "{i}You blink awake.{/i}"
    n "{i}The warm humidity of the swamp envelops you like a muggy blanket. Bits and pieces of the previous two days flutter through your mind as you get out of bed and start your day.{/i}"
    n "{i}Perhaps this will be one of your last days in the Naga Kingdom. It’s far from the first time you’ve said goodbye to a strange land like this, and it definitely won’t be the last.{/i}" 
    n "{i}But this time the excitement that normally accompanies the prospect of traveling somewhere new is muted, tinted gray. You can’t help but think of…{/i}"
    show kannika neutral 
    show kannika blush at center
    with dissolve
    n "{i}Kannika. Emotions well up in your chest. What will you say to her? What will she say to you? Your stomach turns in anxiety and anticipation.{/i}"
    n "{i}She’ll probably come by later tonight. But until then…{/i}"

    hide kannika
    window hide
    with dissolve

    # Intro
    show day bg
    with dissolve
    show kari neutral zorder 2 at center, sprite_highlight("kari")
    show kari frown
    with dissolve
    mc "…"
    window hide
    menu:
        "It’ll all work out.":
            window show
            mc "Yeah. Yeah, it’ll all be okay."
            show kari:
                xzoom -1.0
            n "{i}You repeat these reassurances to yourself as you start prepping ingredients for the day.{/i}"
            n "{i}Unwavering optimism has served you well for most of your life, and it never hurts to hope for the best.{/i}"
            n "{i}But… what is “the best” in this situation?"
            n "{i}Is it what’s best for Kannika? Best for the kingdom? Something in between?{/i}"
            n "{i}Maybe it’d be easier if you weren’t involved.{/i}"
            n "{i}Maybe it’d be better if you weren’t around to influence Kannika’s decisions.{/i}"
            n "{i}Maybe you should leave now, and–{/i}"

            show kari zorder 2:
                xzoom 1.0
            mc "No."
            mc "I’m not gonna just abandon her."
            mc "I want to help her however I can."
            mc "If she was there back then… I think she’d do the same."

            label passdaytime:
                play sound ["Dewdrop_MakeDrink.mp3", "Dewdrop_Clatter.mp3"] volume 0.7
                n "{i}It isn’t long before the first of today’s customers arrive, bringing an end to your introspection. Drinks pour, glasses clink, and the sun moves across the sky.{/i}"
                n "{i}Distracting yourself with the cafe works almost too well.{/i}"
                n "{i}Before you know it the sky begins to darken and the last customers of the day wander away.{/i}"
                show night bg zorder 1 with dissolve
                n "{i}Twilight approaches, and with it comes a very important decision. But unlike so long ago, it isn’t one that you’ll be making.{/i}"
                n "{i}Ultimately, it will all be up to her.{/i}"

        "Well, no use worrying about it right now.":
            window show
            show kari -frown
            mc "I’ve got a cafe to run. I owe it to my patrons to make the best drinks I can give them."
            mc "Can’t exactly do that if I’m stuck in my own head about this stuff."
            mc "Whatever happens… happens." 
            mc "And I’m sure it’ll be fine no matter how things turn out."
            
            show kari zorder 2:
                xzoom -1.0
            n "{i}Humming absentmindedly, you lose yourself in the morning preparations for the Dewdrop Cafe.{/i}"
            n "{i}The tables sparkle in the sunlight.{/i}"
            n "{i}The sign out front is freshly polished.{/i}"
            n "{i}Everything is ready for another day of delicious drinks.{/i}"


            # [IF SWAMP WATER WAS NOT WIPED UP]
            if karihelpedkannika == False:
                # show water stained counter
                show kari frown
                n "{i}Everything, that is, save for a stubborn water stain right across the middle of the countertop.{/i}"
                n "{i}You hardly notice it at first, but it quickly becomes such an eyesore it jars you out of your morning-prep flow state.{/i}"
                n "{i}You scrub at it to no effect. Maybe you should get a tablecloth to cover it up with…{/i}"
                n "{i}Or maybe it’ll be a keepsake. A reminder of this place and the people you met.{/i}"
                n "{i}…{/i}"

            # [IF SWAMP WATER WAS WIPED UP]
            if karihelpedkannika:
                n "{i}Of course, now the only thing left to do is wait.{/i}"
                n "{i}You look around your humble cafe, thinking of all the new faces you’ve seen since you arrived in the Naga Kingdom.{/i}"
                n "{i}Your eyes linger on the countertop as you remember wiping up a puddle of swamp water left in the wake of a runaway princess.{/i}"
                n "{i}You remember the lithe strength with which she pulled herself over the counter.{/i}"
                n" {i}You remember the shimmering of her scales in the lamplight, and the warm glow of her eyes as she held your gaze.{/i}"
                n "{i}…{/i}"

            call passdaytime
            # -------- Refer to passdaytime ---------
            # It isn’t long before the first of today’s customers arrive, bringing an end to your introspection. Drinks pour, glasses clink, and the sun moves across the sky.
            # Distracting yourself with the cafe works almost too well. Before you know it the sky begins to darken and the last customers of the day wander away. Twilight approaches, and with it comes a very important decision. But unlike so long ago, it isn’t one that you’ll be making.
            # Ultimately, it will all be up to her.

        "I’m too anxious to even think about running the cafe…":
            window show
            mc "I might as well start packing now. Maybe I can give this some more thought while I work…"
            show kari zorder 2:
                xzoom -1.0
            n "{i}You start muttering to yourself as you go around the Dewdrop Cafe, packing away your belongings and ingredients into their cupboards and cabinets in preparation for your departure.{/i}"
            mc "Okay, Kari, focus up."
            mc "I’ve just gotta help a princess make a decision that will shape the rest of her life."
            mc "Simple."

            # kannikaplantree menu
            $ kannikaplantree = {"clearly": False, "obviously": False}
            window hide
            menu kannikaplan: 
                "Clearly, she should get out of here." if not kannikaplan["clearly"]:
                    $ kannikaplan["clearly"] = True
                    window show
                    mc "She’s not happy here. She can’t be herself."
                    mc "I mean, she can’t even figure out who she is if she stays here."
                    mc "Not with everyone telling her who she has to be. Telling her that she isn’t allowed to be herself."
                    mc "Her parents… her country…"
                    mc "Waking up every morning and looking in the mirror and seeing a stranger, knowing that she’s lying to herself to keep everyone else happy because they expect her to be someone she’s not."
                    mc "I mean, anyone would try and get out of a situation like that, right?"
                    mc "Even if it means leaving behind family and friends and everyone you’ve ever known."
                    mc "…Right?"
                    window hide
                    menu:
                        "Right.":
                            window show
                            # continue
                        "Hm… maybe not.":
                            window show
                            mc "Being alone on the road is really hard."
                            mc "I mean, I’d travel with her if she wanted me to, of course. But if we ever had to part ways…"
                            mc "She wouldn’t have anyone to lean on or ask for help."
                            mc "I bet her mom would be furious. She might not even let Kannika come back home."
                            mc "…"
                            mc "Well, with that in mind…"
                            jump kannikaplan
                            # back

                "Obviously, she should stay." if not kannikaplan["obviously"]:
                    $ kannikaplan["obviously"] = True
                    window show
                    mc "I know it’s tough, but like… it could be a lot worse."
                    mc "I’m sure Kannika and her mom would be able to find some common ground eventually if she stayed and talked it out."
                    mc "She has her family, she has Luan, and I’m sure she has other friends."
                    mc "If she stays, she won’t be fighting with her mom anymore, and the High Elders will be happy."
                    mc "In fact, the whole kingdom would be happy. And I bet she’d make an amazing queen."
                    mc "Yeah. Yeah! And once she’s fully inherited the throne, she’ll probably be able to do things in more of her own style again!"
                    mc "All she has to do is go through with the arranged marriage and wait for however many years it takes, all while playing the part of a responsible princess."
                    mc "That’s not too bad, right?"
                    window hide
                    menu:
                        "Yeah. Definitely the best outcome overall.":
                            window show
                            #continue
                        "…Maybe it is pretty bad.":
                            window show
                            mc "I mean, Kannika’s been having a hard time already, and she hasn’t even gotten married yet."
                            mc "It might be a bit much to ask her to just deal with it until she’s established herself as queen."
                            mc "Even if it means jeopardizing her relationship with her mom."
                            mc "Hm. In that case…"
                            # back

                "She should totally… um… uh…":
                    window show
                    mc "…"
                    mc "Okay, maybe not so simple."
                    mc "I can’t just tell her to stay here. She’s clearly unhappy."
                    mc "And it’s going to get a lot harder before it ever gets easier."
                    mc "But I can’t just tell her to leave. Sure, it worked for me, but her situation is so different from mine."
                    mc "I just don’t want her to do something she’ll end up regretting…"

            n "{i}You continue to mull over your thoughts as you work.{/i}" 
            n "{i}Soon enough, the cafe is as packed-up as it’ll get. All you have to do is put the magic briefcase on the ground and unlatch it, and the whole cafe will fold up and disappear.{/i}"
            n "{i}You can leave whenever you want.{/i}"

            n "{i}But this time, you can’t leave just yet.{/i}"
            n "{i}You’re waiting for someone.{/i}" 
            n "{i}None of your previous departures were like this, and you find yourself antsy as you sit in your empty cafe, silent save for the sounds of insects and frogs.{/i}"

            n "{i}Any attempts to distract yourself or pass the time eventually return to thoughts of Kannika.{/i}" 
            n "{i}What’s the right answer?{/i}" 
            n "{i}Is there even a right answer?{/i}"

            n "{i}After what feels like an eternity the sky finally begins to darken.{/i}" 
            show night bg zorder 1 with dissolve
            n "{i}Twilight approaches, and with it comes a very important decision. But unlike so long ago, it isn’t one that you’ll be making.{/i}"

            n "{i}Ultimately, it will all be up to her.{/i}"


    # Kannika appears
    play sound ["Dewdrop_Splash.mp3", "Dewdrop_Slither.mp3"] volume 0.7
    n "{i}A tell-tale splash announces her arrival. Kannika slithers up to the Dewdrop Cafe – alone.{/i}"
    b "…Hey."
    
    $ suptree = {"sup": False, "beenluan": False}
    window hide
    menu sup:
        "‘Sup." if not suptree["sup"]: # hide this option if any other option has been chosen
            $ suptree["sup"] = True
            window show
            b "…"
            mc "…"
            mc "So…"
            mc "You come here often?"
            n "{i}Kannika’s mouth twitches into a hint of a smile. You crack a grin in return, and you can feel some of the tension leave the air.{/i}"
            b "I must admit I find your irreverence quite refreshing."
            mc "Well, it’s gotten me into plenty of trouble in the past."
            mc "Glad you like it, though."
            mc "…"
            window hide
            jump sup
            # back
        "…I’m sorry.":
            window show
            mc "I’ve been thinking a lot about the other day. I shouldn’t have responded the way I did."
            mc "I was surprised, I got emotional, and I ended up just blurting out the first things I thought of."
            mc "You were so vulnerable with me and I… Well, I kinda just shut you down."
            mc "I would’ve hated to leave things off like that. You deserve better."
            mc "I want to make it right."
            mc "That’s why tonight I’m going to do everything I can to support you. You don’t have to face this alone."
            b "…Thank you. Truly."
            b "I wanted to apologize as well."
            # continue
        "How’ve you been doing?" if not suptree["beenluan"]:
            $ suptree["sup"] = True
            $ suptree["beenluan"] = True
            window show
            b "…It’s been difficult recently."
            b "My mother grows more and more strict as the final bout approaches."
            b "I’m not even supposed to be here right now. I’ve been restricted to the castle grounds – right now I’m supposed to be finishing up on a stroll through the royal coral gardens."
            b "If it weren’t for Luan I’d probably just be locked up in my room."
            mc "Did he help you sneak out?"
            b "Yes. He’s risking quite a bit just by letting me leave the castle. If my mother ever found out he let me come see you…"
            b "I asked him to stay out of sight. Partially to give us some space to talk, and partially as a precaution if anyone else spots me."
            b "I can claim that I ran away and Luan was simply coming to find me."
            mc "Oh."
            mc "…"
            window hide
            jump sup
            # back
        "Where’s Luan?" if not suptree["beenluan"]:
            $ suptree["sup"] = True
            $ suptree["beenluan"] = True
            window show
            b "He’s nearby, just out of sight. I asked him to give us some space."
            b "Neither of us are supposed to be here in the first place. In fact, Luan is supposed to be accompanying me on a stroll through the royal coral gardens."
            b "He’s risking quite a bit just by letting me leave the castle. If my mother ever found out he let me come see you…"
            b "It’s another reason as to why I had him stay out of sight. If anyone sees me I can say that I ran away and Luan was just trying to find me."
            mc "Oh."
            mc "…"
            window hide
            jump sup
            # back
        "Thank you for coming here." if suptree["beenluan"]:
            window show
            mc "Really. It means a lot to me."
            mc "I didn’t want to leave things off the way we did the other day… and I especially didn’t want to leave you to face all of this alone."
            mc "I want to support you."
            mc "…If you’ll let me, that is."
            b "Thank you, Kari. I truly appreciate it."
            b "And I… wanted to apologize."
            # continue

    b "The other day, when I told you I was thinking about running away from the kingdom… I had expected you to be enthusiastic about it. Perhaps even excited."
    b "I didn’t expect you to have reservations. It caught me off-guard."
    b "So I snapped at you."
    b "But I spent all of yesterday thinking about what you said, and…"
    b "The concerns you raised are valid. Leaving the kingdom has consequences that I will have to reckon with sooner or later."
    b "Truth be told, you’ve taught me quite a bit about what the world is like beyond our borders, and I’ve only just begun to realize how little I truly know."
    b "I know that any objection of yours has a good reason behind it. I trust you."
    b "Sometimes more than I trust myself."
    b "I won’t get mad. I won’t storm off."
    b "What do {i}you{/i} think I should do, Kari?"
    window hide
    menu: 
        "I think you should leave.":
            jump runaway
        "Staying is the right thing to do.":
            jump arrangedmarriage
        "Whoa there, hold on a sec.":
            jump rejecttradition
        
    window hide 

    # return to main menu
    $ renpy.full_restart(transition=Fade(0.5,0.5,0.25))

label runaway:
    mc "It doesn’t have to be forever. In fact, I think you should definitely plan on coming back here eventually."
    mc "But with things like this… You shouldn’t have to put yourself through that."
    b "Do you really think I should leave? I thought you were against it."
    mc "No, no, it’s just…"
    mc "I wanted to make sure you knew what you were getting into."
    mc "It’s a really big decision to make, especially for someone in your position."
    mc "Leaving means saying goodbye to everyone and everything you’ve known your whole life."
    mc "It means severing ties, maybe forever. It means being alone in a strange land."
    mc "When I first left home, I barely had a plan. I hitchhiked, I foraged for food, I slept on benches."
    mc "And my suitcase made it possible for me to carry all my things. Without it… I’d probably just have my clothes and a couple keepsakes."
    mc "It’s really hard at first. And every night I wondered if I was doing the right thing."
    mc "Every night I considered turning around and going right back home."
    mc "Because… even if I was miserable, at least I wouldn’t be alone."
    mc "…"
    mc "But every morning I would be glad I left."
    mc "I got to discover myself, figure out what kind of person I really wanted to be."
    mc "I got to see new things, try new foods. I learned how to make drinks. I opened a cafe!"
    mc "And I know it looks like I’ve got everything figured out now, but I’m still kinda making it up as I go."
    mc "It was hard at first. But that first step is the hardest part."
    mc "You just gotta keep going."
    b "…I understand."
    b "You’re right. It isn’t as simple of a decision as I initially thought it was."
    b "I know it won’t be easy. But I also know that it’s something I need to do."
    b "I need to live for myself. Not for my mother, or for the High Elders."
    b "For me."
    b "…"
    b "Although there is one thing that will be different this time."
    mc "What’s that?"
    b "When I leave, I won’t be alone."
    n "{i}She smiles widely at you and squeezes your hand. You can’t help but smile back.{/i}"

    # RUNAWAY CUTSCSENE
    n "{i}The two of you waste no time.{/i}"
    n "{i}Kannika returns to the palace with Luan to pack some keepsakes and traveling clothes, as well as to write a note to her mother explaining why she’s choosing to leave the kingdom.{/i}"

    n "{i}You’ve already stowed your belongings and folded your cafe back up into your magic briefcase.{/i}"
    n "{i}You wait anxiously at the meeting point, memories of a similar fateful night swirling around your head.{/i}"
    n "{i}Kannika appears, shrouded in a cloak and shawl, panting in fear and exertion.{/i}"
    n "{i}She hurriedly explains that her mother caught wind of her intent to leave and ordered the Halfmoon Guard to stop her.{/i}"
    n "{i}Luan stood in their way to buy her time so that she – and you – could flee.{/i}"

    n "{i}You grab her hand and lead her away.{/i}"
    n "{i}Away from her kingdom and its suffocating decorum.{/i}"
    n "{i}Away from her mother and her uncompromising expectations.{/i}"
    n "{i}Away from a life that would have seen her grow dull and faded, nothing more than an ornament in a gilded cage.{/i}"

    n "{i}Soon enough, you leave the brackish waters of the Naga Kingdom behind.{/i}"
    n "{i}Mud and roots give way to rippling plains of tall grass.{/i}"
    n "{i}The two of you stop for a moment to catch your breath, glancing at each other and laughing as the tension of escape fades away.{/i}"

    n "{i}The night sky above you shines with countless stars. You both look up and marvel at them.{/i}"
    n "{i}You look at Kannika and see those very stars reflected in her eyes.{/i}"

    n "{i}You reach out and lace your fingers between hers.{/i}"
    n "{i}Briefcase in one hand, princess in the other, you continue onward, striding towards the uncertain future.{/i}"

    n "{i}Together.{/i}"


label arrangedmarriage:
    mc "It’s tough, I know. But there are a lot of people here who are relying on you."
    mc "The Naga Kingdom will need a new queen eventually. Not to mention Luan – what would he even do if you were gone?"
    mc "And most importantly, your mom."
    mc "Leaving now means the last memory you’ll have of her will be of fighting with her. And it’ll be the same for her."
    mc "I know right now it seems like it’s not even worth trying to change her mind, but you only really get one family."
    mc "…I wish I had resolved some things better with my own parents before I left."
    b "I… hadn’t really thought about it like that."
    b "I’ve spent all these years sneaking out of the castle at night to go explore the town or the reef, but it was always easy enough to be back in time for a new day."
    b "But if I truly left the kingdom…"
    mc "It’s a serious commitment."
    mc "And it’s definitely not as fun as I make it seem. Not at first, anyways."
    b "I just… I’m not sure if I’ll be able to be happy here."
    b "Thinking about spending every day in that castle listening to the noble matriarchs gossip and scheme…"
    n "{i}Kannika looks wistfully around the cafe. One finger idly trails across the polished wooden countertop.{/i}"
    b "I’ll miss this place."
    n "{i}You remember what Luan said about your banishment and nod sadly.{/i}"
    n "{i}The two of you share a quiet moment reminiscing on the time you shared here, from the first moment you met till now.{/i}"
    n "{i}Suddenly, Kannika’s eyes light up. Her fins flare in excitement as she meets your gaze and grabs your hand.{/i}"
    b "What if you stayed here?"
    mc "I mean, I’d love to, but Luan said that–"
    b "I’ll make her undo it."
    b "I’ll make my mother rescind your banishment."
    mc "Wait, really? How?"
    b "I’ll bargain with her. If she wants me to be a politician, then I’ll start by negotiating a deal with her."
    b "An exchange. I’ll play the part of a proper princess – on the condition that I can add you to my personal retinue."
    mc "You’d do that… for me?"
    b "You’re the one who first showed me the wonders of the world, Kari. If I won’t be seeing them myself, I’ll simply have you continue to show them to me."

    # ARRANGED MARRIAGE CUTSCENE
    n "{i}The day comes soon enough.{/i}"
    n "{i}The warrior Rawi is crowned champion, and for his boon of choice he asks for Kannika’s hand in marriage – as is his right.{/i}"
    n "{i}Kannika formally recognizes his prowess and grants his request, and everything begins to fall into place.{/i}"

    n "{i}As the Naga Kingdom readies itself for the transfer of power to a new pair of regents, Kannika convinces her mother to rescind your banishment.{/i}"
    n "{i}Shortly thereafter, you receive an invitation to become the royal barista, a personal advisor and provider of refreshments to the soon-to-be queen.{/i}"

    n "{i}High society takes some getting used to, but soon your drinks are all the rage among the nobility of the kingdom.{/i}"
    n "{i}You spend many months in the Naga Kingdom, watching as Kannika grows into her own as a ruler and quietly supporting her from behind your counter.{/i}"
    n "{i}Oh, and you end up getting along quite well with Rawi – especially after you introduce him to the marvels of protein shakes.{/i}"

    n "{i}You always knew you couldn’t stay here forever.{/i}"
    n "{i}Eventually that familiar sense of restlessness stirs in your chest, and you say your farewells to the friends you’ve made in your time here.{/i}"

    n "{i}Perhaps you’ll return to this place. Perhaps not. Kannika faced her family and found peace with her future – perhaps you can do the same.{/i}"

    n "{i}You’ve visited many nations in your travels.{/i}"
    n "{i}Most of them you remember by their drinks, or maybe their food.{/i}"
    n "{i}The people you meet are simply too numerous. Their faces bleed together in your memories like charcoal smudged with a finger.{/i}"

    n "{i}But you doubt you’ll ever forget the people you met here. Rawi, Luan… and a princess with a parasol.{/i}"


label rejecttradition:
    mc "What do you mean, you trust me more than you trust yourself?"
    b "I mean exactly what it sounds like. I may sneak out of the castle every now and then, but you’ve been living on the road for years now."
    b "By definition, you are the expert."
    window hide
    menu: 
        "I can’t make that decision for you.":
            window show
            b "I know. I’m not asking you to."
            b "But I value your insight and your advice."
        "Our situations are totally different.":
            window show
            mc "I mean, just because it was what I needed doesn’t necessarily mean it’s right for you."
            b "That may be so. However, I believe your advice will help me choose what is right for me."
    b "Please, Kari."
    b "Tell me what you truly think."
    window hide
    menu: 
        "I think you should leave.":
            jump runaway
        "Staying is the right thing to do.":
            jump arrangedmarriage
        "There’s got to be another option.":
            pass
    window show
    b "I wish there was, but there isn’t."
    window hide
    menu: 
        "I think you should leave.":
            jump runaway
        "Staying is the right thing to do.":
            jump arrangedmarriage
        "Why not?":
            pass
    window show
    b "Because we cannot change things."
    b "I can’t stand up to the High Elders. I can’t even stand up to my own mother."
    window hide
    menu:
        "I think you should leave.":
            jump runaway
        "Staying is the right thing to do.":
            jump arrangedmarriage
        "What if I did something about it?":
            pass
    window show
    mc "If the whole succession thing wasn’t the way it is, things wouldn’t be nearly as bad. For you or for your mom, I’d bet."
    mc "We’ve just gotta change the rules of the game. "
    b "Kari, I appreciate the sentiment."
    b "But you’re just one person. You don’t have a rank or title. You don’t have a powerful backer."
    b "This kingdom will always dance at the whims of the High Elders. It always has."
    b "A single person has no hope of changing such a thing."
    window hide
    menu:
        "I think you should leave.":
            jump runaway
        "Staying is the right thing to do.":
            jump arrangedmarriage
        "We’re not a single person.":
            pass
    window show
    mc "We’ll do it together."
    mc "You and me."
    mc "Oh, and Luan too, if he’s interested in upending a generational power structure based on the arbitrary rules of a group of immortal old lizards."
    b "But… how?"
    mc "We can figure something out if we put our heads together."
    mc "But let me tell you, thanks to my dad’s line of work I happen to know quite a bit about combating cultural hegemonies…"

    # REJECT TRADITION CUTSCENE
    n "{i}Defying decades-old tradition and the will of an immortal council of dragons isn’t exactly a walk in the park.{/i}"
    n "{i}It’ll take cunning, subtlety, and guerilla cafe propaganda.{/i}"

    n "{i}With some helpful tip-offs from Luan, you evade the Halfmoon Guard and operate a thriving pop-up drink stand.{/i}"
    n "{i}Every coffee or tea comes with a complementary pamphlet outlining the injustice in the current balance of power and advocating for a more equal distribution of authority.{/i}"
    n "{i}Soon, even the nobles are whispering about the infamous “Dark Barista” whose ideas are as bewitching as her beverages.{/i}"

    n "{i}Meanwhile, Kannika throws herself into court politics.{/i}"
    n "{i}She meets with the matriarchs of the noble houses, pulling strings and making deals to sway them to her side.{/i}"
    n "{i}The matriarchs are all too eager to claim more scraps of influence for themselves, and though many still subscribe to the traditions Kannika manages to garner a significant amount of support.{/i}"

    n "{i}The queen is quick to see the trajectory of this daring plan.{/i}"
    n "{i}Kannika meets with her not as her daughter, but as a soon-to-be monarch – with the political power to back up her words with action.{/i}"
    n "{i}Her mother has no choice but to acknowledge the shifting tides of power.{/i}"
    n "{i}Kannika hopes that once the kingdom’s future becomes more stable, the two of them will be able to connect as mother and daughter once again.{/i}"

    n "{i}The final round of the Dance of Ribbons is delayed because of boycotting from several major noble houses.{/i}"
    n "{i}Both the nobility and the public begin calling for a reexamination of the near-absolute authority the High Elders have over the royal family.{/i}" 

    n "{i}Kannika is about to give a speech to a massive crowd.{/i}"
    n "{i}She glances at you, a hint of anxiety on her face, and you squeeze her hand reassuringly.{/i}"
    n "{i}The two of you stand there for a moment, together, shoulder-to-shoulder, looking out at a changing kingdom and a brighter future.{/i}"

    # if player helped kannika over counter:
    #   jump sloppystyle

    n "{i}And who knows what else the future has in store for you?{/i}"

label sloppystyle:
