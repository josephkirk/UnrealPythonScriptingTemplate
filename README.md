# Template for extend unreal editor with python

## USAGE
Clone this project to your Unreal Project Root

Edit **UserEngine.ini** in **Config** and adjust the path to **Python** folder.
#TODO find out a way to make this relative

Otherwise copy **Python** folder to your project **Content** folder

In **BlueprintLibrary** Module duplicate relevant blueprint action utility sample and extend functionality, any module will be auto generated with blueprint asset when unreal load.

See **unreal_startup.py** for how to add menu hookup.