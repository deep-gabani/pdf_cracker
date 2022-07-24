"""General utility methods."""
import contextlib
import typing as t
import tempfile
import shutil
from apache_beam.io.filesystems import FileSystems


@contextlib.contextmanager
def open_local(uri: str) -> t.Iterator[str]:
    """Copy input uri file from cloud storage or local, to local temp file."""
    with FileSystems().open(uri) as source_file:
        with tempfile.NamedTemporaryFile() as dest_file:
            shutil.copyfileobj(source_file, dest_file)
            dest_file.flush()
            dest_file.seek(0)
            yield dest_file.name
