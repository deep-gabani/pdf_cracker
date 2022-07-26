"""Cracking a password protected PDF."""
import logging
import os
from math import ceil
from src.parse_args import parse_args
from src.generate_passwords import generate_passwords, GeneratePasswordLists
from src.try_passwords import TryPasswords
from src.filter_result import filterResults
from src.write_password import WritePassword
from src.clean_up import CleanUp
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


if __name__ == '__main__':
    # Parses the command line arguments.
    (input_pdf, password_length, lower_letters, upper_letters, digits,
        special_chars, whitespace, threads, pipeline_args) = parse_args()
    pipeline_options = PipelineOptions(pipeline_args)

    # Generates all possible combinations of passwords.
    potential_passwords = generate_passwords(password_length=password_length,
                                             lower_letters=lower_letters,
                                             upper_letters=upper_letters,
                                             digits=digits,
                                             special_chars=special_chars,
                                             whitespace=whitespace)
    total_passwords = len(potential_passwords)
    passwords_per_job = min(ceil(total_passwords / threads),
                            50_000)
    total_jobs = threads * ceil(ceil(total_passwords / passwords_per_job) /
                                threads)

    # Password file.
    basename, pdf_extension = os.path.splitext(input_pdf)
    password_file = f'{basename}_password.txt'

    # Run the pipeline.
    try:
        with beam.Pipeline(options=pipeline_options) as p:
            (p
             | 'Create job indices' >> beam.Create([total_jobs])
             | 'Fetch passwords list' >> beam.ParDo(
                GeneratePasswordLists(
                    threads=threads,
                    potential_passwords=potential_passwords))
             | 'Reshuffle password lists' >> beam.Reshuffle()
             | 'Try passwords' >> beam.ParDo(
                TryPasswords(
                    input_pdf=input_pdf,
                    password_file=password_file))
             | 'Filter results' >> beam.Filter(filterResults)
             | 'Write result' >> beam.ParDo(
                WritePassword(
                    input_pdf=input_pdf))
             | 'Reshuffle results' >> beam.Reshuffle()
             | 'Print result' >> beam.Map(print)
             | 'Clean up' >> beam.ParDo(
                CleanUp(
                    password_file=password_file)))
    except Exception:
        logging.exception('Oh o! Could not find password!')
