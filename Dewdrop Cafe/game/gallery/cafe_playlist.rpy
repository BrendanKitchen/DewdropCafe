screen cafe_playlist:
    tag menu
    style_prefix "playlist"

    add "../gui/main_menu.png"
    add "../gui/overlay/main_menu.png" 

    # hbox:
    #     xalign 0.5
    #     yalign 0.5
    #     spacing 30

    label "Cafe Playlist"

    use gallery_navigation

    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            textbutton "Pas de Deuxdrop" action music.Play("pas_de_deuxdrop.mp3")
            textbutton "Recollection" action music.Play("Recollection.mp3")

style playlist_label:
    ypos 51
style playlist_label_text:
    color "#FFF7E8"
    font "fonts/Vintage Culture.ttf"
    xpos 1150
    xalign 0.5
    size 96
    