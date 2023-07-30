from setuptools import setup, find_packages

setup(
    name='ones-pyapi',
    version='1.0.0',
    description='ONES python SDK for Engineers to integrate ONES with other applications and insights of network infra in real quick',
    author='Kavyansh',
    author_email='kavyansh.pandey@aviznetworks.com',
    url='https://github.com/AvizNetworks/ones-pyapi',
    packages=find_packages(),
    install_requires=[
        'certifi==2023.5.7',
        'cffi==1.15.1',
        'charset-normalizer==3.1.0',
        'cryptography==40.0.2',
        'idna==3.4',
        'pycparser==2.21',
        'python-dotenv==1.0.0',
        'requests==2.30.0',
        'urllib3==1.26.7'
    ],
)