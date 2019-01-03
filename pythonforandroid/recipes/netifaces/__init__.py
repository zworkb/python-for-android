import os
from pythonforandroid.recipe import CompiledComponentsPythonRecipe

class NetifacesRecipe(CompiledComponentsPythonRecipe):

    version = '0.10.4'

    url = 'https://pypi.python.org/packages/18/fa/dd13d4910aea339c0bb87d2b3838d8fd923c11869b1f6e741dbd0ff3bc00/netifaces-{version}.tar.gz'

    depends = [('python2', 'python3crystax'), 'setuptools']

    site_packages_name = 'netifaces'

    call_hostpython_via_targetpython = False

    def get_recipe_env(self, arch):
        env = super(NetifacesRecipe, self).get_recipe_env(arch)
        env['PYTHON_ROOT'] = self.ctx.get_python_install_dir()
        env['CFLAGS'] += ' -I{}'.format(self.ctx.python_recipe.include_root(arch.arch))
        env['LDSHARED'] = env['CC'] + ' -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions'

        # required for libc and libdl
        ndk_dir = self.ctx.ndk_platform
        ndk_lib_dir = os.path.join(ndk_dir, 'usr', 'lib')
        env['LDFLAGS'] += ' -L{}'.format(ndk_lib_dir)
        env['LDFLAGS'] += ' -L{}'.format(self.ctx.python_recipe.link_root(arch.arch))
        env['LDFLAGS'] += ' -lpython{}'.format(self.ctx.python_recipe.major_minor_version_string)
        if 'python3' in self.ctx.python_recipe.name:
            env['LDFLAGS'] += 'm'
        # XX very very bad, but in their setup, conftest doesn't use LDFLAGS?
        env['CC'] += env['LDFLAGS']
        return env


recipe = NetifacesRecipe()
