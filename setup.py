try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'author'            : 'Jonah Glover',
#	'url'               : 'github.com/jonahglover/lol.git',
#	'download_url'      : 'github.com/jonahglover/lold.git',
	'author_email'      : 'me@jonah.wtf',
	'version'           : '0.1',
	'install_requires'  : ['nose'],
	'packages'          : ['baffin'],
	'scripts'           : [],
	'name'              : 'baffin'
}

setup(**config)
