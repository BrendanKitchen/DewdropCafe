screen gallery_navigation:
    # key "game_menu":
    #     if main_menu:
    #         action ShowMenu("preferences")
    #     else:
    #         action Return()
    key "game_menu" action Return()
    imagebutton auto "gui/quick_menu_buttons/back_%s.png":
        yalign 0.045
        xalign 0.023
        if main_menu:
            action ShowMenu("preferences")
        else:
            action Return()
    imagebutton auto "gui/quick_menu_buttons/sound_%s.png":
        style_prefix "sound"
        yalign 0.04
        xalign 0.98
        action Preference("all mute", "toggle")
        
    vbox:
        xalign 0
        yalign 0.3
        spacing 30
        imagebutton auto "gui/gallery_buttons/menu_%s.png" action ShowMenu("gallery_cafe_menu")
        imagebutton auto "gui/gallery_buttons/playlist_%s.png" action ShowMenu("cafe_playlist")
        imagebutton auto "gui/gallery_buttons/gallery_%s.png" action ShowMenu("gallery_photos")
        imagebutton auto "gui/gallery_buttons/concept_art_%s.png" action ShowMenu("gallery_concept_art")
        
        # textbutton "Chapter Select" action (ShowMenu("chapter_select"))

    $ tooltip = GetTooltip()

    if tooltip:
        add "../gui/gallery_assets/tooltip_bg.png":
            xalign 0.5
            yalign 0.96
        text "[tooltip]":
            xalign 0.5
            yalign 0.95
            color "#FFF7E8"