"""Try to open PDF with given passwords one at a time."""
import typing as t
import pikepdf
from tqdm import tqdm


def try_passwords(input_pdf: str, potential_passwords: t.List[str]) -> str:
    """Tries password one-by-one."""
    iterator = tqdm(potential_passwords, desc='Cracking PDF...')
    for password in iterator:
        try:
            with pikepdf.open(input_pdf, password=password):
                iterator.close()
                return password
        except pikepdf._qpdf.PasswordError:  # pylint: disable=protected-access,c-extension-no-member
            continue
    return ''
