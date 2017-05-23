reconnectTextures
=================

A blender script / addon to help reconnect textures for many materials on many objects quickly. NOTE: this script is basically made redundant by the built in functionality below:

![Builtin method](/builtin_method.png)


Usage
=================

At the moment this works as a script, not an addon. To use it,  open up the blender text editor window and open the "reconnectTextures.py" script. Under the main function you should see the the variable "directory", change that string (text in the quotes) to the path to the directory you want to recheck all textures for.

Note currently it is a hard set, so even if a texture is not found in new location, the data path will still be set to point there. Just be aware.
