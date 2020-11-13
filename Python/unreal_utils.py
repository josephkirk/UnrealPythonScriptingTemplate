# Nguyen Phi Hung @ 2020
# hung.nguyen@onikuma.games

from unreal_global import *
import hashlib
import unreal

class AssetRegistryPostLoad:
    _callbacks={}
    @classmethod
    def register_callback(cls, func, *args, **kws):
        cls._callbacks[hashlib.md5(str((func, args, kws)).encode()).hexdigest()] = (func, args, kws)

    @classmethod
    def unregister_callback(cls, func, *args, **kws):
        try:
            del cls._callbacks[hashlib.md5(str((func, args, kws)).encode()).hexdigest()]
        except KeyError:
            unreal.log_error("No callback name {} with arguments: {} and keywords {} to unregister".format(func.__name__ , args, kws))

    @classmethod
    def run_callbacks(cls):
        for func_name, func_param in cls._callbacks.items():
            func, args, kws = func_param
            unreal.log_warning("execute {} with param {} keywords: {}".format(func.__name__, args, kws))
            try:
                func(*args, **kws)
            except Exception as why:
                unreal.log_error("failed to run with error:\n{}".format(why))

def create_unreal_asset(asset_name, package_path, factory, asset_class, force=False, save=True, is_blueprint=False, parent_class_is_python=False):
    """

    INPUT:
        asset_name: str
            Exp: "MyAwesomeBPActorClass"
        package_path: str
            Exp: "/Game/MyContentFolder"
        package_path: unreal.Factory:
            Exp: unreal.BlueprintFactory()
        asset_class: unreal.Object
            Exp: unreal.Actor
        force: bool
            Force remove old and create new one
        save: bool
            Save asset after creation

    OUPUT:
        unreal.Object

    """

    asset_path = "{}/{}".format(package_path, asset_name)
    if AssetLibrary.does_asset_exist(asset_path):
        if not force:
            unreal.log_warning("{} exists. Skip creating".format(asset_name))
            return
        else:
            unreal.log_warning("{} exists. Remove existing asset.".format(asset_name))
            AssetLibrary.delete_asset(asset_path)
 
    factory.set_editor_property("parent_class", asset_class)
    factory.set_editor_property("create_new", not is_python_generated)
    # if AssetRegistry.is_loading_assets():
    #     return
    new_asset = AssetTools.create_asset(asset_name, package_path, None, factory)


    # if is_python_generated:
    #     generated_class = new_asset.get_class()
    #     unreal.log_warning(generated_class)
    #     AssetLibrary.delete_asset(new_asset.get_path_name())
    #     factory.set_editor_property("ParentClass", generated_class)
    #     new_asset = AssetTools.create_asset(asset_name, package_path, None, factory)
    if new_asset:
        if is_blueprint:
            unreal.EditorAssetLibrary.load_blueprint_class(new_asset.get_path_name())

        if save:
            AssetLibrary.save_loaded_asset(new_asset)
        
        return new_asset

def create_levelsequence_asset(asset_name, package_path, force=False, save=True):
    create_unreal_asset(asset_name, package_path, unreal.LevelSequenceFactoryNew(), unreal.LevelSequence, force, save)

def create_blueprint_asset(asset_name, package_path, asset_parent_class, force=True, save=False):
    create_unreal_asset(asset_name, package_path, unreal.BlueprintFactory(), asset_parent_class, force, save, True)

def create_editor_utility_blueprint(asset_name, asset_parent_class, force=True, save=False):
    create_unreal_asset(asset_name, "/Engine/Transient", unreal.EditorUtilityBlueprintFactory(), asset_parent_class, force, save, True, True)

def register_editor_utility_blueprint(asset_name, asset_parent_class):
    AssetRegistryPostLoad.register_callback(create_editor_utility_blueprint, asset_name, asset_parent_class)
