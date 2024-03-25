screen gallery_cafe_menu: 
    tag menu

    add "../gui/menu_bg.png" 

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        use gallery_navigation
        grid 3 2:
            add gallery.make_button(name="betta_drink", unlocked=im.Scale("BettaDrink.png",384,216), locked=im.Scale("CG/thumbnail/cg_locked.jpg",384,216))
            add gallery.make_button(name="starfruit_sunset", unlocked=im.Scale("BettaDrink2.png",384,216), locked=im.Scale("CG/thumbnail/cg_locked.jpg",384,216))
            add gallery.make_button(name="cattail_citrus", unlocked=im.Scale("cattail_citrus.png",384,216), locked=im.Scale("CG/thumbnail/cg_locked.jpg",384,216))
            add gallery.make_button(name="pink_lady", unlocked=im.Scale("pink_lady.png",384,216), locked=im.Scale("CG/thumbnail/cg_locked.jpg",384,216))
            add gallery.make_button(name="seamelon_button", unlocked=im.Scale("seamelon.png",384,216), locked=im.Scale("CG/thumbnail/cg_locked.jpg",384,216))
            spacing 15