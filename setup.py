from distutils.core import setup

setup(
    name='theaV2',
    version='0.1dev',
    packages=['thea', 'thea.lib', 'thea.lib.views', 'thea.lib.config', 'thea.lib.models', 'thea.lib.helpers',
              'thea.lib.services', 'thea.lib.controllers', 'thea.test', 'thea.test.services', 'thea.test.controllers',
              'thea.test.integration', 'thea.resources'],
    url='',
    license='',
    author='mike',
    author_email='',
    description='',
    requires=['PySide', 'iris', 'mockito']
)
