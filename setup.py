from distutils.core import setup
import sys

if not sys.version_info[0] == 3:
    sys.exit("Sorry, Python 2 is not supported (yet)")

setup(
    name='easywiki',
    version='1.0.0dev',
    packages=['easywiki'],
    #entry_points = {"console_scripts": ['easywiki = easywiki.__main__:main']},
    #install_requires=['bs4',],
    requires=['bs4',],
    url='https://github.com/sherinann/easywiki',
    license='GPL 3',
    author='Sherin Ann Thomas',
    author_email='sherinannthomas1@gmail.com',
    description='A simple CLI for using wikipedia from terminal',
    download_url = 'https://github.com/sherinann/easywiki/archive/0.1.tar.gz'

)
