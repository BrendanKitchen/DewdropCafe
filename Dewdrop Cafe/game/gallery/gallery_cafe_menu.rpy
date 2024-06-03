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

    default curpage = "drinks_1" # code reference: https://lemmasoft.renai.us/forums/viewtopic.php?t=17059
    vbox:
        xalign 0.97
        yalign 0.3
        style_prefix "gallery_concept_art_page"
        textbutton "Drinks" action SetScreenVariable("curpage", "drinks_1")
        textbutton "Drinks (2)" action SetScreenVariable("curpage", "drinks_2")
        # textbutton "Ingredients" action SetScreenVariable("curpage", "ingredients_1")

    use gallery_navigation
    grid 2 3:
        xalign 0.68
        yalign 0.65
        spacing 30
        if curpage == "drinks_1":
            add gallery.make_button("cattail_citrus", im.Scale("cattail_citrus.png",384,216), tooltip="{color=#4DE5BA}{font=Vintage Culture.otf}{size=32}Cattail Citrus{/color}{/font}{/size}\nA common Catistani tea infused with citrus and garnished with cattail root. It’s not quite the same as the one your mother always made, but it never fails to remind you of home.")
            add gallery.make_button("moonjelly_tea", im.Scale("moonjelly.png",384,216), tooltip="{color=#4DE5BA}{font=Vintage Culture.otf}{size=32}Moonjelly Tea{/color}{/font}{/size}\nA fruity drink filled with small, faintly-glowing jellyfish that pop delightfully in your mouth. The jellyfish have a distinct tang but are non-toxic.")
            add gallery.make_button("humming_lavender", im.Scale("humming_lavender.png",384,216), tooltip="{color=#4DE5BA}{font=Vintage Culture.otf}{size=32}Humming Lavender{/color}{/font}{/size}\nA refreshing drink as floral and sweet as the Sun Bearony countryside. Usually enjoyed with generous amounts of honey mixed in.")
            add gallery.make_button("otterkish_coffee", im.Scale("otterkish_coffee.png",384,216), tooltip="{color=#4DE5BA}{font=Vintage Culture.otf}{size=32}Otterkish Coffee{/color}{/font}{/size}\nA dark, rich, slightly salty coffee brought to a boil with heated sand. Notably, the coffee grounds are not filtered out, and the leftover dregs can be used to tell fortunes.")
        
        if curpage == "drinks_2":
            add gallery.make_button("affogato_al_signo", im.Scale("affogato_al_signo.png",384,216), tooltip="{color=#4DE5BA}{font=Vintage Culture.otf}{size=32}Affogato Al Signo{/color}{/font}{/size}\nA shot of piping-hot espresso poured over a scoop of Swanetian gelato. The coffee surrounding the gelato is supposed to mirror the canals of the City of Swans.")
            add gallery.make_button("pink_lady", im.Scale("pink_lady.png",384,216), tooltip="{color=#4DE5BA}{font=Vintage Culture.otf}{size=32}Pink Lady{/color}{/font}{/size}\nA vibrantly pink hibiscus-apple tea based on a tropical tale of fancy. This version was improvised on the spot by a traveling barista.")

        if curpage == "ingredients_1":    
            add gallery.make_button("seamelon_button", im.Scale("seamelon.png",384,216), tooltip="Sea melon by Issy Wong")
        
    $ tooltip = GetTooltip()

    if tooltip:
        add "../gui/gallery_assets/tooltip_menu_bg.png":
            xalign 0.5
            yalign 0.96
        text "[tooltip]":
            xalign 0.5
            yalign 0.95
            color"#FFF7E8"
            xmaximum 1200
            text_align 0.5
            size 28

style cafe_menu_label:
    ypos 51
    xalign 0.65
style cafe_menu_label_text:
    color "#FFF7E8"
    font "fonts/Vintage Culture.otf"
    xalign 0.5
    size 96
