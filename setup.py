from setuptools import setup, find_packages
setup(
    name='footballscraper',
    version='0.0',
    description='Library to scrape football data from the web',
    url='https://github.com/mmassime/Football-data-scraper',
    classifiers=["Development Status :: 2 - Pre-Alpha",
                 "Natural Language :: English"],
    author='Mario Massimetti',
    author_email='mario.massimetti@gmail.com',
    packages=find_packages(),
    install_requires=['beautifulsoup4', 'requests', 'lxml']
)