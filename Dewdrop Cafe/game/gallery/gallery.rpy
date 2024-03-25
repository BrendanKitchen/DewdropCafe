init python:
    gallery = Gallery()

    # -------- COMMON --------
    # ------------------------
    # ------------------------
    # ------------------------
    gallery.button("ch1_1")
    gallery.unlock_image("cg_ch1_1")

    gallery.button("night_background")
    gallery.unlock_image("night bg")

    gallery.button("day_background")
    gallery.unlock_image("day bg")

    # -------- ROUTE A -------
    # ------------------------
    # ------------------------
    # ------------------------


    # ------ CAFE MENU -------
    # ------------------------
    # ------------------------
    # ------------------------
    gallery.button("betta_drink")
    gallery.image(im.Scale("BettaDrink.png", 1920,1080))
    gallery.unlock("betta drink")

    gallery.button("starfruit_sunset")
    gallery.image(im.Scale("BettaDrink2.png", 1920,1080))
    gallery.unlock("starfruit sunset")

    gallery.button("cattail_citrus")
    gallery.image(im.Scale("cattail_citrus.png", 1920,1080))
    gallery.unlock("cattail citrus")

    gallery.button("pink_lady")
    gallery.image(im.Scale("pink_lady.png", 1920,1080))
    gallery.unlock("pink lady")

    gallery.button("seamelon_button")
    gallery.image(im.Scale("seamelon.png", 1920,1080))
    gallery.unlock("seamelon")

    
