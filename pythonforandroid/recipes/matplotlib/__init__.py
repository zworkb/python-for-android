
from pythonforandroid.toolchain import CompiledComponentsPythonRecipe, warning, Recipe

from os.path import join

class MatplotlibRecipe(CompiledComponentsPythonRecipe):
    
    version = '1.5.0'
    url = 'https://github.com/matplotlib/matplotlib/archive/v{version}.zip'

    depends = ['python2', 'numpy', 'freetype_ndk', 'png', 'setuptools']

    patches = ['prevent_setuptools_download.patch',
               'disable_extensions.patch',
               'find_dependencies.patch',
               'show_install_requires.patch']

    call_hostpython_via_targetpython = False

    def get_recipe_env(self, arch):
        env = super(MatplotlibRecipe, self).get_recipe_env(arch)

        numpy_recipe = Recipe.get_recipe('numpy', self.ctx)
        
        env['NUMPY_INCLUDE_DIR'] = join(
            numpy_recipe.get_build_container_dir(arch.arch),
            'numpy', 'core', 'include')

        env['CFLAGS'] = env['CFLAGS'] + ' -I{jni_path}/png -I{jni_path}/freetype/include'.format(
            jni_path=join(self.ctx.bootstrap.build_dir, 'jni'))

        return env


recipe = MatplotlibRecipe()
