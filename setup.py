import os
from setuptools import setup, find_packages

BASEDIR = os.path.dirname(os.path.abspath(__file__))
VERSION = open(os.path.join(BASEDIR, 'VERSION')).read().strip()

# Dependencies (format is 'PYPI_PACKAGE_NAME[>=]=VERSION_NUMBER')
BASE_DEPENDENCIES = [
    'wf-process-cuwb-data>=0.6.0',
]
# TEST_DEPENDENCIES = [
# ]
#
DEVELOPMENT_DEPENDENCIES = [
    'autopep8>=1.5.2'
]

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(BASEDIR))

setup(
    name='wf-honeycomb-service-event-producer',
    packages=find_packages(),
    version=VERSION,
    include_package_data=True,
    description='Honeycomb service for extracting and writing events from sensor data',
    long_description=open('README.md').read(),
    url='https://github.com/WildflowerSchools/wf-honeycomb-service-event-producer',
    author='Benjamin Jaffe-Talberg',
    author_email='ben.talberg@wildflowerschools.org',
    install_requires=BASE_DEPENDENCIES,
    # tests_require=TEST_DEPENDENCIES,
    extras_require={
        'development': DEVELOPMENT_DEPENDENCIES
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
