"""Clean up utility."""
import os
import typing as t
import apache_beam as beam


class CleanUp(beam.DoFn):
    """Cleans up the output of a Beam pipeline."""
    def __init__(self, password_file: str):
        self.password_file = password_file

    def process(self, _: t.Any):
        """Cleans up password file."""
        if os.path.exists(self.password_file):
            os.remove(self.password_file)
