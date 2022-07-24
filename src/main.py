"""Cracking a password protected PDF."""
import typing as t
import argparse
from util import Colors, get_colored_text
from util import create_potential_passwords, crack_pdf


def parse_arguments() -> t.Tuple:
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


if __name__ == '__main__':
    input_pdf, password_length, letters, digits, special_chars, whitespace = parse_arguments()

    potential_passwords = create_potential_passwords(password_length=password_length,
                                                     letters=letters,
                                                     digits=digits,
                                                     special_chars=special_chars,
                                                     whitespace=whitespace)

    password = crack_pdf(input_pdf, potential_passwords)
    if password:
        print(f'Whohooo! The password for pdf {get_colored_text(input_pdf, Colors.header)} is: ' +
              f'"{get_colored_text(password, Colors.okgreen)}".')
    else:
        print(get_colored_text(
            'Oh o! Could not crack it with the arguments given. Try with different ones!',
            Colors.fail))
