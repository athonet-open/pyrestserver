import os
from codecs import open as enc_open
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

#with enc_open(os.path.join(here, 'VERSION'), encoding='utf-8') as f:
#    VERSION = f.read().strip()

with enc_open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyrestserver',
    version="1.0.0",
    description='Athonet Test simple REST server',
    long_description=long_description,
    url='',
    author='Athonet S.r.l.',
    author_email='stefano.sasso@athonet.com',
    license='Other/Proprietary License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: System Administrators',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: System :: Networking',
        'Operating System :: POSIX :: Linux'
    ],
    keywords='athonet test rest',
    packages=find_packages(),
    package_data={},
    entry_points={'console_scripts': ['py-rest-server=pyrestserver.pyrestserver:main']},
    install_requires=["simplejson"],
    zip_safe=False)