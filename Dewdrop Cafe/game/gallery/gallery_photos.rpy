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
    
    label "Gallery"

    use gallery_navigation
    grid 2 3:
        xalign 0.68
        yalign 0.65
        add gallery.make_button(name="night_background", unlocked=im.Scale("CG/thumbnail/night_bg_thumbnail.jpg",384,216), tooltip="Night cafe background by {color=#4DE5BA}Talia Yaser{/color}")
        add gallery.make_button("day_background", im.Scale("CG/thumbnail/day_bg_thumbnail.jpg",384,216), tooltip="Day cafe background by {color=#4DE5BA}Talia Yaser{/color}")
        add gallery.make_button("ch1_1", im.Scale("CG/thumbnail/ch1_1_thumbnail.jpg",384,216), tooltip="Kari's memory by {color=#4DE5BA}Issy Wong{/color}")
        spacing 30

style gallery_photos_label:
    ypos 51
    xalign 0.64
style gallery_photos_label_text:
    color "#FFF7E8"
    font "fonts/Vintage Culture.ttf"
    xalign 0.5
    size 96
