from pydantic import BaseModel
from typing import Optional

from .models.categories import Categories
from .models.dictionary import Dictionary
from .models.event import Event
from .models.extension import Extension
from .models.include import Include
from .models.object import Object
from .models.profile import Profile


class OcsfSchemaDefinition(BaseModel):
    """
    Represents a single OCSF schema definition.
    """
    categories: Optional[Categories]
    dictionary: Optional[Dictionary]
    extension: Optional[Extension]
    events: list[Event]
    includes: list[Include]
    objects: list[Object]
    profiles: list[Profile]