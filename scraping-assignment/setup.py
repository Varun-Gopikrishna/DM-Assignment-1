try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'description': 'reference',
    'author': 'Varun Gopikrishna',
    'author_email': 'varun.gopikrishna@uoit.net',
    'version': '0.0.1',
    'packages': find_packages(),
    'name': 'scrape-package'
}

setup(**config)
