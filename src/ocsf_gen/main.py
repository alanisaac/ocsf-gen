import argparse
import os
import sys
from typing import Sequence

from .app import run
from .options import Options

def main(args: Sequence[str] | None = None) -> None:
    if args is None:
        args = sys.argv[1:]

    parsed_args = _parse_args(args)
    options = Options(**vars(parsed_args))
    run(options)


def _parse_args(args: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="ocsf-gen",
        description="Tool to generate a variety of encodings from OCSF schema definition files.",
    )
    parser.add_argument(
        'path',
        nargs='?',
        default=os.getcwd(),
        help="The path to the directory to generate encodings from."
    )

    parsed = parser.parse_args(args)
    return parsed
