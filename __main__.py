"""Cracking a password protected PDF."""
import logging
import typing as t
from src.parse_args import parse_args
from src.generate_passwords import generate_passwords
from src.try_passwords import TryPasswords
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


class FetchPasswordsList(beam.DoFn):
    """Fetches passwords' list of this worker."""
    def __init__(self, threads: int, potential_passwords: t.List[str]):
        self.threads = threads
        self.potential_passwords = potential_passwords

    def process(self, worker_index: int) -> t.Iterator[t.List[str]]:
        """Cuts out the password list for the given worker index."""
        num_of_passwords_per_worker = int(len(self.potential_passwords)
                                          / self.threads)
        password_list = self.potential_passwords[
            worker_index * num_of_passwords_per_worker:
            (worker_index + 1) * num_of_passwords_per_worker]
        yield password_list


def nonNoneResults(result: str):
    return result != ''


if __name__ == '__main__':
    # Parses the command line arguments.
    (input_pdf, password_length, letters, digits, special_chars, whitespace,
        threads, pipeline_args) = parse_args()
    pipeline_options = PipelineOptions(pipeline_args)

    # Generates all possible combinations of passwords.
    potential_passwords = generate_passwords(password_length=password_length,
                                             letters=letters,
                                             digits=digits,
                                             special_chars=special_chars,
                                             whitespace=whitespace)

    try:
        with beam.Pipeline(options=pipeline_options) as p:
            (p
             | 'Create worker index' >> beam.Create(list(range(threads)))
             | 'Reshuffle worker indices' >> beam.Reshuffle()
             | 'Fetch passwords list' >> beam.ParDo(
                FetchPasswordsList(
                    threads=threads,
                    potential_passwords=potential_passwords))
             | 'Reshuffle password lists' >> beam.Reshuffle()
             | 'Try passwords' >> beam.ParDo(
                TryPasswords(
                    input_pdf=input_pdf))
             | 'Reshuffle results' >> beam.Reshuffle()
             | 'Filter results' >> beam.Filter(nonNoneResults)
             | 'Show results' >> beam.Map(print))
    except Exception as e:
        logging.exception(f'Received error: {e}')
