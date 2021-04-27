from unreal_global import *
import unreal_utils
import unreal


@unreal.uclass()
class SamplePythonAssetAction(unreal.AssetActionUtility):
    # @unreal.ufunction(override=True)
    # def get_supported_class(self):
    #     return unreal.StaticMesh

    @unreal.ufunction(
        static=True,
        meta=dict(CallInEditor=True, Category="Sample Asset Action Library"),
    )
    def python_dump_asset_info():
        selected_assets = UtilLibrary.get_selected_assets()
        for asset in selected_assets:
            unreal.log(
                "{} {} {}".format(
                    asset.get_name(), asset.get_outermost(), asset.get_path_name()
                )
            )

    # @unreal.ufunction(params=[int], static=True, meta=dict(CallInEditor=True, Category="Sample Asset Action Library"))
    # def test_asset_action(input_num):
    #     unreal.log("Execute Sample Asset Action with {}".format(input_num))


# Unreal need a actual blueprint asset to be created and inherit from the new class for it to work
# unreal_utils.register_editor_utility_blueprint(
#     "SampleAssetUtility", SamplePythonAssetAction
# )
