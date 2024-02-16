# generated by datamodel-codegen:
#   filename:  extension.json
#   timestamp: 2024-02-16T16:46:55+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, conint, constr

from . import semver


class Extension(BaseModel):
    """
    Extensions allow the schema to be extended using the framework without modification of the core schema. New attributes, objects, event classes, categories and profiles are all available to extensions.
    """

    model_config = ConfigDict(
        extra='forbid',
    )
    description: str = Field(..., description='A concise description of the extension.')
    caption: str = Field(
        ..., description='A short, human friendly name for the extension.'
    )
    name: constr(pattern=r'^[a-z0-9_]*$') = Field(
        ...,
        description='A name of the extension. It must be a unique name. The name is all lower case letters, combine words using underscore.',
    )
    uid: conint(ge=0) = Field(
        ..., description='The unique identifier for this extension.'
    )
    version: Optional[semver.SemVer] = Field(
        None, description='The version of this extension'
    )
