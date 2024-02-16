import json
from pathlib import Path
from typing import Generic, Iterable, Optional, Type, TypeVar

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


_T = TypeVar("_T", bound=BaseModel)


class _TypeLoader(Generic[_T]):
    """
    Helper class for loading OCSF models.
    """
    def __init__(
        self,
        base_path: Path,
        ocsf_type: Type[_T]
    ) -> None:
        self._base_path = base_path
        self._ocsf_type = ocsf_type
    
    def from_file(self, path: str) -> Optional[_T]:
        path_to_load = self._base_path / path
        if not path_to_load.exists():
            return None

        with open(self._base_path / path) as fp:
            dictionary = json.load(fp)
        
        model = self._ocsf_type(**dictionary)
        return model

    def from_glob(self, pattern: str) -> list[_T]:
        matches = self._base_path.glob(pattern)
        models = []
        for match in matches:
            with open(match) as fp:
                dictionary = json.load(fp)
        
            model = self._ocsf_type(**dictionary)
            models.append(model)
        
        return models


def _load_ocsf_schema_definition(path: Path) -> OcsfSchemaDefinition:
    """
    Load the full object model for a single OCSF schema definition in the given path.
    """
    categories = _TypeLoader(path, Categories).from_file("categories.json")
    dictionary = _TypeLoader(path, Dictionary).from_file("dictionary.json")
    events = _TypeLoader(path, Event).from_glob("events/**/*.json")
    extension = _TypeLoader(path, Extension).from_file("extension.json")
    includes = _TypeLoader(path, Include).from_glob("includes/**/*.json")
    objects = _TypeLoader(path, Object).from_glob("objects/**/*.json")
    profiles = _TypeLoader(path, Profile).from_glob("profiles/**/*.json")

    definition = OcsfSchemaDefinition(
        categories=categories,
        dictionary=dictionary,
        events=events,
        extension=extension,
        includes=includes,
        objects=objects,
        profiles=profiles
    )

    return definition


def _enumerate_schema_paths(base_path: Path) -> Iterable[Path]:
    yield base_path

    # find extensions under the main folder
    extensions = base_path.glob("extensions/**/extension.json")
    for extension in extensions:
        # return the parent folder of the extension.json file
        yield extension.parent


def run(options: Options) -> None:
    schema_paths = _enumerate_schema_paths(base_path=options.path)

    definitions = []
    for path in schema_paths:
        definition = _load_ocsf_schema_definition(path)
        definitions.append(definition)

    print(len(definitions))