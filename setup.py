from setuptools import setup, find_packages

setup(
    name='cli_api_client',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click==7.1.2',
        'requests==2.25.1',
        'injector==0.18.0',
    ],
    entry_points={
        'console_scripts': [
            'cli_api_client = cli_api_client.main:cli',
        ],
    },
)
