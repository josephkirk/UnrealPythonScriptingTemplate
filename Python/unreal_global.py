import unreal

UtilLibrary = unreal.EditorUtilityLibrary
"""
    rename_asset(asset, new_name) -> None
    get_selection_set() -> Array(Actor)
    get_selection_bounds() -> (origin=Vector, box_extent=Vector, sphere_radius=float)
    get_selected_blueprint_classes() -> Array(type(Class))
    get_selected_assets() -> Array(Object)
    get_selected_asset_data() -> Array(AssetData)
    get_actor_reference(path_to_actor) -> Actor
"""

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
"""
    rename_referencing_soft_object_paths(packages_to_check, asset_redirector_map)

    rename_assets_with_dialog(assets_and_names, auto_checkout=False)

    rename_assets(assets_and_names)

    open_editor_for_assets(assets)

    import_asset_tasks(import_tasks)

    import_assets_with_dialog(destination_path)

    import_assets_automated(import_data)

    find_soft_references_to_object(target_object)

    export_assets_with_dialog(assets_to_export, prompt_for_individual_filenames)

    export_assets(assets_to_export, export_path)

    duplicate_asset_with_dialog_and_title(asset_name, package_path, original_object, dialog_title)

    duplicate_asset_with_dialog(asset_name, package_path, original_object)

    duplicate_asset(asset_name, package_path, original_object)

    create_unique_asset_name(base_package_name, suffix)

    create_asset_with_dialog(asset_name, package_path, asset_class, factory, calling_context="None")

    create_asset(asset_name, package_path, asset_class, factory, calling_context="None")
"""

AssetLibrary = unreal.EditorAssetLibrary
"""
    sync_browser_to_objects(cls, asset_paths)

    set_metadata_tag(cls, object, tag, value)

    save_loaded_assets(cls, assets_to_save, only_if_is_dirty=True)

    save_loaded_asset(cls, asset_to_save, only_if_is_dirty=True)

    save_directory(cls, directory_path, only_if_is_dirty=True, recursive=True)
        
    save_asset(cls, asset_to_save, only_if_is_dirty=True)

    rename_loaded_asset(cls, source_asset, destination_asset_path)

    rename_directory(cls, source_directory_path, destination_directory_path)

    rename_asset(cls, source_asset_path, destination_asset_path)

    remove_metadata_tag(cls, object, tag)

    make_directory(cls, directory_path)

    load_blueprint_class(cls, asset_path)

    load_asset(cls, asset_path)

    list_assets(cls, directory_path, recursive=True, include_folder=False)

    list_asset_by_tag_value(cls, tag_name, tag_value)

    get_tag_values(cls, asset_path)

    get_path_name_for_loaded_asset(cls, loaded_asset)

    get_metadata_tag_values(cls, object)

    get_metadata_tag(cls, object, tag)

    find_package_referencers_for_asset(cls, asset_path, load_assets_to_confirm=False)

    find_asset_data(cls, asset_path)

    duplicate_loaded_asset(cls, source_asset, destination_asset_path)

    duplicate_directory(cls, source_directory_path, destination_directory_path)

    duplicate_asset(cls, source_asset_path, destination_asset_path)

    does_directory_have_assets(cls, directory_path, recursive=True)

    does_directory_exist(cls, directory_path)

    does_asset_exist(cls, asset_path)

    do_assets_exist(cls, asset_paths)

    delete_loaded_assets(cls, assets_to_delete)

    delete_loaded_asset(cls, asset_to_delete)

    delete_directory(cls, directory_path)

    delete_asset(cls, asset_path_to_delete)

    consolidate_assets(cls, asset_to_consolidate_to, assets_to_consolidate)

    checkout_loaded_assets(cls, assets_to_checkout)

    checkout_loaded_asset(cls, asset_to_checkout)

    checkout_directory(cls, directory_path, recursive=True)

    checkout_asset(cls, asset_to_checkout)
"""

FilterLibrary = unreal.EditorFilterLibrary
"""
    Utility class to filter a list of objects. Object should be in the World Editor.

    by_selection(cls, target_array, filter_type=EditorScriptingFilterType.INCLUDE)

    by_level_name(cls, target_array, level_name, filter_type=EditorScriptingFilterType.INCLUDE)

    by_layer(cls, target_array, layer_name, filter_type=EditorScriptingFilterType.INCLUDE)

    by_id_name(cls, target_array, name_sub_string, string_match=EditorScriptingStringMatchType.CONTAINS, filter_type=EditorScriptingFilterType.INCLUDE)

    by_class(cls, target_array, object_class, filter_type=EditorScriptingFilterType.INCLUDE)

    by_actor_tag(cls, target_array, tag, filter_type=EditorScriptingFilterType.INCLUDE)

    by_actor_label(cls, target_array, name_sub_string, string_match=EditorScriptingStringMatchType.CONTAINS, filter_type=EditorScriptingFilterType.INCLUDE, ignore_case=True)

"""

AutomationLibrary = unreal.AutomationLibrary
"""
    take_high_res_screenshot(cls, res_x, res_y, filename, camera=None, mask_enabled=False, capture_hdr=False, comparison_tolerance=ComparisonTolerance.LOW, comparison_notes="")

    take_automation_screenshot_of_ui(cls, world_context_object, latent_info, name, options)
     
    take_automation_screenshot_at_camera(cls, world_context_object, latent_info, camera, name_override, notes, options)
        
    take_automation_screenshot(cls, world_context_object, latent_info, name, notes, options)
        
    set_scalability_quality_to_low(cls, world_context_object)
        
    set_scalability_quality_to_epic(cls, world_context_object)
        
    set_scalability_quality_level_relative_to_max(cls, world_context_object, value=1)
       
    get_stat_inc_max(cls, stat_name)
        
    get_stat_inc_average(cls, stat_name)
       
    get_stat_exc_max(cls, stat_name)
        
    get_stat_exc_average(cls, stat_name)
        
    get_stat_call_count(cls, stat_name)
        
    get_default_screenshot_options_for_rendering(cls, tolerance=ComparisonTolerance.LOW, delay=0.200000)
       
    get_default_screenshot_options_for_gameplay(cls, tolerance=ComparisonTolerance.LOW, delay=0.200000)
        
    enable_stat_group(cls, world_context_object, group_name)
       
    disable_stat_group(cls, world_context_object, group_name)
       
    automation_wait_for_loading(cls, world_context_object, latent_info)
       
    are_automated_tests_running(cls)
       
    add_expected_log_error(cls, expected_pattern_string, occurrences=1, exact_match=False)
"""

LevelLibrary = unreal.EditorLevelLibrary
"""
    spawn_actor_from_object(object_to_use, location, rotation=[0.000000, 0.000000, 0.000000]) -> Actor
    spawn_actor_from_class(actor_class, location, rotation=[0.000000, 0.000000, 0.000000]) -> Actor
    set_selected_level_actors(actors_to_select) -> None
    set_level_viewport_camera_info(camera_location, camera_rotation) -> None
    set_current_level_by_name(level_name) -> bool
    set_actor_selection_state(actor, should_be_selected) -> None
    select_nothing() -> None
    save_current_level() -> bool
    save_all_dirty_levels() -> bool
    replace_mesh_components_meshes_on_actors(actors, mesh_to_be_replaced, new_mesh) -> None
    replace_mesh_components_meshes(mesh_components, mesh_to_be_replaced, new_mesh) -> None
    replace_mesh_components_materials_on_actors(actors, material_to_be_replaced, new_material) -> None
    replace_mesh_components_materials(mesh_components, material_to_be_replaced, new_material) -> None
    pilot_level_actor(actor_to_pilot) -> None
    new_level_from_template(asset_path, template_asset_path) -> bool
    new_level(asset_path) -> bool
    merge_static_mesh_actors(actors_to_merge, merge_options) -> StaticMeshActor or None
    load_level(asset_path) -> bool
    join_static_mesh_actors(actors_to_join, join_options) -> Actor
    get_selected_level_actors() -> Array(Actor)
    get_level_viewport_camera_info() -> (camera_location=Vector, camera_rotation=Rotator) or None
    get_game_world() -> World
    get_editor_world() -> World
    get_all_level_actors_components() -> Array(ActorComponent)
    get_all_level_actors() -> Array(Actor)
    get_actor_reference(path_to_actor) -> Actor
    eject_pilot_level_actor() -> None
    editor_set_game_view(game_view) -> None
    editor_play_simulate() -> None
    editor_invalidate_viewports() -> None
    destroy_actor(actor_to_destroy) -> bool
    create_proxy_mesh_actor(actors_to_merge, merge_options) -> StaticMeshActor or None
    convert_actors(actors, actor_class, static_mesh_package_path) -> Array(Actor)
    clear_actor_selection_set() -> None
"""

SequenceBindingLibrary = unreal.MovieSceneBindingExtensions
"""
    set_parent(binding, parent_binding) -> None
    remove_track(binding, track_to_remove) -> None
    remove(binding) -> None
    is_valid(binding) -> bool
    get_tracks(binding) -> Array(MovieSceneTrack)
    get_possessed_object_class(binding) -> type(Class)
    get_parent(binding) -> SequencerBindingProxy
    get_object_template(binding) -> Object
    get_name(binding) -> str
    get_id(binding) -> Guid
    get_display_name(binding) -> Text
    get_child_possessables(binding) -> Array(SequencerBindingProxy)
    find_tracks_by_type(binding, track_type) -> Array(MovieSceneTrack)
    find_tracks_by_exact_type(binding, track_type) -> Array(MovieSceneTrack)
    add_track(binding, track_type) -> MovieSceneTrack
"""

SequenceFolderLibrary = unreal.MovieSceneFolderExtensions
"""
    set_folder_name(folder, folder_name) -> bool
    set_folder_color(folder, folder_color) -> bool
    remove_child_object_binding(folder, object_binding) -> bool
    remove_child_master_track(folder, master_track) -> bool
    remove_child_folder(target_folder, folder_to_remove) -> bool
    get_folder_name(folder) -> Name
    get_folder_color(folder) -> Color
    get_child_object_bindings(folder) -> Array(SequencerBindingProxy)
    get_child_master_tracks(folder) -> Array(MovieSceneTrack)
    get_child_folders(folder) -> Array(MovieSceneFolder)
    add_child_object_binding(folder, object_binding) -> bool
    add_child_master_track(folder, master_track) -> bool
    add_child_folder(target_folder, folder_to_add) -> bool
"""

SequencePropertyLibrary = unreal.MovieScenePropertyTrackExtensions
"""
    X.set_property_name_and_path(track, property_name, property_path) -> None
    X.set_object_property_class(track, property_class) -> None
    X.get_unique_track_name(track) -> Name
    X.get_property_path(track) -> str
    X.get_property_name(track) -> Name
    X.get_object_property_class(track) -> type(Class)
"""

SequenceSectionLibrary = unreal.MovieSceneSectionExtensions
"""
    set_start_frame_seconds(section, start_time) -> None
    set_start_frame_bounded(section, is_bounded) -> None
    set_start_frame(section, start_frame) -> None
    set_range_seconds(section, start_time, end_time) -> None
    set_range(section, start_frame, end_frame) -> None
    set_end_frame_seconds(section, end_time) -> None
    set_end_frame_bounded(section, is_bounded) -> None
    set_end_frame(section, end_frame) -> None
    get_start_frame_seconds(section) -> float
    get_start_frame(section) -> int32
    get_parent_sequence_frame(section, frame, parent_sequence) -> int32
    get_end_frame_seconds(section) -> float
    get_end_frame(section) -> int32
    get_channels(section) -> Array(MovieSceneScriptingChannel)
    find_channels_by_type(section, channel_type) -> Array(MovieSceneScriptingChannel)
"""
SequenceLibrary = unreal.MovieSceneSectionExtensions
"""
    set_work_range_start(sequence, start_time_in_seconds) -> None
    set_work_range_end(sequence, end_time_in_seconds) -> None
    set_view_range_start(sequence, start_time_in_seconds) -> None
    set_view_range_end(sequence, end_time_in_seconds) -> None
    set_tick_resolution(sequence, tick_resolution) -> None
    set_read_only(sequence, read_only) -> None
    set_playback_start_seconds(sequence, start_time) -> None
    set_playback_start(sequence, start_frame) -> None
    set_playback_end_seconds(sequence, end_time) -> None
    set_playback_end(sequence, end_frame) -> None
    set_display_rate(sequence, display_rate) -> None
    make_range_seconds(sequence, start_time, duration) -> SequencerScriptingRange
    make_range(sequence, start_frame, duration) -> SequencerScriptingRange
    make_binding_id(master_sequence, binding, space=MovieSceneObjectBindingSpace.ROOT) -> MovieSceneObjectBindingID
    locate_bound_objects(sequence, binding, context) -> Array(Object)
    is_read_only(sequence) -> bool
    get_work_range_start(sequence) -> float
    get_work_range_end(sequence) -> float
    get_view_range_start(sequence) -> float
    get_view_range_end(sequence) -> float
    get_timecode_source(sequence) -> Timecode
    get_tick_resolution(sequence) -> FrameRate
    get_spawnables(sequence) -> Array(SequencerBindingProxy)
    get_root_folders_in_sequence(sequence) -> Array(MovieSceneFolder)
    get_possessables(sequence) -> Array(SequencerBindingProxy)
    get_playback_start_seconds(sequence) -> float
    get_playback_start(sequence) -> int32
    get_playback_range(sequence) -> SequencerScriptingRange
    get_playback_end_seconds(sequence) -> float
    get_playback_end(sequence) -> int32
    get_movie_scene(sequence) -> MovieScene
    get_master_tracks(sequence) -> Array(MovieSceneTrack)
    get_marked_frames(sequence) -> Array(MovieSceneMarkedFrame)
    get_display_rate(sequence) -> FrameRate
    get_bindings(sequence) -> Array(SequencerBindingProxy)
    find_next_marked_frame(sequence, frame_number, forward) -> int32
    find_master_tracks_by_type(sequence, track_type) -> Array(MovieSceneTrack)
    find_master_tracks_by_exact_type(sequence, track_type) -> Array(MovieSceneTrack)
    find_marked_frame_by_label(sequence, label) -> int32
    find_marked_frame_by_frame_number(sequence, frame_number) -> int32
    find_binding_by_name(sequence, name) -> SequencerBindingProxy
    delete_marked_frames(sequence) -> None
    delete_marked_frame(sequence, delete_index) -> None
    add_spawnable_from_instance(sequence, object_to_spawn) -> SequencerBindingProxy
    add_spawnable_from_class(sequence, class_to_spawn) -> SequencerBindingProxy
    add_root_folder_to_sequence(sequence, new_folder_name) -> MovieSceneFolder
    add_possessable(sequence, object_to_possess) -> SequencerBindingProxy
    add_master_track(sequence, track_type) -> MovieSceneTrack
    add_marked_frame(sequence, marked_frame) -> int32
"""

SequenceTrackLibrary = unreal.MovieSceneTrackExtensions
"""
    remove_section(track, section) -> None
    get_sections(track) -> Array(MovieSceneSection)
    get_display_name(track) -> Text
    add_section(track) -> MovieSceneSection
"""

SequenceTools = unreal.SequencerTools
"""
    render_movie(capture_settings, on_finished_callback) -> bool
    is_rendering_movie() -> bool
    import_fbx(world, sequence, bindings, import_fbx_settings, import_filename) -> bool
    get_object_bindings(world, sequence, object, range) -> Array(SequencerBoundObjects)
    get_bound_objects(world, sequence, bindings, range) -> Array(SequencerBoundObjects)
    export_fbx(world, sequence, bindings, override_options, fbx_file_name) -> bool
    export_anim_sequence(world, sequence, anim_sequence, binding) -> bool
    cancel_movie_render() -> None
"""

LevelSequenceLibrary = unreal.LevelSequenceEditorBlueprintLibrary
"""
    set_lock_level_sequence(lock) -> None
    set_current_time(new_frame) -> None
    play() -> None
    pause() -> None
    open_level_sequence(level_sequence) -> bool
    is_playing() -> bool
    is_level_sequence_locked() -> bool
    get_current_time() -> int32
    get_current_level_sequence() -> LevelSequence
    close_level_sequence() -> None
"""

PathLib = unreal.Paths
"""
    video_capture_dir() -> str
    validate_path(path) -> (did_succeed=bool, out_reason=Text)
    split(path) -> (path_part=str, filename_part=str, extension_part=str)
    source_config_dir() -> str
    should_save_to_user_dir() -> bool
    shader_working_dir() -> str
    set_project_file_path(new_game_project_file_path) -> None
    set_extension(path, new_extension) -> str
    screen_shot_dir() -> str
    sandboxes_dir() -> str
    root_dir() -> str
    remove_duplicate_slashes(path) -> str
    project_user_dir() -> str
    project_saved_dir() -> str
    project_plugins_dir() -> str
    project_persistent_download_dir() -> str
    project_mods_dir() -> str
    project_log_dir() -> str
    project_intermediate_dir() -> str
    project_dir() -> str
    project_content_dir() -> str
    project_config_dir() -> str
    profiling_dir() -> str
    normalize_filename(path) -> str
    normalize_directory_name(path) -> str
    make_valid_file_name(string, replacement_char="") -> str
    make_standard_filename(path) -> str
    make_platform_filename(path) -> str
    make_path_relative_to(path, relative_to) -> str or None
    launch_dir() -> str
    is_same_path(path_a, path_b) -> bool
    is_restricted_path(path) -> bool
    is_relative(path) -> bool
    is_project_file_path_set() -> bool
    is_drive(path) -> bool
    has_project_persistent_download_dir() -> bool
    get_tool_tip_localization_paths() -> Array(str)
    get_restricted_folder_names() -> Array(str)
    get_relative_path_to_root() -> str
    get_property_name_localization_paths() -> Array(str)
    get_project_file_path() -> str
    get_path(path) -> str
    get_invalid_file_system_chars() -> str
    get_game_localization_paths() -> Array(str)
    get_extension(path, include_dot=False) -> str
    get_engine_localization_paths() -> Array(str)
    get_editor_localization_paths() -> Array(str)
    get_clean_filename(path) -> str
    get_base_filename(path, remove_path=True) -> str
    generated_config_dir() -> str
    game_user_developer_dir() -> str
    game_source_dir() -> str
    game_developers_dir() -> str
    game_agnostic_saved_dir() -> str
    file_exists(path) -> bool
    feature_pack_dir() -> str
    enterprise_plugins_dir() -> str
    enterprise_feature_pack_dir() -> str
    enterprise_dir() -> str
    engine_version_agnostic_user_dir() -> str
    engine_user_dir() -> str
    engine_source_dir() -> str
    engine_saved_dir() -> str
    engine_plugins_dir() -> str
    engine_intermediate_dir() -> str
    engine_dir() -> str
    engine_content_dir() -> str
    engine_config_dir() -> str
    directory_exists(path) -> bool
    diff_dir() -> str
    create_temp_filename(path, prefix="", extension=".tmp") -> str
    convert_to_sandbox_path(path, sandbox_name) -> str
    convert_relative_path_to_full(path, base_path="") -> str
    convert_from_sandbox_path(path, sandbox_name) -> str
    combine(paths) -> str
    collapse_relative_directories(path) -> str or None
    cloud_dir() -> str
    change_extension(path, new_extension) -> str
    bug_it_dir() -> str
    automation_transient_dir() -> str
    automation_log_dir() -> str
    automation_dir() -> str
"""

