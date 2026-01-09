# SPDX-FileCopyrightText: 2025 Kota Matsura <s24c1110qm@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause
from glob import glob
import os

from setuptools import setup

package_name = 'robosys2025_homework2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mkota',
    maintainer_email='s24c1110qm@s.chibakoudai.jp',
    description='Virtual Environmental Sensor Toolkit',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor = robosys2025_homework2.sensor:main',
            'monitor = robosys2025_homework2.monitor:main',
        ],
    },
)
