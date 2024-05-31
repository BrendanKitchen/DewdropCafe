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
        #textbutton "Drinks (2)" action SetScreenVariable("curpage", "drinks_2")
        textbutton "Ingredients" action SetScreenVariable("curpage", "ingredients_1")

    use gallery_navigation
    grid 2 3:
        xalign 0.68
        yalign 0.65
        spacing 30
        if curpage == "drinks_1":
            add gallery.make_button("cattail_citrus", im.Scale("cattail_citrus.png",384,216), tooltip="{color=#4DE5BA}Cattail Citrus{/color} - Citrus-based tea with cattail garnish. Reminds you of home.")
            add gallery.make_button("moonjelly_tea", im.Scale("moonjelly.png",384,216), tooltip="{color=#4DE5BA}Moonjelly Tea{/color} - .")
            add gallery.make_button("humming_lavender", im.Scale("humming_lavender.png",384,216), tooltip="{color=#4DE5BA}Humming Lavender{/color} - Floral and sweet, like the Sun Bearony fields.")
            add gallery.make_button("otterkish_coffee", im.Scale("otterkish_coffee.png",384,216), tooltip="{color=#4DE5BA}Otterkish Coffee{/color} - Otterman coffee raised to a boil with heated sand.")
            add gallery.make_button("affogato_al_signo", im.Scale("affogato_al_signo.png",384,216), tooltip="{color=#4DE5BA}Affogato al Signo{/color} - A scoop of gelato in a cup of espresso.")
        
        if curpage == "ingredients_1":    
            add gallery.make_button("seamelon_button", im.Scale("seamelon.png",384,216), tooltip="Sea melon by Issy Wong")
        

style cafe_menu_label:
    ypos 51
    xalign 0.65
style cafe_menu_label_text:
    color "#FFF7E8"
    font "fonts/Vintage Culture.otf"
    xalign 0.5
    size 96