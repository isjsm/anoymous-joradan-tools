from setuptools import setup, find_packages
import os

setup(
    name='anoymousjordan',
    version='2.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'scapy',
        'flask',
        'requests',
        'beautifulsoup4',
        'sqlmap-api',
        'cryptography',
        'pyopenssl',
        'pyfiglet'
    ],
    entry_points={
        'console_scripts': [
            'anoymousjordan=anoymousjordan.core.cli:main'
        ]
    },
    data_files=[
        ('/etc/anoymousjordan', ['config/config.ini']),
        ('/var/log/anoymousjordan', []),
        ('/usr/share/anoymousjordan/templates', 
            ['templates/facebook.html', 'templates/gmail.html'])
    ],
    author='Anoymous Jordan Team',
    description='Educational Security Toolkit for Network Analysis',
    license='MIT',
    url='https://github.com/isjsm/anoymous-joradan-tools'
)
