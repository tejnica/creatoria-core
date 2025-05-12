from setuptools import setup, find_packages

setup(
    name='creatoria-core',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'creatoria-cli = creatoria_core.cli:main',
        ],
    },
)
