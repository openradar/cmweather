#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().strip().split('\n')

with open('README.md') as f:
    long_description = f.read()

setup(
    maintainer='Open Radar Community',
    maintainer_email='mgrover@anl.gov',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
    ],
    description='A library of useful colormaps when visualizing weather and climate data, with numerous color vision deficiency friendly options',
    install_requires=requirements,
    setup_requires='setuptools_scm',
    license='MIT license',
    long_description=long_description,
    include_package_data=True,
    keywords='cmweather',
    name='cmweather',
    packages=find_packages(include=['cmweather', 'cmweather.*']),
    url='https://github.com/openradar/cmweather',
    project_urls={
        'Documentation': 'https://github.com/openradar/cmweather',
        'Source': 'https://github.com/openradar/cmweather',
        'Tracker': 'https://github.com/openradar/cmweather/issues',
    },
    zip_safe=False,
    use_scm_version={
        'version_scheme': 'post-release',
        'local_scheme': 'dirty-tag',
    },
)
