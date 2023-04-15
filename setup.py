from setuptools import setup

readme = open('README.md', 'r').read()

setup(
    name="fernetcrypt",
    version="1.0.0",
    description="FernetCrypt CLI Encrypt and decrypt files using a password.",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Sean Reifschneider",
    author_email="jafo00@gmail.com",
    url="https://github.com/linsomniac/fernetcrypt",
    scripts=["fernetcrypt"],
    install_requires=[
        "cryptography",
    ],
    classifiers=[
        # Classifiers for PyPI
        "Development Status :: 5 - Production/Stable",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
