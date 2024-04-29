label chapter3:
    $ persistent.ch3 = True
    show night bg
    with dissolve
    "{i}A few days later...{/i}"
    show kari neutral at right
    with dissolve
    show kannika neutral:
        xzoom 1
        align (0.0, 0.5)
    with dissolve
    show kannika smile

    mc "You know, I've noticed you've been coming here more frequently without your guard."

    "{i}Taking a sip from her cup, Kannika smiles sadly.{/i}"
    show kannika -smile
    show kannika frown
    pb "Oh how I wish that were true." 
    show kannika -frown
    pb "Luan is still around here, just a lot further now that he knows I won't go anywhere further than your cafe."

    mc "Well, good to know he doesn't see me as a threat."
    show kari smile
    mc "Wouldn't want him scaring away my customers now."

    show kannika smile
    pb "You know, for how frequently I visit, I don't seem to know anything about you. Well, aside from you being a wandering cafe owner."
    window hide

    menu:
        "You know my name.":
            show kannika -smile
            window show
            pb "Well, yes, but I mean aside from that."
            mc "Haha, well, what would you like to know?"
        "What would you like to know?":
            show kannika -smile
            pass

    window show
    pb "You mentioned previously that you are a traveling cafe owner. How did that come about?"

    show kari -smile
    mc "Well, for starters, I'm a {b}Purrson{/b} -- if the ears and tail weren't already a giveaway."
    mc "I was born in the PRDC and spent the majority of my life there."

    pb "PRDC?"
    show kannika smile
    pb "Oh! The {b}Purrsons' Democratic Republic of Catistan{/b}! I recall being taught about that country."
    show kannika -smile
    pb "But isn't that on the opposite side of the continent? Why are you venturing so far?"

    mc "Haha, well... let's just say I had a bit of a disagreement with my parents."
    pb "Oh, I'm sorry to hear that. What was the disagreement if you don't mind me asking?"

    mc "Before I get into that, how much do you know about the PRDC?"
    pb "Not much if I'm being honest. I only know it's quite a distance away and that it's a country of Purrsons."

    mc "Pretty accurate description."
    show kari smile
    mc "The land is quite nice there: not too cold, not too hot, and the scenery is beautiful."
    show kari -smile
    show kari frown
    mc "Politically, however, they are very conservative."
    mc "They don't particularly take kind to people who aren't 'normal,' if that makes sense."

    pb "Normal? I'm not quite sure I understand."
    window hide

    menu:
        "Don't fret about it too much.":
            show kari -frown
            mc "Don't fret about it too much, just know that they have a very old-school mindset."
            pb "Ah, I see, gender constructs."
            mc "Close enough."
        "People who don't follow what they believe in.":
            pb "Again, I'm still not quite sure I follow."
            mc "Think romantic interests, identity, stuff like that."
            pb "Ah, I see now."

    pb "So, what was the reason?"

    mc "It played a role, but it wasn't necessarily the reason for my departure."
    mc "My parents have always been a little too overprotective of me."
    mc "I was someone very different growing up, someone who isn't the person you see me as."

    pb "Hard to believe someone as optimistic as you wasn't like that from the start."
    show kari smile
    window hide

    menu:
        "Haha, you'd be surprised...":
            pass
        "I try my best, y'know?":
            pass
        "What's not to be happy about?":
            mc "Well, now I get to travel, make delicious drinks, and meet amazing people. What's not to be happy about?"

    window show
    pb "So then you left because you were different?"
    show kari -smile

    mc "Kind of."
    mc "I told my parents that I wasn't the person they thought I was."
    show kari frown
    mc "They had trouble seeing things the way I saw them and we got into a big argument."
    mc "A lot of things were said at the moment that I'm sure they feel bad about now."

    show kannika angry
    pb "That's absurd! How could they just throw you out like that?"

    show kari -frown
    mc "No, they didn't throw me out."
    show kannika -angry
    mc "I left of my own accord because I didn't want to worsen things between me and my parents."
    mc "In fact, being on my own made me realize that they were caring for me, they just had a hard time showing it."

    show kannika frown
    pb "That doesn't sound like caring to me."

    mc "Well... I thought so too at first, but they were trying to protect me from the society that is the PRDC."
    mc "As much as I would like to change the PRDC's way of thinking, there's only so much I can do."

    show kannika -frown
    pb "Do you plan on going back?"
    window hide

    menu:
        "Eventually, just not right now.":
            window show
            mc "I want to give my parents some time before I decide to face them again."
            pb "That's brave of you. Admirable."
            mc "Thank you, but I promise it's not that brave."
            mc "It just feels like the right thing to do."
            mc "I'm just hoping that when I return, the tension between me and my parents will dissipate."
        "I'm not quite sure yet.":
            window show
            mc "My original plan was to leave for a bit and then return."
            mc "However, I like being on my own and traveling around the continent."
            pb "Oh, that sounds delightful."
            show kannika frown
            pb "Much better than being cooped up in a castle all day listening to politicians argue back and forth."
            show kari smile
            mc "You're only listening to the good parts, but there are a lot of dangers that come with camping in an unfamiliar territory alone."
            show kannika -frown
            show kari -smile

    pb "..."
    mc "..."

    pb "Do you resent them?"
    show kari surprised
    mc "Hm?"
    pb "Your parents."
    show kari -surprised

    mc "Resent isn't the word I would use."
    mc "I understand where they are coming from, and that is something that I choose to respect about them."
    mc "I'm more frustrated than mad at them, but eventually, they'll come around."

    show kannika frown
    pb "..."
    pb "You know, sometimes I wish I could walk away from the palace. Sometimes I wonder what my life would've been like if I wasn't of royal descent."

    show kari smile
    mc "Well, I'm always here to listen to you, {i}Your Highness{i}."

    show kannika -frown
    show kannika smile
    "{i}Kannika rolls her eyes at Kari's playful jab. While not the best attempt, she can tell that the blue haired Purrson is doing her best to lighten the heavy mood.{/i}"

    pb "You know I despise everything about that."

    mc "I kid, I kid."

    "{i}Looking up from the glasses she is cleaning, Kari notices that the sky has gotten considerably darker.{/i}"
    show kari -smile

    mc "Isn't it getting late now? Don't you have to go back to your kingdom?"
    show kannika -smile
    pb "Ugh, don't remind me."
    show kari smile
    mc "Well, as much as I enjoy your company, I don't want Luan to start attacking me on sight for holding his beloved princess captive for too long."
    show kannika smile
    pb "Unless they want to face my disappointment, I doubt that will happen."
    show kannika -smile
    pb "But you are correct, I shall take my departure now."
    pb "Goodbye, Kari."
    window hide

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