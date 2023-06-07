from setuptools import setup, find_packages

setup(
    name='OneSDKPOC',
    version='1.0.0',
    author='Kavyansh Pandey',
    author_email='kavyansg@aviz.com',
    description='Python SDK ONES POC',
    url= 'github.com/test',
    packages=find_packages(),
    install_requires=[
        'certifi==2023.5.7',
        'cffi==1.15.1',
        'charset-normalizer==3.1.0',
        'cryptography==40.0.2',
        'idna==3.4',
        'pycparser==2.21',
        'pyOpenSSL==23.1.1',
        'python-dotenv==1.0.0',
        'requests==2.30.0',
        'urllib3==1.26.7'
    ]
)