from distutils.core import setup

setup(
    name='PyPing',
    version='0.1.0',
    packages=['argparse', 'os', 'select', 'signal', 'socket', 'struct', 'sys', 'time'],
    url='https://github.com/joedborg/PyPing',
    license='GPLv2',
    author='Joe Borg',
    author_email='mail@jdborg.com',
    description='A Cisco style ping tool'
)
