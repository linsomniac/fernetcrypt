from setuptools import setup

setup(
    name="fernetcrypt",
    version="1.0.0",
    description="FernetCrypt CLI Encrypt and decrypt files using a password.",
    long_description="""
A command-line tool that implements [Fernet encryption](https://cryptography.io/en/latest/fernet/).

FernetCrypt encryption is a Python library that implement best-practices for encrypting
data using a password.

Fernet is a combination of AES, PKCS7, HMAC, and SHA256 for doing the heavy lifting.

This tool includes a "raw" mode which just writes the raw salt and then the
encrypted data, or the normal mode which stores the salt in base85 format and also
includes a file identification magic string "#UF1#".  In either case, the data is
blocked in 40,960 bytes to allow for encrypting files larger than memory.
    """,
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
