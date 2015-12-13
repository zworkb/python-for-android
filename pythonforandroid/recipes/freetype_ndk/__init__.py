

from pythonforandroid.toolchain import NDKRecipe


class Freetype(NDKRecipe):
    version = 'master'
    url = 'https://github.com/inclement/p4a-freetype_ndk/archive/{version}.zip'
    dir_name = 'freetype'

    patches = []

    call_ndk_build = True


recipe = Freetype()
