screen gallery_fanart: 
    tag menu
    style_prefix "gallery_fanart"

    add "../gui/overlay/plain_overlay.png" 
    
    label "Fanart"

    use gallery_navigation
    grid 2 2:
        xalign 0.66
        yalign 0.55
        spacing 30
        add gallery.make_button("ash_kari", im.Scale("ash_kari.PNG", 300,300))
        add gallery.make_button("el_kannikari", im.Scale("el_kannikari.png",229,300))
        add gallery.make_button("issy_kannika", im.Scale("issy_kannika.png",263,300))
        add gallery.make_button("issy_luan", im.Scale("issy_luan.png",225,300))

style gallery_fanart_label:
    ypos 51
style gallery_fanart_label_text:
    color "#FFF7E8"
    font "fonts/Vintage Culture.ttf"
    xpos 1150
    xalign 0.5
    size 96
