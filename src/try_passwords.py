"""Try to open PDF with given passwords one at a time."""
import typing as t
import pikepdf
from tqdm import tqdm
import apache_beam as beam
from src.colors import Colors, get_colored_text


def try_passwords(input_pdf: str, potential_passwords: t.List[str]) -> str:
    """Tries password one-by-one."""
    iterator = tqdm(potential_passwords, desc='Cracking PDF...')
    for password in iterator:
        try:
            with pikepdf.open(input_pdf, password=password):
                iterator.close()
                return password
        except pikepdf._qpdf.PasswordError:
            continue
    return ''


class TryPasswords(beam.DoFn):
    """Tries passwords' list with input PDF."""
    def __init__(self, input_pdf: str):
        self.input_pdf = input_pdf

    def process(self, password_list: t.List[str]) -> t.Iterator[str]:
        """Applies passwords one-by-one."""
        password = try_passwords(self.input_pdf, password_list)

        # Yields the result.
        if password:
            result = ('Whohooo! The password for pdf ' +
                      get_colored_text(self.input_pdf, Colors.header) +
                      f' is: "{get_colored_text(password, Colors.okgreen)}".')
        else:
            result = ''

        yield result
