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
- Blocks of 54712 bytes of Fernet encrypted data.  The final block will be less
  than this length.

I'm calling this format "uPlaybook Fernet" because I built it for use in the
[uPlaybook project](https://github.com/linsomniac/uplaybook) and there doesn't seem
to be any sort of format for Fernet encryption persisting.

I chose this format because the base Fernet encrypted data seems to be ASCII
encoded, so let's make the salt also ASCII, and I wanted to put a [magic
number](https://en.wikipedia.org/wiki/Magic_number_(programming)#In_files) in there
to allow identifying of the file and also allow for versions of files in case a
future format shift is warranted.

The block size was chosen as that is the encrypted size of input blocks of 40960
bytes.  This is slightly more space efficient than 4096 bytes, but still fairly
reasonable for even small machines to be able to handle, in 2023.

I'm calling this "uPlaybook Fernet Format 1".

## Format (raw)

If the "--raw" option is given, the file format is:

- 16 bytes of salt (expect to be non-ascii).
- Blocks of 54712 bytes of Fernet encrypted data.  The final block will be less than this length.

This is, as far as I understand it, the most basic format of Fernet encrypted data,
and foregoes my magic number, so this might be able to read files written by someone
who is unaware of my format above.  Assuming either they chose 40K block size, or
their encrypted data is less than 40K.

This could also be considered "uPlaybook Format 0", the format used by uPlaybook
before I decided to add the magic.

## License

CC0 1.0 Universal, see LICENSE file for more information.

<!-- vim: ts=4 sw=4 ai et tw=85
-->
