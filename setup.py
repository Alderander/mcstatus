import sys

from setuptools import setup

PY2 = sys.version_info[0] == 2

install_requires = [
    'Click'
]

setup(
    name='mcstatus',
    version='3.0.0',
    author='Nathan Adams',
    author_email='dinnerbone@dinnerbone.com',
    url='https://pypi.python.org/pypi/mcstatus',
    packages=['mcstatus', 'mcstatus.protocol', 'mcstatus.scripts'],
    description='A library to query Minecraft Servers for their status and capabilities.',
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points='''
        [console_scripts]
        mcstatus=mcstatus.scripts.mcstatus:cli
    ''',
)
