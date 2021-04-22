# 4.25 + 

import unreal

def refresh():
    unreal.ToolMenus.get().refresh_all_widgets()

def get_toolbar():
    return unreal.ToolMenus.get().find_menu("LevelEditor.LevelEditorToolBar")

def get_mainmenu():
    return unreal.ToolMenus.get().find_menu("MainFrame.MainMenu")

def get_main_submenu(name):
    return unreal.ToolMenus.get().find_menu("MainFrame.MainMenu.{}".format(name))

def create_menu_button(name, label , command_string):
    menu_button = unreal.ToolMenuEntry(name, type=unreal.MultiBlockType.MENU_ENTRY)
    menu_button.set_label(label)
    menu_button.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, "python", command_string)
    return menu_button

def create_sub_submenu(mainmenu_name, section_name, name, label, tooltips=""):
    parent_menu = get_main_submenu(mainmenu_name)
    return parent_menu.add_sub_menu(parent_menu.menu_name, section_name, name, label, tooltips)


def create_submenu(name, label, tooltip=""):
    main_menu = get_mainmenu()
    return main_menu.add_sub_menu(main_menu.menu_name, unreal.Name(), name, label , tooltip)

def parent_qt_window(qt_widget):
    unreal.parent_external_window_to_slate(qt_widget.winId())