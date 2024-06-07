init python:
    gallery = Gallery()

    gallery.transition = dissolve
    gallery.locked_button = "../gui/gallery_assets/gallery_locked_image.png"
    gallery.hover_border = "../gui/gallery_assets/gallery_border_hover.png"
    gallery.idle_border = "../gui/gallery_assets/gallery_border_idle.png"

    # -------- ILLUSTRATIONS --------
    # ------------------------
    # ------------------------
    # ------------------------
    gallery.button("ch1_1")
    gallery.unlock_image("cg_ch1_1")

    gallery.button("night_background")
    gallery.unlock_image("night bg")

    gallery.button("day_background")
    gallery.unlock_image("day bg")

    # INSIDE BGS
    gallery.button("inside_bg")
    gallery.image("inside bg")

    gallery.button("inside_bg_water")
    gallery.unlock_image("inside bg water")
    
    gallery.button("inside_bg_stain")
    gallery.unlock_image("inside bg stain")

    gallery.button("inside_bg_kannika")
    gallery.unlock_image("inside bg kannika")


    # BAD ENDING CUTSCENES
    gallery.button("badending1")
    gallery.unlock_image("badending1")

    gallery.button("badending2")
    gallery.unlock_image("badending2")

    gallery.button("badending3")
    gallery.unlock_image("badending3")

    # RUN AWAY ENDING CUTSCENES
    gallery.button("runaway1")
    gallery.unlock_image("runaway1")

    gallery.button("runaway2")
    gallery.unlock_image("runaway2")

    gallery.button("runaway3")
    gallery.unlock_image("runaway3")

    # ARRANGED MARRAIGE ENDING CUTSCENES
    gallery.button("marriage1")
    gallery.unlock_image("marriage1")

    gallery.button("marriage2")
    gallery.unlock_image("marriage2")

    gallery.button("marriage3")
    gallery.unlock_image("marriage3")

    # REJECT TRADITION ENDING CUTSCENES
    gallery.button("reject1")
    gallery.unlock_image("reject1")

    gallery.button("reject2")
    gallery.unlock_image("reject2")

    gallery.button("reject3")
    gallery.unlock_image("reject3")


    # - CONCEPT ART & DRAFTS -
    # ------------------------
    # ------------------------
    # ------------------------

    # PROTOTYPE DRINKS
    gallery.button("prototype_tea")
    gallery.image("../gui/overlay/plain_overlay.png", "../gui/gallery_assets/gallery_drink_bg.png", im.Scale("prototype_tea.png", 1920,1080))


    # CAFE CONCEPTS
    gallery.button("night_background_concept")
    gallery.image("../gui/overlay/plain_overlay.png", "concept_art/issy_cafe_night_bg_concept.png")
    gallery.unlock("night bg")

    gallery.button("day_background_concept")
    gallery.image("../gui/overlay/plain_overlay.png", "concept_art/issy_cafe_day_bg_concept.png")
    gallery.unlock("day bg")

    gallery.button("bg_concepts")
    gallery.image("../gui/overlay/plain_overlay.png", im.Scale("concept_art/talia_bg_concepts.png", 1920, 1080))
    gallery.unlock("night bg")

    gallery.button("drink_concepts")
    gallery.image("../gui/overlay/plain_overlay.png", "concept_art/issy_drink_concepts.png")

    # CHARACTER CONCEPTS
    gallery.button("kannika_concept")
    gallery.image("../gui/overlay/plain_overlay.png", "concept_art/el_kannika_concept.jpg")

    gallery.button("kari_concepts")
    gallery.image("../gui/overlay/plain_overlay.png", "concept_art/el_kari_concepts.jpg")

    gallery.button("character_concepts")
    gallery.image("../gui/overlay/plain_overlay.png", "concept_art/el_character_concepts.jpg")
    
    # -------- FANART -------
    # ------------------------
    # ------------------------
    # ------------------------
    gallery.button("ash_kari")
    gallery.image("../gui/overlay/plain_overlay.png", im.Scale("fanart/ash_kari.PNG", 1080, 1080))

    gallery.button("ash_kannika")
    gallery.image("../gui/overlay/plain_overlay.png", im.Scale("fanart/ash_kannika.PNG", 1080, 1080))

    gallery.button("el_kannikari")
    gallery.image("../gui/overlay/plain_overlay.png", "fanart/el_kannikari.png")

    gallery.button("issy_kannika")
    gallery.image("../gui/overlay/plain_overlay.png", "fanart/issy_kannika.png")

    gallery.button("issy_kannika2")
    gallery.image("../gui/overlay/plain_overlay.png", "fanart/issy_kannika2.png")

    gallery.button("issy_luan")
    gallery.image("../gui/overlay/plain_overlay.png", "fanart/issy_luan.png")

    gallery.button("issy_luan2")
    gallery.image("../gui/overlay/plain_overlay.png", "fanart/issy_luan2.png")

    gallery.button("issy_kannikari")
    gallery.image("../gui/overlay/plain_overlay.png", "fanart/issy_kannikari.png")




    # ------ CAFE MENU -------
    # ------------------------
    # ------------------------
    # ------------------------
    gallery.button("cattail_citrus")
    gallery.image("../gui/overlay/plain_overlay.png", "../gui/gallery_assets/gallery_drink_bg.png", im.Scale("cattail_citrus.png", 1920,1080))
    gallery.unlock("cattail citrus") # the condiiton for unlocking - aka if cattail citrus is true

    gallery.button("moonjelly_tea")
    gallery.image("../gui/overlay/plain_overlay.png", "../gui/gallery_assets/gallery_drink_bg.png", im.Scale("moonjelly.png", 1920,1080))
    gallery.unlock("moon jelly")

    gallery.button("affogato_al_signo")
    gallery.image("../gui/overlay/plain_overlay.png", "../gui/gallery_assets/gallery_drink_bg.png", im.Scale("affogato_al_signo.png", 1920,1080))
    gallery.unlock("affogato al signo")

    gallery.button("otterkish_coffee")
    gallery.image("../gui/overlay/plain_overlay.png", "../gui/gallery_assets/gallery_drink_bg.png", im.Scale("otterkish_coffee.png", 1920,1080))
    gallery.unlock("otterkish coffee")

    gallery.button("humming_lavender")
    gallery.image("../gui/overlay/plain_overlay.png", "../gui/gallery_assets/gallery_drink_bg.png", im.Scale("humming_lavender.png", 1920,1080))
    gallery.unlock("humming lavender")

    gallery.button("pink_lady")
    gallery.image("../gui/overlay/plain_overlay.png", "../gui/gallery_assets/gallery_drink_bg.png", im.Scale("pink_lady.png", 1920,1080))
    gallery.unlock("pink lady")

    gallery.button("starfruit_sunset")
    gallery.image("../gui/overlay/plain_overlay.png", "../gui/gallery_assets/gallery_drink_bg.png", im.Scale("starfruit_sunset.png", 1920,1080))
    gallery.unlock("starfruit sunset")


    # ------ INGREDIENTS -------
    # ------------------------
    # ------------------------
    # ------------------------
    gallery.button("seamelon_button")
    gallery.image("../gui/overlay/plain_overlay.png", "../gui/gallery_assets/gallery_drink_bg.png", im.Scale("seamelon.png", 1920,1080))
    gallery.unlock("seamelon")

    
