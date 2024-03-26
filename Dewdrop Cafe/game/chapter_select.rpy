screen chapter_select:
    tag menu

    add "../gui/menu_bg.png" 
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 30
            text ("Chapter Select"):
                xalign 0.5
            grid 5 1:
                textbutton "Chapter 1":
                    if persistent.ch1:
                        action Start("start")
                textbutton "Chapter 2":
                    if persistent.ch2:
                        action Start("chapter2") 
                textbutton "Chapter 3":
                    if persistent.ch3:
                        action Start("chapter3") 
                textbutton "Chapter 4":
                    if persistent.ch4:
                        action Start("chapter4") 
                textbutton "Chapter 5":
                    if persistent.ch5:
                        action Start("chapter5") 
                spacing 15
            textbutton "Return" action Return():
                xalign 0.5

    