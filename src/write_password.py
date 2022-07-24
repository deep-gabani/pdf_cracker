"""Writes the password in a file."""
import apache_beam as beam
import typing as t
from src.colors import Colors, get_colored_text


class WritePassword(beam.DoFn):
    """Write the result to a file."""
    def __init__(self, input_pdf: str):
        self.input_pdf = input_pdf

    def process(self, result: t.Tuple[str, str]) -> t.Iterator[str]:
        """Writes the result to a file."""
        password, password_file = result
        with open(password_file, 'w') as f:
            f.write(password)

        yield ('Whohooo! The password for pdf ' +
               get_colored_text(self.input_pdf, Colors.header) +
               f' is: "{get_colored_text(password, Colors.okgreen)}".')
