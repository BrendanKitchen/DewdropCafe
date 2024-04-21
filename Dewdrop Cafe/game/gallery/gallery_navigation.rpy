screen gallery_navigation:
    key "game_menu":
        if main_menu:
            action ShowMenu("preferences")
        else:
            action Return()
    imagebutton auto "gui/quick_menu_buttons/back_%s.png":
        yalign 0.04
        xalign 0.02
        if main_menu:
            action ShowMenu("preferences")
        else:
            action Return()
    vbox:
        xalign 0
        yalign 0.3
        spacing 30
        imagebutton auto "gui/gallery_buttons/gallery_%s.png" action ShowMenu("gallery_photos")
        imagebutton auto "gui/gallery_buttons/fanart_%s.png" action ShowMenu("gallery_fanart")
        imagebutton auto "gui/gallery_buttons/menu_%s.png" action ShowMenu("gallery_cafe_menu")
        imagebutton auto "gui/gallery_buttons/playlist_%s.png" action ShowMenu("cafe_playlist")
        # textbutton "Chapter Select" action (ShowMenu("chapter_select"))