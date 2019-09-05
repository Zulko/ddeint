import ez_setup

ez_setup.use_setuptools()

from setuptools import setup, find_packages

exec(open("ddeint/version.py").read())  # loads __version__

setup(
    name="ddeint",
    version=__version__,
    author="Zulko",
    description="Scipy-based Delay Differential Equations solver",
    long_description=open("README.md").read(),
    license="see LICENSE.txt",
    keywords="delay differential equation DDE",
    packages=find_packages(exclude="docs"),
    install_requires=["numpy", "scipy"],
)
