from os import PathLike


def read_file(filepath: str | PathLike):
    with open(filepath, "r") as file:
        return file.read().strip()
