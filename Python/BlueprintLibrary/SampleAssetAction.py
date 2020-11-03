from unreal_global import *
import unreal_utils
@unreal.uclass()
class SampleAssetAction(unreal.AssetActionUtility):
    @unreal.ufunction(override=True)
    def get_supported_class(self):
        return unreal.StaticMesh

    @unreal.ufunction(static=True, meta=dict(CallInEditor=True, Category="Sample Asset Action Library"))
    def test_asset_action():
        unreal.log("Execute Sample Asset Action")


    @unreal.ufunction(params=[int], static=True, meta=dict(CallInEditor=True, Category="Sample Asset Action Library"))
    def test_asset_action(input_num):
        unreal.log("Execute Sample Asset Action with {}".format(input_num))

unreal_utils.create_editor_utility_blueprint("SampleAssetUtility", SampleAssetAction)