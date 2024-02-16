from . import parser
from .options import Options


def run(options: Options) -> None:
    parser.run(options)