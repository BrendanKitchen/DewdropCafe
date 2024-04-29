screen gallery_concept_art: 
    tag menu
    style_prefix "gallery_concept_art"

    add "../gui/overlay/plain_overlay.png" 
    
    label "Concept Art"

    use gallery_navigation
    grid 2 3:
        xalign 0.66
        yalign 0.65
        spacing 30
        add gallery.make_button("ash_kari", "fanart/thumbnails/ash_kari.PNG", tooltip="Kari fanart by {color=#4DE5BA}Ashley Lu{/color}")
        add gallery.make_button("el_kannikari", "fanart/thumbnails/el_kannikari.png", tooltip="Kannika and Kari fanart by {color=#4DE5BA}Elizabeth Liao{/color}")
        add gallery.make_button("issy_kannika", "fanart/thumbnails/issy_kannika.png", tooltip="Kannika fanart by {color=#4DE5BA}Issy Wong{/color}")
        # add gallery.make_button("betta_drink", im.Scale("BettaDrink.png",384,216), tooltip="by Issy Wong")
        # add gallery.make_button("starfruit_sunset", im.Scale("BettaDrink2.png",384,216), tooltip="Starfruit Sunset by Issy Wong")
        # add gallery.make_button("pink_lady", im.Scale("pink_lady.png",384,216), tooltip="Pink Lady by Issy Wong")

style gallery_concept_art_label:
    ypos 51
style gallery_concept_art_label_text:
    color "#FFF7E8"
    font "fonts/Vintage Culture.ttf"
    xpos 1150
    xalign 0.5
    size 96
