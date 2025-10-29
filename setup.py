from setuptools import setup, find_packages

setup(
    name='datacleaningtoolkit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy'
    ],
    description='Reusable Python utilities for data wrangling and validation',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/your-username/data_cleaning_toolkit',
)
