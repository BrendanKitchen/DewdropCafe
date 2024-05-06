# define characters (and their textbox stuff here || NOT IMAGES) here
define mc = Character("Kari", color="#FFB772", window_background=Image("gui/textboxes/textbox_kari.png", style="window"), callback=name_callback, cb_name="kari")
define b = Character("Kannika", color="#CBE3FF", window_background=Image("gui/textboxes/textbox_kannika.png", style="window"), callback=name_callback, cb_name="kannika")
define pb = Character("Princess Kannika", color="#CBE3FF", window_background=Image("gui/textboxes/textbox_kannika.png", style="window"), callback=name_callback, cb_name="kannika")
define princess = Character("Princess(?!)", color="#CBE3FF", window_background=Image("gui/textboxes/textbox_kannika.png", style="window"), callback=name_callback, cb_name="kannika")
define bquestionmark = Character("???", color="#CBE3FF", window_background=Image("gui/textboxes/textbox_kannika.png", style="window"), callback=name_callback, cb_name="kannika")
define g = Character("???", color="#A7AFFF", window_background=Image("gui/textboxes/textbox_luan.png", style="window"), callback=name_callback, cb_name="luan")
define pancake = Character("Pancake(?)", color="#A7AFFF", window_background=Image("gui/textboxes/textbox_luan.png", style="window"), callback=name_callback, cb_name="luan")
define lu = Character("Luan", color="#A7AFFF", window_background=Image("gui/textboxes/textbox_luan.png", style="window"), callback=name_callback, cb_name="luan")
define n = Character(callback = name_callback, cb_name = ["kari", "kannika", "luan"]) # narrator - all characters highlighted
define nn = Character(callback = name_callback, cb_name = None) # narrator_none - no characters highlighted, can specify character to be highlighted in script (refer to auto-highlight rpy)