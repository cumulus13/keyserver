#!/usr/bin/env python

""" keyserver installation script """

VERSION = '1.0'

try:
	from distutils.core import setup
except:
	from setuptools import setup

setup(
		name			= 'keyserver',
		version			= '{0}'.format(VERSION),
		description 	= 'Command line Pub key generator from keyserver.ubuntu.com',
		License 		= 'MIT',
		author			= 'Laode Hadi Cahyadi',
		author_email	= 'licface@yahoo.com',
		url				= 'https://codecumulus13.wordpress.com',
		download_url    = 'https://github.com/cumulus13/keyserver/archive/{0}.tar.gz'.format(VERSION),
		keywords 		= ['keyserver', 'cli', 'command line'],
		packages		= ['keyserver'],
		scripts			= ['keyserver.py'],
		classifiers 	= [
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Debian Community',
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Linux :: Debian',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Software',
          'Topic :: Utilities',
          'Operating System :: OS Independent',
      ]
)


