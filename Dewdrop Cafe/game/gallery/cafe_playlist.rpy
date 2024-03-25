screen cafe_playlist:
    tag menu

    add "../gui/menu_bg.png" 
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        use gallery_navigation
        frame:
            vbox:
                textbutton "Pas de Deuxdrop" action music.Play("pas_de_deuxdrop.mp3")
                textbutton "Recollection" action music.Play("Recollection.mp3")