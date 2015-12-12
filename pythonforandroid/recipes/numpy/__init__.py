
from pythonforandroid.toolchain import CompiledComponentsPythonRecipe, warning
from pythonforandroid.patching import is_arch


class NumpyRecipe(CompiledComponentsPythonRecipe):
    
    version = '1.9.2'
    url = 'http://pypi.python.org/packages/source/n/numpy/numpy-{version}.tar.gz'
    site_packages_name= 'numpy'

    depends = ['python2']

    patches = ['patches/fix-numpy.patch',
               'patches/prevent_libs_check.patch',
               'patches/ar.patch',
               'patches/lib.patch']

    def prebuild_arch(self, arch):
        super(NumpyRecipe, self).prebuild_arch(arch)

        # AND: Fix this warning!
        warning('Numpy is built assuming the archiver name is '
                'arm-linux-androideabi-ar, which may not always be true!')
        if arch.arch[:3] != 'arm':
            error('Trying to build with unsupported arch - the numpy patches need '
                  'to be fixed to use the right archiver.')
            exit(1)



recipe = NumpyRecipe()
