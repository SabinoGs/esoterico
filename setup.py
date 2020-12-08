import os
from setuptools import setup
from esoterico import __version__ as version


dev_requirements = [
    'pytest',
    'ipdb',
    'flake8',
    'pytest-cov',
    'autopep8'
]

production_requirements = [
    'fastapi',
    'uvicorn[standard]',
    'gunicorn',
    'pydantic[email]'
]

setup(
    name = 'esoterico',
    version = version,
    author = 'Gustavo Sabino',
    author_email = 'gustavo.sabino.contact@gmail.com',
    install_requires=production_requirements,
    extras_require={
        'dev': dev_requirements
    }

)