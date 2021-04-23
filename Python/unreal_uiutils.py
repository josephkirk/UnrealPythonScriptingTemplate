# 4.25 + 

import unreal

def refresh():
    unreal.ToolMenus.get().refresh_all_widgets()

def get_toolbar():
    return unreal.ToolMenus.get().find_menu("LevelEditor.LevelEditorToolBar")

def get_toolbar_item(name):
    return unreal.ToolMenus.get().find_menu("LevelEditor.LevelEditorToolBar.{}".format(name))

def get_mainmenu():
    return unreal.ToolMenus.get().find_menu("MainFrame.MainMenu")

def get_mainmenu_item(name):
    return unreal.ToolMenus.get().find_menu("MainFrame.MainMenu.{}".format(name))

def create_tool_menu_entry(name, label , command_string, entry_type=unreal.MultiBlockType.MENU_ENTRY):
    toolbar_button = unreal.ToolMenuEntry(name, type=entry_type)
    toolbar_button.set_label(label)
    toolbar_button.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, "python", command_string)
    return toolbar_button

def create_menu_button(name, label , command_string):
    return create_tool_menu_entry(name, label , command_string)

def create_toolbar_button(name, label , command_string):
    return create_tool_menu_entry(name, label , command_string, entry_type=unreal.MultiBlockType.TOOL_BAR_BUTTON)

def create_toolbar_combo_button(name, label , command_string):
    return create_tool_menu_entry(name, label , command_string, entry_type=unreal.MultiBlockType.TOOL_BAR_COMBO_BUTTON)

def create_editable_text(name, label , command_string):
    return create_tool_menu_entry(name, label , command_string, entry_type=unreal.MultiBlockType.EDITABLE_TEXT)

def create_widget(name, label , command_string):
    return create_tool_menu_entry(name, label , command_string, entry_type=unreal.MultiBlockType.WIDGET)

def create_heading(name, label , command_string):
    return create_tool_menu_entry(name, label , command_string, entry_type=unreal.MultiBlockType.HEADING)

def create_separator(name, label , command_string):
    return create_tool_menu_entry(name, label , command_string, entry_type=unreal.MultiBlockType.SEPARATOR)

def extend_mainmenu_item(mainmenu_name, section_name, name, label, tooltips=""):
    parent_menu = get_mainmenu_item(mainmenu_name)
    return parent_menu.add_sub_menu(parent_menu.menu_name, section_name, name, label, tooltips)

def extend_toolbar(name, label, tooltip=""):
    toolbar = get_toolbar()
    return toolbar.add_sub_menu(toolbar.menu_name, unreal.Name(), name, label , tooltip)

def extend_mainmenu(name, label, tooltip=""):
    main_menu = get_mainmenu()
    return main_menu.add_sub_menu(main_menu.menu_name, unreal.Name(), name, label , tooltip)

def parent_qt_window(qt_widget):
    unreal.parent_external_window_to_slate(qt_widget.winId())