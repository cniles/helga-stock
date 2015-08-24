from pip.req import parse_requirements
from setuptools import setup, find_packages

from pip.req import parse_requirements
from helga_stock import __version__ as version
from pip.download import PipSession

requirements = [
    str(req.req) for req in parse_requirements('requirements.txt', session=PipSession())
]

setup(
    name='helga-stock',
    version=version,
    description=('Helga plugin that gives stock information'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat :: Internet Relay Chat'],
    keywords='irc bot stock stocks',
    author='Craig Niles',
    author_email='niles.c@gmail.com',
    url='https://github.com/cniles/helga-stock',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['helga_stock.plugin'],
    zip_safe=True,
    install_requires=requirements,
    test_suite='tests.test_util',
    entry_points = dict(
        helga_plugins=[
            'stock = helga_stock.plugin:stock',
        ],
        helga_webhooks=[
            'stock-route = helga_stock.webhooks:stock_route',
        ],
    ),
)
