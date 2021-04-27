# Nguyen Phi Hung @ 2020
# hung.nguyen@onikuma.games

from unreal_global import *
import hashlib
import unreal


class AssetRegistryPostLoad:
    _callbacks = {}

    @classmethod
    def register_callback(cls, func, *args, **kws):
        cls._callbacks[hashlib.md5(str((func, args, kws)).encode()).hexdigest()] = (
            func,
            args,
            kws,
        )

    @classmethod
    def unregister_callback(cls, func, *args, **kws):
        try:
            del cls._callbacks[hashlib.md5(str((func, args, kws)).encode()).hexdigest()]
        except KeyError:
            unreal.log_error(
                "No callback name {} with arguments: {} and keywords {} to unregister".format(
                    func.__name__, args, kws
                )
            )

    @classmethod
    def run_callbacks(cls):
        for func_name, func_param in cls._callbacks.items():
            func, args, kws = func_param
            unreal.log_warning(
                "execute {} with param {} keywords: {}".format(func.__name__, args, kws)
            )
            try:
                func(*args, **kws)
            except Exception as why:
                unreal.log_error("failed to run with error:\n{}".format(why))

def get_outer_package():
    return unreal.find_object(None, "/Engine/Transient")

def create_unreal_asset(
    asset_name, package_path, factory, asset_class, force=False, save=True
):
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
        if force:
            unreal.log_warning("{} exists. Skip creating".format(asset_name))
            return
        else:
            unreal.log_warning("{} exists. Remove existing asset.".format(asset_name))
            AssetLibrary.delete_asset(asset_path)

    factory.set_editor_property("ParentClass", asset_class)

    new_asset = AssetTools.create_asset(asset_name, package_path, None, factory)

    if save:
        AssetLibrary.save_loaded_asset(new_asset)

    return new_asset


def create_levelsequence_asset(asset_name, package_path, force=False, save=True):
    create_unreal_asset(
        asset_name,
        package_path,
        unreal.LevelSequenceFactoryNew(),
        unreal.LevelSequence,
        force,
        save,
    )


def create_blueprint_asset(
    asset_name, package_path, asset_parent_class, force=False, save=True
):
    create_unreal_asset(
        asset_name,
        package_path,
        unreal.BlueprintFactory(),
        asset_parent_class,
        force,
        save,
    )


def create_editor_utility_blueprint(
    asset_name, asset_parent_class, force=False, save=False
):
    create_unreal_asset(
        f"{asset_name}",
        "/Engine/",
        unreal.EditorUtilityBlueprintFactory(),
        asset_parent_class,
        force,
        save,
    )


def register_editor_utility_blueprint(asset_name, asset_parent_class):
    AssetRegistryPostLoad.register_callback(
        create_editor_utility_blueprint, asset_name, asset_parent_class
    )


# def new_object(object_class):
#     unreal.load_object(unreal.new_object(object_class))
# def register_editor_utility_blueprint(asset_name, asset_parent_class):
#     AssetRegistryPostLoad.register_callback(new_object, asset_parent_class)
