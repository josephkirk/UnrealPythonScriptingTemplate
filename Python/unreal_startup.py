import unreal
import unreal_uiutils
unreal.log("""@

####################

Init Start up Script

####################

""")

import BlueprintLibrary

def register_menus():
    # declare menu entry
    testbutton1 = unreal_uiutils.create_menu_button("samplebutton", "open test ui", "unreal.log('Clicked on Sample Button')")
    # testbutton2 = unreal_uiutils.create_menu_button("testbutton2", "test button 2","common_lib.test_function('Do button 2')")
    
    # create submenu in 'File' Menu
    pythonsubmenu = unreal_uiutils.create_sub_submenu("File", "Python", "samplecustomtools", "Sample Custom Tools")
    pythonsubmenu.add_section("test")
    pythonsubmenu.add_menu_entry("test", testbutton1)
    
    # create new menu on main menu
    new_mainmenu = unreal_uiutils.create_submenu("sample_tools", "Sample Tools")
    new_mainmenu.add_section("test")
    new_mainmenu.add_menu_entry("test", testbutton1)
    
    # refresh menu
    unreal_uiutils.refresh()

register_menus()