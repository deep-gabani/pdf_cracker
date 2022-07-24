"""Utilities for cracking passwords of a PDF."""
from dataclasses import dataclass
from itertools import product
import typing as t
import pikepdf
from tqdm import tqdm

ASCII_LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# DIGITS = '0123456789'
DIGITS = '39315'
SPECIAL_CHARS = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
WHITESPACE = ' \t\n\r\x0b\x0c'


@dataclass
class Colors:
    """A class to represent the ANSI color codes."""
    # pylint: disable=too-many-instance-attributes
    header = '\033[95m'
    okblue = '\033[94m'
    okcyan = '\033[96m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


def get_colored_text(text: str, color: str) -> str:
    """Returns colored text"""
    return color + text + Colors.endc


def create_potential_passwords(password_length: int,
                               letters: bool,
                               digits: bool,
                               special_chars: bool,
                               whitespace: bool) -> t.List[str]:
    """
    Create a list of potential passwords for the given total number of letters.

    Args:
        password_length: The total number of letters in the password.
        digits: Flag to indicate if there are digits in the password.
        special_chars: Flag to indicate if there are special characters in the password.
        whitespace: Flag to indicate if there are whitespace in the password.
    Returns:
        A list of potential passwords.
    """
    possible_chars = ''
    if letters:
        possible_chars += ASCII_LETTERS
    if digits:
        possible_chars += DIGITS
    if special_chars:
        possible_chars += SPECIAL_CHARS
    if whitespace:
        possible_chars += WHITESPACE

    # Convert the letters into a list of characters.
    possible_chars_list = list(possible_chars)

    # Compute all possible combinations of length: password_length.
    all_combinations = product(possible_chars_list, repeat=password_length)
    all_combinations = [''.join(c) for c in all_combinations]

    print(f'Found {len(all_combinations)} possible combinations...')
    return all_combinations


def crack_pdf(input_pdf: str, potential_passwords: t.List[str]) -> str:
    """Open the PDF file."""
    iterator = tqdm(potential_passwords, desc='Cracking PDF...')
    for password in iterator:
        try:
            with pikepdf.open(input_pdf, password=password):
                iterator.close()
                return password
        except pikepdf._qpdf.PasswordError:  # pylint: disable=protected-access,c-extension-no-member
            continue
    return ''
