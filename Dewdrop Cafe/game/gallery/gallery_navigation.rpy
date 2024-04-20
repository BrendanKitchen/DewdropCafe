screen gallery_navigation:
    key "game_menu":
        if main_menu:
            action ShowMenu("load")
        else:
            action Return()
    imagebutton auto "gui/quick_menu_buttons/back_%s.png":
        yalign 0.04
        xalign 0.02
        if main_menu:
            action ShowMenu("load")
        else:
            action Return()
    vbox:
        xalign 0.1
        yalign 0.5
        textbutton "Gallery" action ShowMenu("gallery_photos")
        # textbutton "Route ???" action ShowMenu("gallery_routeA")
        textbutton "Cafe Menu" action ShowMenu("gallery_cafe_menu")
        textbutton "Cafe Playlist" action ShowMenu("cafe_playlist")
        # textbutton "Chapter Select" action (ShowMenu("chapter_select"))