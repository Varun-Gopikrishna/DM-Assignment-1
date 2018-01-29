try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'description': 'scraping for uoit events in 2017',
    'author': 'Varun Gopikrishna',
    'author_email': 'varun.gopikrishna@uoit.net',
    'version': '0.0.1',
    'packages': find_packages(),
    'name': 'scrape-assignment'
}

setup(**config)
