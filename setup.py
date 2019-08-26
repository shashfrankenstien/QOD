from setuptools import setup

setup(
	name='qod',
	version='1.0.1',
	author='Shashank Gopikrishna',
	author_email='shashank.gopikrishna@gmail.com',
	packages=['qod'],
	install_requires=['requests'],
	entry_points = {
		'console_scripts': ['qod=qod.quotes:_cli'],
	},
	description='Quotes from www.quotery.com (with CLI)',
)