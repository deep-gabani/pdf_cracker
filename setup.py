"""Setup pdf-cracker.

This setup.py script makes use of Apache Beam's recommended way to install
non-python dependencies to worker images.

Please see this documentation and example code:
- https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/#nonpython
- https://github.com/apache/beam/blob/master/sdks/python/apache_beam/examples/complete/juliaset/setup.py
"""

import subprocess
from distutils.command.build import build as _build  # type: ignore

from setuptools import setup, find_packages, Command

base_requirements = [
    "apache-beam[gcp]",
    "dataclasses",
    "pikepdf",
    "tqdm"
]


# This class handles the pip install mechanism.
class build(_build):
    """A build command class that will be invoked during package install.
    The package built using the current setup.py will be staged and later
    installed in the worker using `pip install package'. This class will be
    instantiated during install for this specific scenario and will trigger
    running the custom commands specified.
    """
    sub_commands = _build.sub_commands + [('CustomCommands', None)]


CUSTOM_COMMANDS = [
    cmd.split() for cmd in [
        'apt-get update'
    ]
]


class CustomCommands(Command):
    """A setuptools Command class able to run arbitrary commands."""

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def RunCustomCommand(self, command_list):
        print('Running command: %s' % command_list)
        p = subprocess.Popen(
            command_list,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)

        stdout_data, _ = p.communicate()
        print('Command output: %s' % stdout_data)
        if p.returncode != 0:
            raise print(
                'Command %s failed: exit code: %s' % (command_list, p.returncode))

    def run(self):
        for command in CUSTOM_COMMANDS:
            self.RunCustomCommand(command)


setup(
    name='pdf-cracker',
    packages=find_packages(),
    author='Deep',
    author_email='16bit052@nirmauni.ac.in',
    version='2.0.0',
    description='A utility to crack open password-protected PDFs.',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    platforms=['darwin', 'linux'],
    python_requires='>=3.7, <3.9',
    install_requires=base_requirements,
    scripts=['__main__.py'],
    cmdclass={
        'build': build,
        'CustomCommands': CustomCommands,
    }
)
