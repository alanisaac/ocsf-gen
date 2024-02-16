from .models.categories import Categories
from .models.dictionary import Dictionary
from .models.event import Event
from .models.extension import Extension
from .models.include import Include
from .models.object import Object
from .models.profile import Profile


class OcsfSchemaDefinition:
    categories: Categories
    dictionary: Dictionary
    events: list[Event]
    extensions: list[Extension]
    includes: list[Include]
    objects: list[Object]
    profiles: list[Profile]