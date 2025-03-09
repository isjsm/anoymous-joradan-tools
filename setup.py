from setuptools import setup, find_packages
import os

setup(
    name='AnoymousJordan-Toolkit',
    version='2.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'scapy',
        'nmap',
        'flask',
        'pyfiglet',
        'sqlmap-api',
        'beautifulsoup4',
        'requests',
        'pycryptodome'
    ],
    entry_points={
        'console_scripts': [
            'anoymousjordan=anoymousjordan.core.cli:main'
        ]
    },
    data_files=[
        ('/etc/anoymousjordan', ['config/config.ini']),
        ('/var/log/anoymousjordan', [])
    ],
    author='Your Name',
    author_email='you@example.com',
    description='Security toolkit for educational purposes only',
    license='MIT',
    keywords='security network pentesting education',
    url='https://github.com/yourname/AnoymousJordan-Toolkit'
)
