from unreal_global import *
import unreal_utils
import unreal


@unreal.uclass()
class SampleActorAction(unreal.ActorActionUtility):
    # @unreal.ufunction(override=True)
    # def get_supported_class(self):
    #     return unreal.Actor

    @unreal.ufunction(
        static=True,
        meta=dict(CallInEditor=True, Category="Sample Actor Action Library"),
    )
    def python_test_actor_action():
        unreal.log("Execute Sample Actor Action")

    @unreal.ufunction(
        params=[str],
        static=True,
        meta=dict(CallInEditor=True, Category="Sample Actor Action Library"),
    )
    def python_test_actor_action_with_parameters(input_string):
        unreal.log("Execute Sample Actor Action with {}".format(input_string))


# Unreal need a actual blueprint asset to be created and inherit from the new class for it to work
# unreal_utils.register_editor_utility_blueprint("SampleActorUtility", SampleActorAction)
