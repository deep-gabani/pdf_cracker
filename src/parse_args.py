"""Parses command line arguments."""
import argparse
import typing as t


def parse_args() -> t.Tuple:
    """Parses arguments and returns a tuple of arguments."""
    parser = argparse.ArgumentParser(
        prog='pdf_cracker',
        description='PDF Password Cracker.'
    )

    parser.add_argument('-i', '--input_pdf',
                        type=str,
                        required=True,
                        help="Path of pdf file to crack.")
    parser.add_argument('-n', '--password_length',
                        type=int,
                        required=True,
                        help="Password length.")
    parser.add_argument('-l', '--lower_letters',
                        action='store_true',
                        default=False,
                        help="Flag to indicate if there are lower case letters in \
                            the password. Default = False.")
    parser.add_argument('-u', '--upper_letters',
                        action='store_true',
                        default=False,
                        help="Flag to indicate if there are upper case letters in \
                            the password. Default = False.")
    parser.add_argument('-d', '--digits',
                        action='store_true',
                        default=False,
                        help="Flag to indicate if there are digits in the password. \
                            Default = False.")
    parser.add_argument('-sc', '--special_chars',
                        action='store_true',
                        default=False,
                        help="Flag to indicate if there are special characters in \
                            the password. Default = False.")
    parser.add_argument('-w', '--whitespace',
                        action='store_true',
                        default=False,
                        help="Flag to indicate if there are whitespace in the password. \
                            Default = False.")
    parser.add_argument('-t', '--threads',
                        type=int,
                        default=1,
                        help="Number of threads to use.")

    args, pipeline_args = parser.parse_known_args()

    # For beam to use parallelism.
    if 'runner' not in pipeline_args:
        pipeline_args.extend('--runner DirectRunner'.split())
    if 'direct_num_workers' not in pipeline_args:
        pipeline_args.extend(f'--direct_num_workers {args.threads}'.split())
    if 'direct_running_mode' not in pipeline_args:
        pipeline_args.extend('--direct_running_mode multi_processing'.split())

    return (args.input_pdf,
            args.password_length,
            args.lower_letters,
            args.upper_letters,
            args.digits,
            args.special_chars,
            args.whitespace,
            args.threads,
            pipeline_args)
