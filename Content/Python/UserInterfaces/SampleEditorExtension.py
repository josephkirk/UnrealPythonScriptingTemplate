# Create Virtuos Menu
# Nguyen PHi Hung

import unreal_uiutils
import unreal 
# Create standard menu entry
me_reloadbutton = unreal_uiutils.create_menu_button(name="ReloadBtn", label="Reload", command_string="import importlib; import unreal_startup; importlib.reload(unreal_startup)")
me_quitbutton = unreal_uiutils.create_menu_button(name="QuitUnrealBtn", label="Quit Unreal", command_string="SystemLib.quit_editor()")

# unreal_uiutils.extend_toolbar("Common",unreal_uiutils.create_separator())
# This create a button on toolboard
tb_reloadbutton = unreal_uiutils.create_toolbar_button(name="ReloadBtn", label="PyReload", command_string="import importlib; import unreal_startup; importlib.reload(unreal_startup)")

# This create a drop down button on toolboard
tb_combobutton = unreal_uiutils.create_toolbar_combo_button("Python", "Toolbar", "comboBtn")
# print(unreal_uiutils.extend_toolbar("Common",tb_combobutton))
# print(tb_combobutton.get_editor_property("script_object"))
# print(tb_combobutton.get_editor_property("toolbar_data"))

new_mainmenu = unreal_uiutils.extend_toolbar("PythonToolbar", "PythonToolbar")
new_mainmenu.add_section("python.tools", "PythonToolbar", "PythonToolbar")
new_mainmenu.add_menu_entry("python.tools", me_reloadbutton)
new_mainmenu.add_menu_entry("python.tools", me_quitbutton)

# tb_combomenu = unreal.ToolMenu()
# tb_combobutton_script.construct_menu_entry()
# tb_combobutton.add_section("common", "Python Tools")
# tb_combobutton.add_menu_entry("common", me_reloadbutton)
# tb_combobutton.add_menu_entry("common", me_quitbutton)


# This set the icon for the toolboard buttn. Read unreal_icon.py to see icon available for EditorStyle Set
tb_reloadbutton.set_icon("EditorStyle", "LevelEditor.Build")


# create submenu in 'File' Menu and register menu entry created above
pythonsubmenu = unreal_uiutils.extend_mainmenu_item("File", "PythonTools", "PythonTools", "Python Tools")
pythonsubmenu.add_section("python.file.menu", "Python Tools")
pythonsubmenu.add_menu_entry("python.file.menu", me_reloadbutton)
pythonsubmenu.add_menu_entry("python.file.menu", me_quitbutton)

# Create Standalone Menu and register menu entry created above
new_mainmenu = unreal_uiutils.extend_mainmenu("Python", "Python")
new_mainmenu.add_section("python.menu", "Python Tools")
new_mainmenu.add_menu_entry("python.menu", me_reloadbutton)
new_mainmenu.add_menu_entry("python.menu", me_quitbutton)
