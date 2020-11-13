# Create Virtuos Menu
# Nguyen PHi Hung

import unreal_uiutils

# Declare Action
listcutscenebtn = unreal_uiutils.create_menu_button("CutsceneListBtn", "Open Cutscene List", "unreal.log('Clicked on Sample Button')")

# Create Standalone Menu
new_mainmenu = unreal_uiutils.create_submenu("layout", "Layout Tools")
new_mainmenu.add_section("cutscene", "Cutscene", "Cutscene")
new_mainmenu.add_menu_entry("cutscene", listcutscenebtn)