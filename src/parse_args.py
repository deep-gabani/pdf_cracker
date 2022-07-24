"""Parses command line arguments."""
import argparse
import typing as t


def parse_args() -> t.Tuple:
    """Parses arguments and returns a tuple of arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_pdf', type=str, required=True,
                        help="Path of pdf file to crack.")
    parser.add_argument('-n', '--password_length', type=int, required=True,
                        help="Password length.")
    parser.add_argument('-l', '--letters', action='store_true', default=False,
                        help="Flag to indicate if there are letters in the password. \
                            Default = False.")
    parser.add_argument('-d', '--digits', action='store_true', default=False,
                        help="Flag to indicate if there are digits in the password. \
                            Default = False.")
    parser.add_argument('-sc', '--special_chars', action='store_true',
                        default=False,
                        help="Flag to indicate if there are special characters in the password. \
                            Default = False.")
    parser.add_argument('-w', '--whitespace', action='store_true',
                        default=False,
                        help="Flag to indicate if there are whitespace in the password. \
                            Default = False.")

    args = parser.parse_args()

    return (args.input_pdf,
            args.password_length,
            args.letters,
            args.digits,
            args.special_chars,
            args.whitespace)
