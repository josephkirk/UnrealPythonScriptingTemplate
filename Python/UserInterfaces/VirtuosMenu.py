# Create Virtuos Menu
# Nguyen PHi Hung

import unreal_uiutils

# Declare Action
reloadbutton = unreal_uiutils.create_menu_button("ReloadBtn", "Reload", "import BlueprintLibrary; reload(BlueprintLibrary)")
quitbutton = unreal_uiutils.create_menu_button("QuitUnrealBtn", "Quit Unreal", "SystemLib.quit_editor()")

# create submenu in 'File' Menu
pythonsubmenu = unreal_uiutils.create_sub_submenu("File", "Virtuos", "virtuostools", "Virtuos Tools")
pythonsubmenu.add_section("common", "Common")
pythonsubmenu.add_menu_entry("common", reloadbutton)
pythonsubmenu.add_menu_entry("common", quitbutton)

# Create Standalone Menu
new_mainmenu = unreal_uiutils.create_submenu("virtuos", "Virtuos")
new_mainmenu.add_section("common", "Common", "Common")
new_mainmenu.add_menu_entry("common", reloadbutton)
new_mainmenu.add_menu_entry("common", quitbutton)