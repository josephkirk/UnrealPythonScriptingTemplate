from unreal_global import *
import unreal_utils

@unreal.uclass()
class SampleActorAction(unreal.ActorActionUtility):
    @unreal.ufunction(override=True)
    def get_supported_class(self):
        return unreal.Actor

    @unreal.ufunction(static=True, meta=dict(CallInEditor=True, Category="Sample Actor Action Library"))
    def test_actor_action():
        unreal.log("Execute Sample Actor Action")

    # any parameters declare will generated a UI show those input when the function is activated
    @unreal.ufunction(params=[str], static=True, meta=dict(CallInEditor=True, Category="Sample Actor Action Library"))
    def test_actor_action(input_string):
        unreal.log("Execute Sample Actor Action with {}".format(input_string))

# Unreal require actual Editor Utility Blueprint asset to be created and inherit from the new class for it to work.
unreal_utils.create_editor_utility_blueprint("SampleActorUtility", SampleActorAction)