screen gallery_photos: 
    tag menu
    style_prefix "gallery_photos"

    add "../gui/overlay/plain_overlay.png" 
    
    label "Gallery"

    use gallery_navigation
    grid 2 3:
        xalign 0.66
        yalign 0.65
        add gallery.make_button(name="night_background", unlocked=im.Scale("CG/thumbnail/night_bg_thumbnail.jpg",384,216), tooltip="Night cafe background by {color=#4DE5BA}Talia Yaser{/color}")
        add gallery.make_button("day_background", im.Scale("CG/thumbnail/day_bg_thumbnail.jpg",384,216), tooltip="Day cafe background by {color=#4DE5BA}Talia Yaser{/color}")
        add gallery.make_button("ch1_1", im.Scale("CG/thumbnail/ch1_1_thumbnail.jpg",384,216), tooltip="Kari's memory by {color=#4DE5BA}Issy Wong{/color}")
        spacing 30

style gallery_photos_label:
    ypos 51
style gallery_photos_label_text:
    color "#FFF7E8"
    font "fonts/Vintage Culture.ttf"
    xpos 1150
    xalign 0.5
    size 96
