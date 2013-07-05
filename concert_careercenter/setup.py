#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['concert_careercenter'],
    package_dir={'':'src'},
    requires=['rospy','concert_msgs']
)

setup(**d)
