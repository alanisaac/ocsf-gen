import json
from pathlib import Path
from typing import Type

from pydantic import BaseModel

from .defs import OcsfSchemaDefinition
from .options import Options
from .models.categories import Categories
from .models.dictionary import Dictionary
from .models.event import Event
from .models.extension import Extension
from .models.include import Include
from .models.object import Object
from .models.profile import Profile

_MATCHERS: dict[str, Type[BaseModel]] = {
    r"**/categories.json": Categories,
    r"**/dictionary.json": Dictionary,
    r"**/events/**/*.json": Event,
    r"extensions/*/extension.json": Extension,
    r"**/includes/**/*.json": Include,
    r"**/objects/**/*.json": Object,
    r"**/profiles/**/*.json": Profile,
}


def _load_ocsf_schema_definition(path: Path) -> OcsfSchemaDefinition:
    """
    Load the full object model for the OCSF schema in question.
    """
    ignores = set(path.glob(r"**/metaschema/*"))

    for pattern, type_ in _MATCHERS.items():
        matches = path.glob(pattern)
        filtered_matches = [match for match in matches if match not in ignores]
        for match in filtered_matches:
            with open(match) as fp:
                dictionary = json.load(fp)

            try:
                model = type_(**dictionary)
            except:
                print(match)
                raise


def run(options: Options) -> None:
    _load_ocsf_schema_definition(path=options.path)