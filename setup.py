# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst') as file:
    description = file.read()

setup(
    name='django-pipeline-handlebars',
    version='0.1',
    description='django-pipeline compiler for handlebars templates',
    long_description=description,
    author='Karol Sikora',
    author_email='karol.sikora@laboratorium,ee',
    url='http://laboratorium.ee',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'django-pipeline',
    ],
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)
