"""Filter out results which are empty strings."""
import typing as t
import os


def filterResults(result: t.Tuple[str, str]):
    """Filters result which are not an empty string."""
    password, password_file = result
    return password != '' and not os.path.exists(password_file)
