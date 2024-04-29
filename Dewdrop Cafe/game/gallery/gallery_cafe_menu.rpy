screen gallery_cafe_menu: 
    tag menu
    style_prefix "cafe_menu"

    add "../gui/overlay/plain_overlay.png" 

    label "Cafe Menu"

    use gallery_navigation
    grid 2 3:
        xalign 0.66
        yalign 0.65
        add gallery.make_button("betta_drink", im.Scale("BettaDrink.png",384,216), tooltip="")
        add gallery.make_button("starfruit_sunset", im.Scale("BettaDrink2.png",384,216), tooltip="Starfruit Sunset by Issy Wong")
        add gallery.make_button("cattail_citrus", im.Scale("cattail_citrus.png",384,216), tooltip="{color=#4DE5BA}Cattail Citrus{/color} - Citrus-based tea with cattail garnish.")
        add gallery.make_button("pink_lady", im.Scale("pink_lady.png",384,216), tooltip="Pink Lady by Issy Wong")
        add gallery.make_button("seamelon_button", im.Scale("seamelon.png",384,216), tooltip="Sea melon by Issy Wong")
        spacing 30

style cafe_menu_label:
    ypos 51
style cafe_menu_label_text:
    color "#FFF7E8"
    font "fonts/Vintage Culture.ttf"
    xpos 1150
    xalign 0.5
    size 96