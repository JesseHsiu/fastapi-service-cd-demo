import os
from pathlib import Path


def get_project_root(path=__file__) -> Path:
    # return Path(path).parent.parent.parent
    directory = os.path.dirname(path)
    while directory != "/":
        p = os.path.join(directory, "Pipfile")
        if os.path.isfile(p):
            return directory
        directory = os.path.dirname(directory)

    return None
