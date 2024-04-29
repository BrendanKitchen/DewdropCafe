screen gallery_cafe_menu: 
    tag menu
    style_prefix "cafe_menu"

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

    label "Cafe Menu"

    use gallery_navigation
    grid 2 3:
        xalign 0.68
        yalign 0.65
        add gallery.make_button("cattail_citrus", im.Scale("cattail_citrus.png",384,216), tooltip="{color=#4DE5BA}Cattail Citrus{/color} - Citrus-based tea with cattail garnish.")
        add gallery.make_button("seamelon_button", im.Scale("seamelon.png",384,216), tooltip="Sea melon by Issy Wong")
        spacing 30

style cafe_menu_label:
    ypos 51
    xalign 0.65
style cafe_menu_label_text:
    color "#FFF7E8"
    font "fonts/Vintage Culture.ttf"
    xalign 0.5
    size 96