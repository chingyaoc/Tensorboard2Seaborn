#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(name='Tensorboard2Seaborn',
                 version='0.0.1',
                 description='Plot Tensorflow event in a beautiful way (using seaborn actually) instead of using Tensorboard.',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 license='MIT',
                 author='JamesChuanggg',
                 url="https://github.com/JamesChuanggg/Tensorboard2Seaborn",
                 install_requires=requirements,
                 packages=setuptools.find_packages(),
                 classifiers=(
                     "Intended Audience :: Developers",
                     "Intended Audience :: Education",
                     "Intended Audience :: Science/Research",
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ), entry_points='''
                    [console_scripts]
                    Tensorboard2Seaborn=Tensorboard2Seaborn.Tensorboard2Seaborn:main
                    ''',
                 )
