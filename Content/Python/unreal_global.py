import unreal

AssetRegistry = unreal.AssetRegistryHelpers.get_asset_registry()

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

AutomationScheduler = unreal.AutomationScheduler

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

SystemLib = unreal.SystemLibrary
"""
    unregister_for_remote_notifications() -> None
    unload_primary_asset_list(primary_asset_id_list) -> None
    unload_primary_asset(primary_asset_id) -> None
    transact_object(object) -> None
    sphere_trace_single_for_objects(world_context_object, start, end, radius, object_types, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> HitResult or None
    sphere_trace_single_by_profile(world_context_object, start, end, radius, profile_name, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> HitResult or None
    sphere_trace_single(world_context_object, start, end, radius, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> HitResult or None
    sphere_trace_multi_for_objects(world_context_object, start, end, radius, object_types, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> Array(HitResult) or None
    sphere_trace_multi_by_profile(world_context_object, start, end, radius, profile_name, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> Array(HitResult) or None
    sphere_trace_multi(world_context_object, start, end, radius, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> Array(HitResult) or None
    sphere_overlap_components(world_context_object, sphere_pos, sphere_radius, object_types, component_class_filter, actors_to_ignore) -> Array(PrimitiveComponent) or None
    sphere_overlap_actors(world_context_object, sphere_pos, sphere_radius, object_types, actor_class_filter, actors_to_ignore) -> Array(Actor) or None
    snapshot_object(object) -> None
    show_platform_specific_leaderboard_screen(category_name) -> None
    show_platform_specific_achievements_screen(specific_player) -> None
    show_interstitial_ad() -> None
    show_ad_banner(ad_id_index, show_on_bottom_of_screen) -> None
    set_window_title(title) -> None
    set_volume_buttons_handled_by_system(enabled) -> None
    set_user_activity(user_activity) -> None
    set_suppress_viewport_transition_message(world_context_object, state) -> None
    set_gamepads_block_device_feedback(block) -> None
    retriggerable_delay(world_context_object, duration, latent_info) -> None
    reset_gamepad_assignment_to_controller(controller_id) -> None
    reset_gamepad_assignments() -> None
    register_for_remote_notifications() -> None
    quit_game(world_context_object, specific_player, quit_preference, ignore_platform_restrictions) -> None
    quit_editor() -> None
    print_text(world_context_object, text="Hello", print_to_screen=True, print_to_log=True, text_color=[0.000000, 0.000000, 0.000000, 0.000000], duration=2.000000) -> None
    print_string(world_context_object, string="Hello", print_to_screen=True, print_to_log=True, text_color=[0.000000, 0.000000, 0.000000, 0.000000], duration=2.000000) -> None
    not_equal_soft_object_reference(a, b) -> bool
    not_equal_soft_class_reference(a, b) -> bool
    not_equal_primary_asset_type(a, b) -> bool
    not_equal_primary_asset_id(a, b) -> bool
    normalize_filename(filename) -> str
    move_component_to(component, target_relative_location, target_relative_rotation, ease_out, ease_in, over_time, force_shortest_rotation_path, move_action, latent_info) -> None
    make_literal_text(value) -> Text
    make_literal_string(value) -> str
    make_literal_name(value) -> Name
    make_literal_int(value) -> int32
    make_literal_float(value) -> float
    make_literal_byte(value) -> uint8
    make_literal_bool(value) -> bool
    load_interstitial_ad(ad_id_index) -> None
    load_class_asset_blocking(asset_class) -> type(Class)
    load_asset_blocking(asset) -> Object
    line_trace_single_for_objects(world_context_object, start, end, object_types, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> HitResult or None
    line_trace_single_by_profile(world_context_object, start, end, profile_name, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> HitResult or None
    line_trace_single(world_context_object, start, end, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> HitResult or None
    line_trace_multi_for_objects(world_context_object, start, end, object_types, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> Array(HitResult) or None
    line_trace_multi_by_profile(world_context_object, start, end, profile_name, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> Array(HitResult) or None
    line_trace_multi(world_context_object, start, end, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> Array(HitResult) or None
    launch_url(url) -> None
    un_pause_timer_handle(world_context_object, handle) -> None
    un_pause_timer_delegate(delegate) -> None
    un_pause_timer(object, function_name) -> None
    timer_exists_handle(world_context_object, handle) -> bool
    timer_exists_delegate(delegate) -> bool
    timer_exists(object, function_name) -> bool
    set_timer_delegate(delegate, time, looping, initial_start_delay=0.000000, initial_start_delay_variance=0.000000) -> TimerHandle
    set_timer(object, function_name, time, looping, initial_start_delay=0.000000, initial_start_delay_variance=0.000000) -> TimerHandle
    pause_timer_handle(world_context_object, handle) -> None
    pause_timer_delegate(delegate) -> None
    pause_timer(object, function_name) -> None
    is_valid_timer_handle(handle) -> bool
    is_timer_paused_handle(world_context_object, handle) -> bool
    is_timer_paused_delegate(delegate) -> bool
    is_timer_paused(object, function_name) -> bool
    is_timer_active_handle(world_context_object, handle) -> bool
    is_timer_active_delegate(delegate) -> bool
    is_timer_active(object, function_name) -> bool
    invalidate_timer_handle(handle) -> (TimerHandle, handle=TimerHandle)
    get_timer_remaining_time_handle(world_context_object, handle) -> float
    get_timer_remaining_time_delegate(delegate) -> float
    get_timer_remaining_time(object, function_name) -> float
    get_timer_elapsed_time_handle(world_context_object, handle) -> float
    get_timer_elapsed_time_delegate(delegate) -> float
    get_timer_elapsed_time(object, function_name) -> float
    clear_timer_handle(world_context_object, handle) -> None
    clear_timer_delegate(delegate) -> None
    clear_timer(object, function_name) -> None
    clear_and_invalidate_timer_handle(world_context_object, handle) -> TimerHandle
    is_valid_soft_object_reference(soft_object_reference) -> bool
    is_valid_soft_class_reference(soft_class_reference) -> bool
    is_valid_primary_asset_type(primary_asset_type) -> bool
    is_valid_primary_asset_id(primary_asset_id) -> bool
    is_valid_class(class_) -> bool
    is_valid(object) -> bool
    is_unattended() -> bool
    is_standalone(world_context_object) -> bool
    is_split_screen(world_context_object) -> bool
    is_server(world_context_object) -> bool
    is_screensaver_enabled() -> bool
    is_packaged_for_distribution() -> bool
    is_logged_in(specific_player) -> bool
    is_interstitial_ad_requested() -> bool
    is_interstitial_ad_available() -> bool
    is_dedicated_server(world_context_object) -> bool
    is_controller_assigned_to_gamepad(controller_id) -> bool
    hide_ad_banner() -> None
    get_volume_buttons_handled_by_system() -> bool
    get_unique_device_id() -> str
    get_supported_fullscreen_resolutions() -> Array(IntPoint) or None
    get_soft_object_reference_from_primary_asset_id(primary_asset_id) -> Object
    get_soft_class_reference_from_primary_asset_id(primary_asset_id) -> Class
    get_rendering_material_quality_level() -> int32
    get_rendering_detail_mode() -> int32
    get_project_saved_directory() -> str
    get_project_directory() -> str
    get_project_content_directory() -> str
    get_primary_assets_with_bundle_state(required_bundles, excluded_bundles, valid_types, force_current_state) -> Array(PrimaryAssetId)
    get_primary_asset_id_list(primary_asset_type) -> Array(PrimaryAssetId)
    get_primary_asset_id_from_soft_object_reference(soft_object_reference) -> PrimaryAssetId
    get_primary_asset_id_from_soft_class_reference(soft_class_reference) -> PrimaryAssetId
    get_primary_asset_id_from_object(object) -> PrimaryAssetId
    get_primary_asset_id_from_class(class_) -> PrimaryAssetId
    get_preferred_languages() -> Array(str)
    get_platform_user_name() -> str
    get_platform_user_dir() -> str
    get_path_name(object) -> str
    get_outer_object(object) -> Object
    get_object_name(object) -> str
    get_object_from_primary_asset_id(primary_asset_id) -> Object
    get_min_y_resolution_for_ui() -> int32
    get_min_y_resolution_for3d_view() -> int32
    get_local_currency_symbol() -> str
    get_local_currency_code() -> str
    get_game_time_in_seconds(world_context_object) -> float
    get_gamepad_controller_name(controller_id) -> str
    get_game_name() -> str
    get_game_bundle_id() -> str
    get_frame_count() -> int64
    get_engine_version() -> str
    get_display_name(object) -> str
    get_device_id() -> str
    get_default_locale() -> str
    get_default_language() -> str
    get_current_bundle_state(primary_asset_id, force_current_state) -> Array(Name) or None
    get_convenient_windowed_resolutions() -> Array(IntPoint) or None
    get_console_variable_int_value(variable_name) -> int32
    get_console_variable_float_value(variable_name) -> float
    get_console_variable_bool_value(variable_name) -> bool
    get_component_bounds(component) -> (origin=Vector, box_extent=Vector, sphere_radius=float)
    get_command_line() -> str
    get_class_from_primary_asset_id(primary_asset_id) -> type(Class)
    get_class_display_name(class_) -> str
    get_ad_id_count() -> int32
    get_actor_list_from_component_list(component_list, actor_class_filter) -> Array(Actor)
    get_actor_bounds(actor) -> (origin=Vector, box_extent=Vector)
    force_close_ad_banner() -> None
    flush_persistent_debug_lines(world_context_object) -> None
    flush_debug_strings(world_context_object) -> None
    execute_console_command(world_context_object, command, specific_player=None) -> None
    equal_equal_soft_object_reference(a, b) -> bool
    equal_equal_soft_class_reference(a, b) -> bool
    equal_equal_primary_asset_type(a, b) -> bool
    equal_equal_primary_asset_id(a, b) -> bool
    end_transaction() -> int32
    draw_debug_string(world_context_object, text_location, text, test_base_actor=None, text_color=[0.000000, 0.000000, 0.000000, 0.000000], duration=0.000000) -> None
    draw_debug_sphere(world_context_object, center, radius=100.000000, segments=12, line_color=[0.000000, 0.000000, 0.000000, 0.000000], duration=0.000000, thickness=0.000000) -> None
    draw_debug_point(world_context_object, position, size, point_color, duration=0.000000) -> None
    draw_debug_plane(world_context_object, plane_coordinates, location, size, plane_color=[0.000000, 0.000000, 0.000000, 0.000000], duration=0.000000) -> None
    draw_debug_line(world_context_object, line_start, line_end, line_color, duration=0.000000, thickness=0.000000) -> None
    draw_debug_frustum(world_context_object, frustum_transform, frustum_color=[0.000000, 0.000000, 0.000000, 0.000000], duration=0.000000, thickness=0.000000) -> None
    draw_debug_float_history_transform(world_context_object, float_history, draw_transform, draw_size, draw_color=[0.000000, 0.000000, 0.000000, 0.000000], duration=0.000000) -> None
    draw_debug_float_history_location(world_context_object, float_history, draw_location, draw_size, draw_color=[0.000000, 0.000000, 0.000000, 0.000000], duration=0.000000) -> None
    draw_debug_cylinder(world_context_object, start, end, radius=100.000000, segments=12, line_color=[0.000000, 0.000000, 0.000000, 0.000000], duration=0.000000, thickness=0.000000) -> None
    draw_debug_coordinate_system(world_context_object, axis_loc, axis_rot, scale=1.000000, duration=0.000000, thickness=0.000000) -> None
    draw_debug_cone_in_degrees(world_context_object, origin, direction, length=100.000000, angle_width=45.000000, angle_height=45.000000, num_sides=12, line_color=[0.000000, 0.000000, 0.000000, 0.000000], duration=0.000000, thickness=0.000000) -> None
    draw_debug_cone(world_context_object, origin, direction, length, angle_width, angle_height, num_sides, line_color, duration=0.000000, thickness=0.000000) -> None
    draw_debug_circle(world_context_object, center, radius, num_segments=12, line_color=[0.000000, 0.000000, 0.000000, 0.000000], duration=0.000000, thickness=0.000000, y_axis=[0.000000, 1.000000, 0.000000], z_axis=[0.000000, 0.000000, 1.000000], draw_axis=False) -> None
    draw_debug_capsule(world_context_object, center, half_height, radius, rotation, line_color=[0.000000, 0.000000, 0.000000, 0.000000], duration=0.000000, thickness=0.000000) -> None
    draw_debug_camera(camera_actor, camera_color=[0.000000, 0.000000, 0.000000, 0.000000], duration=0.000000) -> None
    draw_debug_box(world_context_object, center, extent, line_color, rotation=[0.000000, 0.000000, 0.000000], duration=0.000000, thickness=0.000000) -> None
    draw_debug_arrow(world_context_object, line_start, line_end, arrow_size, line_color, duration=0.000000, thickness=0.000000) -> None
    does_implement_interface(test_object, interface) -> bool
    delay(world_context_object, duration, latent_info) -> None
    create_copy_for_undo_buffer(object_to_modify) -> None
    convert_to_relative_path(filename) -> str
    convert_to_absolute_path(filename) -> str
    conv_soft_obj_path_to_soft_obj_ref(soft_object_path) -> Object
    conv_soft_object_reference_to_string(soft_object_reference) -> str
    conv_soft_class_reference_to_string(soft_class_reference) -> str
    conv_soft_class_path_to_soft_class_ref(soft_class_path) -> Class
    conv_primary_asset_type_to_string(primary_asset_type) -> str
    conv_primary_asset_id_to_string(primary_asset_id) -> str
    conv_interface_to_object(interface) -> Object
    control_screensaver(allow_screen_saver) -> None
    component_overlap_components(component, component_transform, object_types, component_class_filter, actors_to_ignore) -> Array(PrimitiveComponent) or None
    component_overlap_actors(component, component_transform, object_types, actor_class_filter, actors_to_ignore) -> Array(Actor) or None
    collect_garbage() -> None
    capsule_trace_single_for_objects(world_context_object, start, end, radius, half_height, object_types, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> HitResult or None
    capsule_trace_single_by_profile(world_context_object, start, end, radius, half_height, profile_name, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> HitResult or None
    capsule_trace_single(world_context_object, start, end, radius, half_height, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> HitResult or None
    capsule_trace_multi_for_objects(world_context_object, start, end, radius, half_height, object_types, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> Array(HitResult) or None
    capsule_trace_multi_by_profile(world_context_object, start, end, radius, half_height, profile_name, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> Array(HitResult) or None
    capsule_trace_multi(world_context_object, start, end, radius, half_height, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> Array(HitResult) or None
    capsule_overlap_components(world_context_object, capsule_pos, radius, half_height, object_types, component_class_filter, actors_to_ignore) -> Array(PrimitiveComponent) or None
    capsule_overlap_actors(world_context_object, capsule_pos, radius, half_height, object_types, actor_class_filter, actors_to_ignore) -> Array(Actor) or None
    can_launch_url(url) -> bool
    cancel_transaction(index) -> None
    box_trace_single_for_objects(world_context_object, start, end, half_size, orientation, object_types, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> HitResult or None
    box_trace_single_by_profile(world_context_object, start, end, half_size, orientation, profile_name, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> HitResult or None
    box_trace_single(world_context_object, start, end, half_size, orientation, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> HitResult or None
    box_trace_multi_for_objects(world_context_object, start, end, half_size, orientation, object_types, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> Array(HitResult) or None
    box_trace_multi_by_profile(world_context_object, start, end, half_size, orientation, profile_name, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> Array(HitResult) or None
    box_trace_multi(world_context_object, start, end, half_size, orientation, trace_channel, trace_complex, actors_to_ignore, draw_debug_type, ignore_self, trace_color=[0.000000, 0.000000, 0.000000, 0.000000], trace_hit_color=[0.000000, 0.000000, 0.000000, 0.000000], draw_time=5.000000) -> Array(HitResult) or None
    box_overlap_components(world_context_object, box_pos, extent, object_types, component_class_filter, actors_to_ignore) -> Array(PrimitiveComponent) or None
    box_overlap_actors(world_context_object, box_pos, box_extent, object_types, actor_class_filter, actors_to_ignore) -> Array(Actor) or None
    begin_transaction(context, description, primary_object) -> int32
    add_float_history_sample(value, float_history) -> DebugFloatHistory
"""
