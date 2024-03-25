screen gallery_navigation:
    frame:
        vbox:
            textbutton "Common" action ShowMenu("gallery_common")
            textbutton "Route ???" action ShowMenu("gallery_routeA")
            textbutton "Cafe Menu" action ShowMenu("gallery_cafe_menu")
            textbutton "Cafe Playlist" action ShowMenu("cafe_playlist")
            textbutton "Return":
                action Return()