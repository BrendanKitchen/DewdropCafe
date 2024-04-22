screen gallery_photos: 
    tag menu
    style_prefix "gallery_photos"

    add "../gui/overlay/plain_overlay.png" 
    
    label "Gallery"

    use gallery_navigation
    grid 2 3:
        xalign 0.66
        yalign 0.65
        add gallery.make_button(name="night_background", unlocked=im.Scale("CG/thumbnail/night_bg_thumbnail.jpg",384,216), locked=im.Scale("CG/thumbnail/cg_locked.jpg",384,216))
        add gallery.make_button("day_background", im.Scale("CG/thumbnail/day_bg_thumbnail.jpg",384,216), im.Scale("CG/thumbnail/cg_locked.jpg",384,216))
        add gallery.make_button("ch1_1", im.Scale("CG/thumbnail/ch1_1_thumbnail.jpg",384,216), im.Scale("CG/thumbnail/cg_locked.jpg",384,216))
        spacing 30

style gallery_photos_label:
    ypos 51
style gallery_photos_label_text:
    color "#FFF7E8"
    font "fonts/Vintage Culture.ttf"
    xpos 1150
    xalign 0.5
    size 96
