screen gallery_concept_art: 
    tag menu
    style_prefix "gallery_concept_art"

    if main_menu:
        add "gui/menu_bg.png"
        add "gui/menu_kari.png"
        add "gui/menu_decor.png" 
    add "../gui/overlay/plain_overlay.png"
    add "gui/gallery_assets/gallery_chibi.png":
        zoom 0.4
        # xzoom -1.0
        yalign 1.0
        xalign 1.04

    label "Concept Art"

    default curpage = "character_concepts_1" # code reference: https://lemmasoft.renai.us/forums/viewtopic.php?t=17059
    vbox:
        xalign 0.97
        yalign 0.3
        style_prefix "gallery_concept_art_page"
        textbutton "Character Concepts" action SetScreenVariable("curpage", "character_concepts_1")
        textbutton "Cafe Concepts" action SetScreenVariable("curpage", "cafe_concepts_1")
        textbutton "Prototype Drinks" action SetScreenVariable("curpage", "prototype_drinks_1")
        textbutton "Character Fanart" action SetScreenVariable("curpage", "character_fanart_1")
        
        

    use gallery_navigation
    grid 2 3:
        xalign 0.68
        yalign 0.65
        spacing 30

        if curpage == "character_concepts_1":
            add gallery.make_button("kari_concepts", im.Scale("concept_art/thumbnails/el_kari_concepts.jpg", 384, 216), tooltip="Kari concept art by {color=#4DE5BA}Elizabeth Liao{/color}")
            add gallery.make_button("kannika_concept", im.Scale("concept_art/thumbnails/el_kannika_concept.jpg",384,216), tooltip="Kannika concept art by {color=#4DE5BA}Elizabeth Liao{/color}")
            add gallery.make_button("character_concepts", im.Scale("concept_art/thumbnails/el_character_concepts.jpg",384,216), tooltip="Character concepts by {color=#4DE5BA}Elizabeth Liao{/color}")
        
        if curpage == "cafe_concepts_1":
            add gallery.make_button("night_background_concept", im.Scale("concept_art/issy_cafe_night_bg_concept.png", 384, 216), tooltip="Cafe at night concept art by {color=#4DE5BA}Issy Wong{/color}")
            add gallery.make_button("day_background_concept", im.Scale("concept_art/issy_cafe_day_bg_concept.png", 384, 216), tooltip="Cafe at day concept art by {color=#4DE5BA}Issy Wong{/color}")
            add gallery.make_button("bg_concepts", im.Scale("concept_art/talia_bg_concepts.png", 384, 216), tooltip="Background concept art by {color=#4DE5BA}Talia Yaser{/color}")
            add gallery.make_button("drink_concepts", im.Scale("concept_art/thumbnails/issy_drink_concepts.png", 384, 216), tooltip="Cafe drink concept art by {color=#4DE5BA}Issy Wong{/color}")

        if curpage == "prototype_drinks_1":
            add gallery.make_button("betta_drink", im.Scale("BettaDrink.png",384,216), tooltip="Betta drink by {color=#4DE5BA}Issy Wong{/color}")
            add gallery.make_button("starfruit_sunset", im.Scale("BettaDrink2.png",384,216), tooltip="Starfruit Sunset {color=#4DE5BA}Issy Wong{/color}")
            add gallery.make_button("pink_lady", im.Scale("pink_lady.png",384,216), tooltip="Pink Lady by {color=#4DE5BA}Issy Wong{/color}")

        if curpage == "character_fanart_1":
            add gallery.make_button("ash_kari", "fanart/thumbnails/ash_kari.PNG", tooltip="Kari fanart by {color=#4DE5BA}Ashley Lu{/color}")
            add gallery.make_button("el_kannikari", "fanart/thumbnails/el_kannikari.png", tooltip="Kannika and Kari fanart by {color=#4DE5BA}Elizabeth Liao{/color}")
            add gallery.make_button("issy_kannika", "fanart/thumbnails/issy_kannika.png", tooltip="Kannika fanart by {color=#4DE5BA}Issy Wong{/color}")
            add gallery.make_button("issy_luan", "fanart/thumbnails/issy_luan.png", tooltip="Luan fanart by {color=#4DE5BA}Issy Wong{/color}")

style gallery_concept_art_label:
    ypos 51
    xalign 0.65
style gallery_concept_art_label_text:
    color "#FFF7E8"
    font "fonts/Vintage Culture.ttf"
    xalign 0.5
    size 96

# style gallery_concept_art_page_button:
#     yalign 0.189
#     xalign 0.61

style gallery_concept_art_page_button_text:
    size 24
    color "#FFF7E8"
    selected_color "#4DE5BA"
    hover_color "#CFFFD9"
