# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='gitsuper',
    long_description='Git scripts for managing submodule trees',
    version='0.1.0',
    packages=['gitsuper'],
    license='MIT',
    scripts=[
    	'bin/git-super-root',
    	'bin/git-super-foreach',
        'bin/git-super-sync',
        'bin/git-super-branch',
        'bin/git-super-merge',
    ])
)
