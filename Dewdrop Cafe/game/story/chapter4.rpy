label chapter4:
    $ persistent.ch4 = True
    show night bg
    with dissolve
    show kari neutral:
        xzoom -1
        align (1.0, 0.5)
    with dissolve
    "{i}One week later...{/i}"

    show kannika neutral:
        xzoom 1
    show kannika at left
    with MoveTransition(1.5)
    play sound "Dewdrop_Bell.mp3" volume 0.8

    show kari:
        xzoom 1

    show kari smile
    mc "Ah, Kannika! Always nice to see you."
    show kannika smile
    pb "Well, aren't you the charmer?"
    show kari -smile
    mc "Your usual, I'm presuming?"
    pb "Actually, I was considering trying something new."
    pb "I always get the same drink, and while it's delicious, I'm feeling a bit adventurous today."
    pb "Something fruity, but not too sweet."
    pb "What do you suggest?"
    window hide

    menu:
        "One of my personal favorites is the Cattail Citrus.":
            window show
            pb "That sounds intriguing, what kind of drink is it?"
            mc "It's a tea that can be served hot or cold -- it's citrus fruit infused in cattail tea."
            mc "It's a bit on the medicinal side because the tea helps soothe the stomach and the citrus helps with digestion, making it easy for the body to consume, which is is why it's popular amongst the older folks."
            mc "I will warn you, however, that the tea is quite strong, which is why the citrus is added, to help reduce the bold flavor of the tea."
            show kannika -smile
            pb "Ooh, that sounds interesting... and healthy."
            pb "How did you come up with such a concoction?"
            show kari smile
            "{i}At the question, Kari smiles fondly, reminiscing about her childhood.{/i}"
            mc "This is something that my mother used to make for me a lot when I was a child."
            mc "Every morning, she'd have me drink cattail tea because, in her words, 'It's good for your body.'"
            mc "I despised the taste of it so much that sometimes I would run away from her whenever she tried to make me drink it."
            show kannika smile
            play sound "Dewdrop_KannikaLaugh.mp3" 

            pb "Oh my, that is hilarious."
            pb "Just imagining baby Kari running around."
            "{i}Kari shoots a playful glare at Kannika{/i}."
            mc "Yeah, yeah, laugh all you want, but it was traumatizing for me as a kid."
            mc "I'd have to hold my breath while I drank it just so I wouldn't have to deal with the taste of it."
            mc "And even then, it was still strong enough for me to taste!"
            mc "Though I will say, she was indeed correct about it being good for you."
            mc "I don't recall ever getting sick for a large portion of my childhood."
            mc "Eventually, my mother started adding citrus fruit to it because citrus fruit is good for your body as well."
            show kari -smile
            mc "{i}And also because she wanted me to drink the tea without the hassle of trying to get me to drink it."
            pb "That's sweet that you decided to keep the drink that tormented you as a child."
            mc "As traumatic as it was, I decided to add it as an homage to my mother."
            mc "Though, I was very surprised by the amount of elderly folks that ordered it."
            mc "Definitely something I was not expecting."
            show kannika -smile
            play sound "Dewdrop_MakeDrink.mp3" volume 0.8

            with Fade(0.5, 0.5, 0.5)
            show drink bg zorder 3:
                align (0.5, 0.4)
            show cattail citrus zorder 3:
                align (0.5, 0.4)
            with dissolve

            "{i}Finished making the drink, Kari places it on the counter in front of Kannika, who is seated in her usual spot.{/i}"
            mc "Well, here you go."
            mc "I'm curious to see what you think of it."
            hide drink bg
            hide cattail citrus
            with dissolve

            "{i}Kannika picks up the cup and inspects the drink from different angles.{/i}"
            pb "Well, it certainly doesn't look daunting and it smells quite delectable."
            pb "..."
            "{i}Bringing the cup to her lips, she takes a cautious sip.{/i}"
            show kari smile
            "{i}To Kari's delight, once the liquid hits her tongue, the princess's face quickly scrunches up from the sourness of the beverage.{/i}"
            pb "Well, that is... quite the taste."
            mc "Haha! I told you it was strong."
            pb "Yes, I can see why you would despise this as a kid."
            mc "It definitely takes some getting used to."
            pb "The more you drink it, the more you'll get accustomed to it."
            show kari -smile
        "The Pink Lady is quite popular with the customers.":
            window show
            pb "Oooh, with a name like that, it's hard to go wrong."
            mc "It's a wapple-infused, lotus iced tea with wapple slices."
            pb "Sounds delicious."
            show kannika -smile
            play sound "Dewdrop_MakeDrink.mp3" volume 0.8 

            with Fade(0.5, 0.5, 0.5)
            show drink bg zorder 3:
                align (0.5, 0.4)
            show pink lady zorder 3:
                align (0.5, 0.4)
            with dissolve
            
            "{i}Kari quickly makes a Pink Lady and sets in in front of Kannika.{/i}"
            hide drink bg
            hide pink lady
            with dissolve

            pb "Where did this drink come from?"
            mc "I want to say it was one of the original drinks I made when I was first starting my cafe."
            mc "At that time, I was around the {b}Phibiman Kingdom{/b} and I only had about a few customers."
            mc "While walking around one of the temples, I decided to do one of the tea ceremonies that they offered."
            mc "They brewed a pot of lotus tea and served some wapple slices with it."
            mc "The sweetness from the wapple complimented the subtle floral taste of the tea -- I made sure to bring extras for my cafe."
            pb "That sounds like a wonderful experience."
        "Nothing quite fits what you're looking for.":
            window show
            show kari frown
            mc "I don't think I have anything that quite fits what you're looking for."
            show kannika -smile
            show kannika frown
            pb "Aw, that's unfortunate."
            show kannika -frown
            pb "Well, my usual it is then."
            show kari -frown
            mc "Coming right up!"
            play sound "Dewdrop_MakeDrink.mp3" volume 0.8

            with Fade(0.5, 0.5, 0.5)
            show starfruit sunset zorder 3:
                align (0.5, 0.4)
            "{i}Finished making her usual, Kari sets the Starfruit Sunset down in front of Kannika{/i}."
            hide starfruit sunset
            pb "I remember you mentioned that this drink was something you created from the Floral Kingdom."
            mc "Wow, I'm surprised you remembered that."
            mc "It's a sweet story actually of how I made it."
            show kannika smile
            pb "Oooh, do tell."
            show kari smile
            mc "Well, it was just as I was beginning to close the shop for the day."
            mc "One of my regulars came with her child trotting behind her."
            mc "Cute little guy he was."
            mc "She handed me a basket of starfruit as a thank-you gift."
            mc "She told me that starfruits were their native fruits and she thought that they would make for a good drink."
            mc "I think in total I tried about... seven? eight? different recipes."
            mc "Amongst all of them, the one you're drinking was the most liked."
            mc "A starfruit puree with a hint of mint, combined with cream soda, and topped with starfruit slices, blueberries, and mint leaf garnish."
            mc "The next time I saw her, I let her name the drink and she called it 'Starfruit Sunset' because of the coloring."
            pb "Aw, that's such a lovely story."
            show kannika -smile
            show kari -smile

    pb "I've noticed that the drinks you make are based on your travels."
    mc "That is correct."
    mc "I try to make a drink based on each of the different regions that I visit."
    show kannika surprised
    pb "Does that mean that you will make something based on the Naga Kingdom as well?"
    show kari smile
    mc "That's the plan!"
    show kari -smile
    show kannika -surprised
    show kari frown
    mc "Though, I don't know much about your kingdom aside from what you've told me."
    mc "And I haven't been able to explore your kingdom that much because I've been getting quite the amount of customers."
    show kannika smile
    pb "Oh, allow me!"
    show kari -frown
    show kannika -smile
    window hide

    # kannika leaves the scene for a few seconds, then returns
    show kannika:
        xzoom -1
    show kari surprised
    show kannika at offscreenleft
    with MoveTransition(0.5)
    pause 2.5
    show kannika:
        xzoom 1
    show kannika at left
    with MoveTransition (1.0)

    show drink bg zorder 3:
        align (0.5, 0.4)
    show seamelon zorder 3:
        align (0.5, 0.4)
    with dissolve

    show kannika smile
    window show
    pb "Here! I think these should work!"
    hide drink bg
    hide seamelon
    with dissolve

    mc "Oh my Lanta, they're ginormous!"
    show kari -surprised
    mc "What are they!?"

    pb "They're seamelons, my kingdom's native fruit!"
    pb "They're also one of my favorite fruits."
    pb "They have a soft crunch to them and have plenty of juice inside of them, making them perfect for drinks!"
    pb "Here, cut one open!"

    "{i}Taking a seamelon from Kannika's hand, Kari pulls out a small knife and slices the fruit in half."

    show kari surprised
    mc "Oh wow, that color is just..."
    pb "Gorgeous right?"
    show kari -surprised
    mc "I've never seen anything like it."
    "{i}Kari cuts the fruit into smaller pieces and eats a slice, her eyes lighting up as the flavors erupt in her mouth.{/i}"
    show kari surprised
    mc "!"
    mc "Wow, this tastes amazing!"
    
    pb "Joy! I'm so glad you like it!"

    show kari -surprised
    show kari smile
    mc "This will be perfect for my menu!"
    mc "Would you like to help me make a drink?"

    "{i}Kannika's fins perk up from the suggestion as she quickly slides out of her seat.{/i}"

    pb "I would love to!"

    mc "Here, I'll show you how to prepare fruit for drink making."

    show kari -smile
    show kannika -smile
    "{i}Kannika makes her way around the counter and stands beside Kari.{/i}"
    "{i}Kari hands Kannika the knife and moves to stand behind her, grasping one of the princess' hands in each of her own as she guides her through the motion.{/i}"
    show kannika surprised
    mc "Once you cut them into sections, you'll run the knife along the edge to separate the flesh from the rind."
    show kannika -surprised
    "{i}Together, they begin to cut the seamelon, with Kari carefully guiding Kannika along the way.{/i}"
    show kari smile
    mc "Yeah, just like that."
    show kannika smile
    pb "This is so fun!"
    mc "I'm glad you're enjoying this."
    show kari -smile
    show kannika -smile
    pb "What do we do now?"
    mc "Next is the part where me mix the fruit with different bases to see how they taste with them."
    window hide

    $ seamelon_tested = {"cattail": False, "lotus": False, "soda": False}
    menu seamelon_test:
        "Let's try the cattail tea." if not seamelon_tested["cattail"]:
            $ seamelon_tested["cattail"] = True
            window show 
            "{i}The seamelon steeps with the cattail tea before Kari pours the liquid out into two cups.{/i}"
            mc "..."
            pb "..."
            show kari surprised
            show kannika surprised
            mc "Ahem, I..."
            pb "Wow, uhm..."
            show kannika -surprised
            pb "I do not think that was a success."
            show kari -surprised
            mc "No, that definitely was not a success."
            pb "That tasted as if a tilapia had gone wrong."
            mc "Not quite sure I understand what that means, but I do agree it doesn't taste right."
            mc "The melon probably didn't have a strong enough flavor to compliment the taste of the cattail which is why it tasted like that."
            jump seamelon_test
        "Let's try the lotus tea." if not seamelon_tested["lotus"]:
            $ seamelon_tested["lotus"] = True
            window show 
            "{i}The seamelon steeps with the lotus tea before Kari pours the liquid out into two cups.{/i}"
            pb "Oh, this tastes marvelous."
            mc "I agree, the flavors seem to go well with each-"
            pb "Ew, my Lanta! What is this!?"
            "{i}Sour faces appear on both Kari and Kannika's faces as the taste of the beverage begins to devolve into something repulsive.{/i}"
            show kari frown
            mc "That started fine... but that aftertaste..."
            show kannika frown
            pb "It tasted like an undercooked mackerel."
            show kari -frown
            show kannika -frown
            mc "Nope, not this one then."
            pb "Agreed."
            jump seamelon_test
        "Let's try the cream soda." if not seamelon_tested["soda"]:
            $ seamelon_tested["soda"] = True
            window show 
            "{i}Kari pours cream soda over a bowl of cut-up seamelon.{/i}"
            pb "This looks like... a combination."
            mc "That's one way to put it."
            mc "A little scared, not going to lie."
            "{i}Apprehensively, both Kari and Kannika eat a piece of the fruit that is soaked with the cream soda."
            show kari surprised
            show kannika surprised
            mc "...!"
            pb "...!"
            pb "That is quite good."
            mc "I'm shocked, myself."
            show kari -surprised
            show kannika -surprised
            show kari smile
            show kannika smile
            mc "The sweetness from the soda goes well with the melon and the carbonation helps make the crunch more satisfying."
            pb "It's as if I'm eating freshly cut salmon."
            mc "Well, I'll say that one is a success."
            pb "As do I."
            show kari -smile
            show kannika -smile
    
    pb "However, it still feels as if it's missing something."
    mc "You're right. Though I'm not sure what exactly."
    pb "How about we try adding another fruit?"
    pb "Maybe that will help."
    mc "Hmm..."
    mc "I have extra wapples and starfruit we could try."
    window hide

    menu:
        "Let's try the wapple":
            window show
            "{i}Kari adds the wapples to the bowl of the cream soda and seamelon mixture.{/i}"
            pb "I thought the melon with the cream soda was weird enough, but the wapple slices certainly don't make it look any better."
            mc "Well, the odd one ended up being the best one, so I'm hoping that this will produce similar results."
        "Let's try the starfruit":
            window show
            "{i}Kari adds the starfruit to the bowl of the cream soda and seamelon mixture.{/i}"
            mc "Theoretically, this should be fine because I use the same cream soda in Starfruit Sunsets."
            "{i}Kari and Kannika each take a bite of the new concoction, but their faces quickly scrunch up in disgust.{/i}"
            pb "{i}Blegh!{/i}"
            pb "That did not taste nearly as good as it was when they were separated."
            mc "That's so weird that they don't go together."
            mc "I think it's because the two fruits have such a different taste that they clash with each other."
            show kannika frown
            pb "That's so disappointing."
            mc "Let's try the wapples."
            mc "I think we'll have better success with that."
            show kannika -frown
            "{i}Taking the other seamelon that Kannika brought, Kari prepares a new bowl of seamelon, cream soda, and wapple slices.{/i}"
            pb "This doesn't look nearly as appetizing as the starfruit."
            mc "A shame, really. But anything ought to be better than what we just tasted."
    
    "{i}Taking a deep breath, both Kari and Kannika take a bite of the melon and wapple together.{/i}"
    show kari surprised
    show kannika surprised
    
    pb "Mmmm!"
    mc "It's perfect."
    pb "Splendid!"
    show kari -surprised
    show kannika -surprised
    mc "With a little more tampering, I think this is ready to be served."
    show kannika smile
    pb "Really? do you mean it?"
    mc "Of course! All it's missing now is a name."
    show kari smile
    mc "For giving me the melon, would you like to do the honors of naming it?"
    "{i}At the offer, Kannika's face lights up and her smiles grows even wider than it already was.{/i}"
    pb "I would love to!"
    show kari -smile
    pb "How about we name it..."

    # PLAYER NAMES THE ITEM WITH USER INPUT
    python:
        seamelon_item = renpy.input("{i}Enter a name for the new menu item:", length=64)
        seamelon_item = seamelon_item.strip()

        # IF THE PLAYER DOESN'T NAME THE THING, HERE'S A DEFAULT NAME TO USE 
        if not seamelon_item:
            seamelon_item = "WHY DIDN'T YOU NAME THE THING"
    
    show kari smile
    mc "{color=#3AC8A0}[seamelon_item]{/color} is now the newest addition to Dewdrop Cafe!"
    window hide
    pause 1.0
    scene black
    with fade
    # hide kari
    # hide kannika 
    # with dissolve
    # with Fade (0.5, 1.0, 0.5)
    
    jump chapter5