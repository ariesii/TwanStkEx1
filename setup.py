try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A Python program to show/analyse Taiwan stock data that got from Yahoo! Finance.',
    'author': 'kueihua chang',
    'url': 'https://github.com/kueihua100/TwanStkEx1',
    'download_url': 'https://github.com/kueihua100/TwanStkEx1',
    'author_email': 'kueihua.chang@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['TwanStkEx1'],
    'scripts': [],
    'name': 'TwanStkEx1'
}

setup(**config)