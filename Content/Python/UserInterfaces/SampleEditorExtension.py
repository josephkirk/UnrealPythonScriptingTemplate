# Create Virtuos Menu
# Nguyen PHi Hung

import unreal_uiutils
from unreal_utils import AssetRegistryPostLoad
import unreal


def extend_editor():
    # Create standard menu entry
    me_reloadbutton = unreal_uiutils.create_menu_button(
        name="ReloadBtn",
        label="Reload",
        command_string="import importlib; import unreal_startup; importlib.reload(unreal_startup); unreal_startup.reload()",
    )
    me_quitbutton = unreal_uiutils.create_menu_button(
        name="QuitUnrealBtn",
        label="Quit Unreal",
        command_string="SystemLib.quit_editor()",
    )

    # This create a button on toolboard
    tb_reloadbutton = unreal_uiutils.create_toolbar_button(
        name="ReloadBtn",
        label="PyReload",
        command_string="import importlib; import unreal_startup; importlib.reload(unreal_startup); unreal_startup.reload()",
    )

    # This create a drop down button on toolboard
    tb_combobutton = unreal_uiutils.create_toolbar_combo_button(
        "comboBtn", "python.tools"
    )
    #TODO: Find out where it is possible to register a new context menu for combo button

    # create submenu in 'File' Menu and register menu entry created above
    pythonsubmenu = unreal_uiutils.extend_mainmenu_item(
        "File", "PythonTools", "PythonTools", "Python Tools"
    )
    pythonsubmenu.add_section("python.file.menu", "Python Tools")
    pythonsubmenu.add_menu_entry("python.file.menu", me_reloadbutton)
    pythonsubmenu.add_menu_entry("python.file.menu", me_quitbutton)

    # Create Standalone Menu and register menu entry created above
    new_mainmenu = unreal_uiutils.extend_mainmenu("Python", "Python")
    section = new_mainmenu.add_section("python.menu", "Python Tools")
    new_mainmenu.add_menu_entry("python.menu", me_reloadbutton)
    new_mainmenu.add_menu_entry("python.menu", me_quitbutton)
    new_entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
        new_mainmenu.menu_name,
        "submenu",
        "Test Sub Menu",
        "nothing here",
        unreal.ToolMenuStringCommandType.COMMAND,
        "command",
        "",
    )
    print(f"Script Object: {new_entry.script_object}")

    # Extend Asset Context Menu
    sub_asset_context_menu = unreal_uiutils.extend_toolmenu(unreal_uiutils.get_asset_context_menu(), "PythonAssetContextMenu", "Python Asset Actions")
    sub_asset_context_menu.add_section("python.assetmenu", "Tools")
    action_sampleassetprint = unreal_uiutils.create_menu_button(
        name="SampleAssetTool",
        label="Print Selected Assets",
        command_string='print(UtilLibrary.get_selected_assets())',
    )
    sub_asset_context_menu.add_menu_entry("python.assetmenu", action_sampleassetprint)

    # Extend Asset Context Menu - Only show for Level Sequence Asset
    sequence_contextmenu = unreal_uiutils.get_sequence_asset_context_menu()
    sub_sequence_context_menu = unreal_uiutils.extend_toolmenu(sequence_contextmenu, "PythonSequenceContextMenu", "Python Sequence Actions")
    sub_sequence_context_menu.add_section("python.sequencemenu", "Tools")
    action_samplesequenceprint = unreal_uiutils.create_menu_button(
        name="SampleSequenceTool",
        label="Print Selected Assets",
        command_string='print(UtilLibrary.get_selected_assets())',
    )
    sub_sequence_context_menu.add_menu_entry("python.sequencemenu", action_samplesequenceprint)

    # Extend Actor Context Menu
    actor_context_menu = unreal_uiutils.get_actor_context_menu()
    actor_context_menu.add_section("python.actoractions", "Python Tools")
    #!NOTE: The submenu can only be seen when right click in viewport and not the outliner
    sub_actor_context_menu = actor_context_menu.add_sub_menu(actor_context_menu.menu_name, "python.actoractions", "PythonActorContextMenu", "Python Actor Actions")
    # is_sub_actor_context_menu_registered = unreal.ToolMenus.get().is_menu_registered(sub_actor_context_menu.menu_name)
    # if not is_sub_actor_context_menu_registered:
        # unreal.ToolMenus.get().register_menu(sub_actor_context_menu.menu_name, actor_context_menu.menu_name)
    # print("{} - is registered {}".format(sub_actor_context_menu.menu_name, is_sub_actor_context_menu_registered))
    sub_actor_context_menu.add_section("python.actormenu", "Tools")
    action_sampleactorprint = unreal_uiutils.create_menu_button(
        name="SampleActorTool",
        label="Print Selected Actor",
        command_string='print(LevelLibrary.get_selected_level_actors())',
    )
    sub_actor_context_menu.add_menu_entry("python.actormenu", action_sampleactorprint)
    # actor_context_menu.add_menu_entry("python.actoractions", action_sampleactorprint)

# AssetRegistryPostLoad.register_callback(extend_editor)
extend_editor()