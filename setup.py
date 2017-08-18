try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My project',
	'author': 'Aditi',
	'url': 'github.com/aditib13',
	'download_url': 'Where to download it.',
	'author_email': 'aditibhandari24@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)