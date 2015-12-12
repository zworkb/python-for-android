
from pythonforandroid.toolchain import CompiledComponentsPythonRecipe, warning


class MatplotlibRecipe(CompiledComponentsPythonRecipe):
    
    version = '1.5.0'
    url = 'https://github.com/matplotlib/matplotlib/archive/v{version}.zip'

    depends = ['python2', 'numpy', 'freetype_ndk', 'png']

    patches = []



recipe = MatplotlibRecipe()
