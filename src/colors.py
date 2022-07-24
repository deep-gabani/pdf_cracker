"""Colors utility. It is used to print text with famous command line colors."""
from dataclasses import dataclass


@dataclass
class Colors:
    """A class to represent the ANSI color codes."""
    # pylint: disable=too-many-instance-attributes
    header = '\033[95m'
    okblue = '\033[94m'
    okcyan = '\033[96m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


def get_colored_text(text: str, color: str) -> str:
    """Returns colored text"""
    return color + text + Colors.endc
