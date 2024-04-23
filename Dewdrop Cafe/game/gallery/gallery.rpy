init python:
    gallery = Gallery()

    gallery.transition = dissolve
    gallery.locked_button = "../gui/gallery_assets/gallery_locked_image.png"
    gallery.hover_border = "../gui/gallery_assets/gallery_border_hover.png"
    gallery.idle_border = "../gui/gallery_assets/gallery_border_idle.png"

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




    # -------- FANART -------
    # ------------------------
    # ------------------------
    # ------------------------
    gallery.button("ash_kari")
    gallery.image("../gui/overlay/plain_overlay.png", im.Scale("fanart/ash_kari.PNG", 1080, 1080))

    gallery.button("el_kannikari")
    gallery.image("../gui/overlay/plain_overlay.png", "fanart/el_kannikari.png")

    gallery.button("issy_kannika")
    gallery.image("../gui/overlay/plain_overlay.png", "fanart/issy_kannika.png")

    gallery.button("issy_luan")
    gallery.image("../gui/overlay/plain_overlay.png", "fanart/issy_luan.png")




    # ------ CAFE MENU -------
    # ------------------------
    # ------------------------
    # ------------------------
    gallery.button("betta_drink")
    gallery.image("../gui/overlay/plain_overlay.png", "../gui/gallery_assets/gallery_drink_bg.png", im.Scale("BettaDrink.png", 1920,1080))
    gallery.unlock("betta drink") # the condiiton for unlocking - aka if betta drink is true

    gallery.button("starfruit_sunset")
    gallery.image("../gui/overlay/plain_overlay.png", "../gui/gallery_assets/gallery_drink_bg.png", im.Scale("BettaDrink2.png", 1920,1080))
    gallery.unlock("starfruit sunset")

    gallery.button("cattail_citrus")
    gallery.image("../gui/overlay/plain_overlay.png", "../gui/gallery_assets/gallery_drink_bg.png", im.Scale("cattail_citrus.png", 1920,1080))
    gallery.unlock("cattail citrus")

    gallery.button("pink_lady")
    gallery.image("../gui/overlay/plain_overlay.png", "../gui/gallery_assets/gallery_drink_bg.png", im.Scale("pink_lady.png", 1920,1080))
    gallery.unlock("pink lady")

    gallery.button("seamelon_button")
    gallery.image("../gui/overlay/plain_overlay.png", "../gui/gallery_assets/gallery_drink_bg.png", im.Scale("seamelon.png", 1920,1080))
    gallery.unlock("seamelon")

    
