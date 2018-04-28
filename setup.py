from setuptools import setup

setup(
    name = "compbio2",
    version = ".1",
    author = "Ben Holmes",
    author_email = "ben@coolship.io",
    license = "MIT",
    keywords = "zlab",
    url = "http://github.com/bh0085/compbio2",
    install_requires=['numpy','scipy', 'biopython','aiohttp','ipython','aiohttp-devtools'],
    packages=['']
)
