# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='ploto-esmdiag',

    version='0.2',

    description='A ploto extension for esmdiag.',
    long_description=__doc__,

    packages=find_packages(exclude=["tests", "vendor", "docker"]),

    include_package_data=True,

    package_data={
        '': ['*.ncl'],
    },

    zip_safe=False,

    install_requires=[
        'click',
        'pyyaml',
        'requests',
        'loguru',
        'celery',
        'netCDF4',
        'elasticsearch==6.3.1',
        'redis',
        'ploto',
    ],

    extras_require={
        'test': [],
    }
)