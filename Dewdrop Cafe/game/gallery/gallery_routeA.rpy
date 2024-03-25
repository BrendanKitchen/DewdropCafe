screen gallery_routeA: 
    tag menu

    add "../gui/menu_bg.png" 
    
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        use gallery_navigation
        text "???"
        # grid 3 2:
        #     add gallery.make_button(name="night_background", unlocked=im.Scale("CG/thumbnail/night_bg_thumbnail.jpg",384,216), locked=im.Scale("CG/thumbnail/cg_locked.jpg",384,216))
        #     add gallery.make_button(name="day_background", unlocked=im.Scale("CG/thumbnail/day_bg_thumbnail.jpg",384,216), locked=im.Scale("CG/thumbnail/cg_locked.jpg",384,216))
        #     add gallery.make_button(name="ch1_1", unlocked=im.Scale("CG/thumbnail/ch1_1_thumbnail.jpg",384,216), locked=im.Scale("CG/thumbnail/cg_locked.jpg",384,216))
        #     add gallery.make_button(name="ch1_1", unlocked=im.Scale("CG/thumbnail/ch1_1_thumbnail.jpg",384,216), locked=im.Scale("CG/thumbnail/cg_locked.jpg",384,216))
        #     spacing 15