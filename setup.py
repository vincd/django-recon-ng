import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='Django-Recon-ng',
    version='0.1',
    packages=['django_recon_ng'],
    include_package_data=True,
    description='Use Django to manage Recon-NG data.',
    long_description=README,
    url='https://github.com/vincd/django-recon-ng',
    author='Vincent D.',
    author_email='vinc.dep@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)