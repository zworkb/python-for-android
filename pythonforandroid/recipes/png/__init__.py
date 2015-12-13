
from pythonforandroid.toolchain import NDKRecipe


class Libpng(NDKRecipe):
    version = 'master'
    url = 'https://github.com/inclement/p4a-libpng/archive/{version}.zip'
    dir_name = 'png'

    patches = []

    call_ndk_build = True


recipe = Libpng()
