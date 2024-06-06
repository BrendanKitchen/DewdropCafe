screen gallery_photos: 
    tag menu
    style_prefix "gallery_photos"

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

    $ tooltip = GetTooltip()

    if tooltip:
        add "../gui/gallery_assets/tooltip_bg.png":
            xalign 0.5
            yalign 0.96
        text "[tooltip]":
            xalign 0.5
            yalign 0.95
            color "#FFF7E8"
    
    label "Gallery"
    default curpage = "ill1" # code reference: https://lemmasoft.renai.us/forums/viewtopic.php?t=17059
    vbox:
        xalign 0.97
        yalign 0.3
        style_prefix "gallery_concept_art_page"
        textbutton "Illustrations (1)" action SetScreenVariable("curpage", "ill1")
        textbutton "Illustrations (2)" action SetScreenVariable("curpage", "ill2")
        textbutton "Illustrations (3)" action SetScreenVariable("curpage", "ill3")


    use gallery_navigation
    grid 2 3:
        xalign 0.68
        yalign 0.65
        spacing 30
        if curpage == "ill1":
            add gallery.make_button(name="night_background", unlocked=im.Scale("CG/thumbnail/night_bg_thumbnail.jpg",384,216), tooltip="Night cafe background by {color=#4DE5BA}Talia Yaser{/color}")
            add gallery.make_button("day_background", im.Scale("CG/thumbnail/day_bg_thumbnail.jpg",384,216), tooltip="Day cafe background by {color=#4DE5BA}Talia Yaser{/color}")
            add gallery.make_button("ch1_1", im.Scale("CG/thumbnail/ch1_1_thumbnail.jpg",384,216), tooltip="Kari thinks about home by {color=#4DE5BA}Issy Wong{/color}")
            add gallery.make_button("inside_bg", im.Scale("inside_background.png",384,216), tooltip="Inside of the cafe by {color=#4DE5BA}Talia Yaser{/color}")
            add gallery.make_button("inside_bg_water", im.Scale("inside_background_water.png",384,216), tooltip="Inside of the cafe with a water puddle by {color=#4DE5BA}Talia Yaser{/color}")
            add gallery.make_button("inside_bg_kannika", im.Scale("inside_background_kannika.png",384,216), tooltip="Inside of the cafe with a special guest by {color=#4DE5BA}Talia Yaser{/color}")
        if curpage == "ill2":
            add gallery.make_button("badending1", im.Scale("CG/chapter1/luanarrestskannika.jpg",384,216), tooltip="Kannika is taken back to the Naga Kingdom by {color=#4DE5BA}Issy Wong{/color} and {color=#4DE5BA}Ashley Lu{/color}")
            add gallery.make_button("badending2", im.Scale("CG/chapter1/pensivekari.jpg",384,216), tooltip="Kari thinks about her actions by {color=#4DE5BA}Issy Wong{/color} and {color=#4DE5BA}Ashley Lu{/color}")
            add gallery.make_button("badending3", im.Scale("CG/chapter1/badending3.png",384,216), tooltip="Kari moves on by {color=#4DE5BA}Issy Wong{/color} and {color=#4DE5BA}Ashley Lu{/color}")
            add gallery.make_button("runaway1", im.Scale("CG/run_away_ending/runaway1.png",384,216), tooltip="Luan protects Kannika by {color=#4DE5BA}Issy Wong{/color} and {color=#4DE5BA}Ashley Lu{/color}")
            add gallery.make_button("runaway2", im.Scale("CG/run_away_ending/runaway2.png",384,216), tooltip="Kari guides Kannika by {color=#4DE5BA}Issy Wong{/color} and {color=#4DE5BA}Ashley Lu{/color}")
            add gallery.make_button("runaway3", im.Scale("CG/run_away_ending/runaway3.png",384,216), tooltip="Kannika is free by {color=#4DE5BA}Issy Wong{/color} and {color=#4DE5BA}Ashley Lu{/color}")
            
        if curpage == "ill3":
            add gallery.make_button(name="night_background", unlocked=im.Scale("CG/thumbnail/night_bg_thumbnail.jpg",384,216), tooltip="Night cafe background by {color=#4DE5BA}Talia Yaser{/color}")
            add gallery.make_button("day_background", im.Scale("CG/thumbnail/day_bg_thumbnail.jpg",384,216), tooltip="Day cafe background by {color=#4DE5BA}Talia Yaser{/color}")
            add gallery.make_button("ch1_1", im.Scale("CG/thumbnail/ch1_1_thumbnail.jpg",384,216), tooltip="Kari's memory by {color=#4DE5BA}Issy Wong{/color}")
            add gallery.make_button("badending1", im.Scale("CG/chapter1/luanarrestskannika.jpg",384,216), tooltip="Kannika is taken back to the Naga Kingdom, by {color=#4DE5BA}Issy Wong{/color} and {color=#4DE5BA}Ashley Lu{/color}")
            add gallery.make_button("badending2", im.Scale("CG/chapter1/pensivekari.jpg",384,216), tooltip="Kari thinks about her actions, by {color=#4DE5BA}Issy Wong{/color} and {color=#4DE5BA}Ashley Lu{/color}")
            add gallery.make_button("badending3", im.Scale("",384,216), tooltip="Kari's memory by {color=#4DE5BA}Issy Wong{/color} and {color=#4DE5BA}Ashley Lu{/color}")

style gallery_photos_label:
    ypos 51
    xalign 0.64
style gallery_photos_label_text:
    color "#FFF7E8"
    font "fonts/Vintage Culture.otf"
    xalign 0.5
    size 96
