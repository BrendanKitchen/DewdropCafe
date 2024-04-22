screen cafe_playlist:
    tag menu
    style_prefix "cafe_playlist"

    add "gui/overlay/plain_overlay.png" 

    add "gui/gallery_assets/music_chibis.png":
        zoom 0.5
        xzoom -1.0
        yalign 1.0
        xalign 0.2

    # hbox:
    #     xalign 0.5
    #     yalign 0.5
    #     spacing 30

    label "Cafe Playlist"

    use gallery_navigation

    # track info and controls
    vbox:
        style_prefix "track"
        yalign 0.9
        xalign 0.66
        spacing 20
        # playlist
        vbox:
            style_prefix "playlist"
            xalign 0.0
            box_reverse True
            textbutton "Pas de Deuxdrop" action music.Play("pas_de_deuxdrop.mp3")
            textbutton "Recollection" action music.Play("Recollection.mp3")
            text "song 3"
        add "gui/gallery_assets/album_cover.png":
            zoom 1.4
            xalign 0.5
        text "Connor Green"
        add "gui/gallery_assets/track_bar.png":
            xzoom 0.8
        hbox: # controls
            xalign 0.6
            spacing 50
            imagebutton auto "gui/gallery_assets/previous_track_%s.png" action music.Previous():
                yalign 0.5
            imagebutton auto "gui/gallery_assets/pause_%s.png" action music.TogglePause()
            imagebutton auto "gui/gallery_assets/next_track_%s.png" action music.Next():
                yalign 0.5
            imagebutton auto "gui/gallery_assets/shuffle_%s.png" action music.ToggleShuffle():
                yalign 0.5


style track_text:
    color "#FFF7E8"
    line_spacing 0

# style track_label_text:
#     color "#FFF7E8"
#     font "fonts/Vintage Culture.ttf"
#     size 60
#     spacing 0
#     ypos 30

style playlist_button_text:
    color "#FFF7E880"
    size 30
    selected_color "#FFF7E8"
    selected_size 60
    selected_font "fonts/Vintage Culture.ttf"
    hover_color "#CFFFD980"

style playlist_text is playlist_button_text

style cafe_playlist_label:
    ypos 51
style cafe_playlist_label_text:
    color "#FFF7E8"
    font "fonts/Vintage Culture.ttf"
    xpos 1150
    xalign 0.5
    size 96
    