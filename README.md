# Fernet

A command-line tool that implements [Fernet encryption](https://cryptography.io/en/latest/fernet/).

    usage: fernet [-h] [-p PASSWORD] [-r] {encrypt,decrypt} input_file output_file

    Encrypt or decrypt a file based on a password.

    positional arguments:
      {encrypt,decrypt}     Mode of operation: encrypt or decrypt
      input_file            Input file to be encrypted/decrypted
      output_file           Output file after encryption/decryption

    options:
      -h, --help            show this help message and exit
      -p PASSWORD, --password PASSWORD
                            Password for encryption/decryption (optional). Can
                            also be specified in the 'FERNET_PASSWORD' environment
                            variable. Otherwise, it will be read from the
                            terminal.
      -r, --raw             Use "raw" Fernet encrypted format rather than the default.

## Format

The normal format this tool writes Fernet data in is as follows:

- 20 bytes of base85 encoded salt.
- 5 bytes of magic: "#UF1#"
- Blocks of 54712 bytes of Fernet encrypted data.  The final block will be less than this length.

## Format (raw)

If the "--raw" option is given, the file format is:

- 16 bytes of salt (expect to be non-ascii).
- Blocks of 54712 bytes of Fernet encrypted data.  The final block will be less than this length.
