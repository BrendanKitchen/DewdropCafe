screen chapter_select:
    tag menu
    style_prefix "chapter_select"

    # add "../gui/main_menu.png"
    if main_menu:
        add "gui/menu_bg.png"
        add "gui/menu_kari.png"
        add "gui/menu_decor.png" 
    add "../gui/overlay/plain_overlay.png" 

    add "../images/betta_fish_neutral.png":
        xpos -50
    add "../images/mc_neutral.png":
        xpos 1120
        zoom 0.7
        ypos 100
        

    key "game_menu" action Return()

    label "Chapter Select"
    imagebutton auto "gui/quick_menu_buttons/back_%s.png":
        style "return_button"
        yalign 0.04
        xalign 0.02
        if main_menu: 
            action Return()
        else:
            action ShowMenu("preferences")
    imagebutton auto "gui/quick_menu_buttons/sound_%s.png":
        style_prefix "sound"
        yalign 0.04
        xalign 0.98
        action Preference("all mute", "toggle")
        
    add "../gui/chapter_select_frame.png":
        xalign 0.5
        yalign 0.9
    vbox:
        xalign 0.5
        yalign 0.65
        grid 1 5:
            textbutton "Chapter 1":
                action [Play("sound", "Dewdrop_StartGame.mp3"), Start("start")]
            textbutton "Chapter 2":
                if persistent.ch2:
                    action [Play("sound", "Dewdrop_StartGame.mp3"), Start("chapter2")]
            textbutton "Chapter 3":
                if persistent.ch3:
                    action [Play("sound", "Dewdrop_StartGame.mp3"), Start("chapter3")]
            textbutton "Chapter 4":
                if persistent.ch4:
                    action [Play("sound", "Dewdrop_StartGame.mp3"), Start("chapter4")]
            textbutton "Chapter 5":
                if persistent.ch5:
                    action [Play("sound", "Dewdrop_StartGame.mp3"), Start("chapter5")]
            spacing 60
        # textbutton "Return" action Return():
            xalign 0.5


style chapter_select_label:
    ypos 65
    xalign 0.5
style chapter_select_label_text:
    color "#FFF7E8"
    font "fonts/Vintage Culture.otf"
    size 96
    