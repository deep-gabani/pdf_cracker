"""Try to open PDF with given passwords one at a time."""
import typing as t
import pikepdf
import os
from tqdm import tqdm
import apache_beam as beam
from src.util import open_local


def try_passwords(input_pdf: str,
                  potential_passwords: t.List[str],
                  password_file: str) -> str:
    """Tries password one-by-one."""
    # If password file exists, then return.
    if os.path.exists(password_file):
        return ''

    iterator = tqdm(potential_passwords, desc='Cracking PDF...')

    with open_local(input_pdf) as local_pdf:
        for password in iterator:
            try:
                # If password_file file exists, then return.
                if os.path.exists(password_file):
                    return ''

                with pikepdf.open(local_pdf, password=password):
                    iterator.close()
                    return password
            except pikepdf._qpdf.PasswordError:
                continue
        return ''


class TryPasswords(beam.DoFn):
    """Tries passwords' list with input PDF."""
    def __init__(self, input_pdf: str, password_file: str):
        self.input_pdf = input_pdf
        self.password_file = password_file

    def process(self, password_list: t.List[str]) -> t.Iterator[
                                                    t.Tuple[str, str]]:
        """Applies passwords one-by-one."""
        password = try_passwords(self.input_pdf,
                                 potential_passwords=password_list,
                                 password_file=self.password_file)

        yield password, self.password_file
