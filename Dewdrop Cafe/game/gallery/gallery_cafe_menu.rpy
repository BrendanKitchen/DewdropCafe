screen gallery_cafe_menu: 
    tag menu
    style_prefix "cafe_menu"

    add "../gui/overlay/plain_overlay.png" 

    label "Cafe Menu"

    use gallery_navigation
    grid 2 3:
        xalign 0.66
        yalign 0.65
        add gallery.make_button(name="betta_drink", unlocked=im.Scale("BettaDrink.png",384,216), locked=im.Scale("CG/thumbnail/cg_locked.jpg",384,216))
        add gallery.make_button(name="starfruit_sunset", unlocked=im.Scale("BettaDrink2.png",384,216), locked=im.Scale("CG/thumbnail/cg_locked.jpg",384,216))
        add gallery.make_button(name="cattail_citrus", unlocked=im.Scale("cattail_citrus.png",384,216), locked=im.Scale("CG/thumbnail/cg_locked.jpg",384,216))
        add gallery.make_button(name="pink_lady", unlocked=im.Scale("pink_lady.png",384,216), locked=im.Scale("CG/thumbnail/cg_locked.jpg",384,216))
        add gallery.make_button(name="seamelon_button", unlocked=im.Scale("seamelon.png",384,216), locked=im.Scale("CG/thumbnail/cg_locked.jpg",384,216))
        spacing 15

style cafe_menu_label:
    ypos 51
style cafe_menu_label_text:
    color "#FFF7E8"
    font "fonts/Vintage Culture.ttf"
    xpos 1150
    xalign 0.5
    size 96