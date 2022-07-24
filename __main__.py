"""Cracking a password protected PDF."""
from src.colors import Colors, get_colored_text
from src.parse_args import parse_args
from src.generate_passwords import generate_passwords
from src.try_passwords import try_passwords


if __name__ == '__main__':
    input_pdf, password_length, letters, digits, special_chars, whitespace = parse_args()

    potential_passwords = generate_passwords(password_length=password_length,
                                             letters=letters,
                                             digits=digits,
                                             special_chars=special_chars,
                                             whitespace=whitespace)

    password = try_passwords(input_pdf, potential_passwords)
    if password:
        print(f'Whohooo! The password for pdf {get_colored_text(input_pdf, Colors.header)} is: ' +
              f'"{get_colored_text(password, Colors.okgreen)}".')
    else:
        print(get_colored_text(
            'Oh o! Could not crack it with the arguments given. Try with different ones!',
            Colors.fail))
