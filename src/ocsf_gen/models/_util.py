import re
from pydantic import BaseModel
from typing import Any, Type


def validate_additional_properties(
    cls: Type[BaseModel],
    v: Any,
    type_: Type[BaseModel],
    pattern: str | None = None
) -> Any:
    if isinstance(v, dict):
        errors = {}
        for k, value in v.items():
            if k in cls.model_fields.keys():
                break

            if pattern is not None and re.match(pattern, k):
                v[k] = type_(**value)
        if errors:
            raise ValueError(errors)
    return v