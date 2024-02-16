# generated by datamodel-codegen:
#   filename:  profile.json
#   timestamp: 2024-02-16T16:46:55+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, constr


class Meta(Enum):
    """
    A value indicating the type of this profile.
    """

    profile = 'profile'


class Attributes(BaseModel):
    """
    A dictionary of attributes for the profile.
    """

    model_config = ConfigDict(
        extra='forbid',
    )
    field_include: Optional[List[str]] = Field(
        None,
        alias='$include',
        description='A reference to another schema for attributes to include.',
    )


class Profile1(BaseModel):
    """
    Profiles are overlays on event classes and objects, effectively a dynamic mix-in class of attributes with their requirements and constraints.
    """

    model_config = ConfigDict(
        extra='forbid',
    )
    annotations: Optional[Dict[str, Any]] = Field(
        None,
        description='Annotations for this profile describing categories it belongs in.',
    )
    caption: str = Field(
        ..., description='A short, human friendly name for the profile.'
    )
    description: str = Field(..., description='A concise description of the profile.')
    extends: Optional[str] = Field(
        None, description='A profile that this one extends from.'
    )
    meta: Meta = Field(..., description='A value indicating the type of this profile.')
    name: constr(pattern=r'^[a-z0-9_]*$') = Field(
        ...,
        description='A name of the profile. It must be a unique name. The name is all lower case letters, combine words using underscore.',
    )
    attributes: Attributes = Field(
        ..., description='A dictionary of attributes for the profile.'
    )


class Profile2(BaseModel):
    """
    Profiles are overlays on event classes and objects, effectively a dynamic mix-in class of attributes with their requirements and constraints.
    """

    model_config = ConfigDict(
        extra='forbid',
    )
    annotations: Optional[Dict[str, Any]] = Field(
        None,
        description='Annotations for this profile describing categories it belongs in.',
    )
    caption: Optional[str] = Field(
        None, description='A short, human friendly name for the profile.'
    )
    description: Optional[str] = Field(
        None, description='A concise description of the profile.'
    )
    extends: str = Field(..., description='A profile that this one extends from.')
    meta: Optional[Meta] = Field(
        None, description='A value indicating the type of this profile.'
    )
    name: Optional[constr(pattern=r'^[a-z0-9_]*$')] = Field(
        None,
        description='A name of the profile. It must be a unique name. The name is all lower case letters, combine words using underscore.',
    )
    attributes: Optional[Attributes] = Field(
        None, description='A dictionary of attributes for the profile.'
    )


class Profile(RootModel[Union[Profile1, Profile2]]):
    root: Union[Profile1, Profile2] = Field(
        ...,
        description='Profiles are overlays on event classes and objects, effectively a dynamic mix-in class of attributes with their requirements and constraints.',
        title='Profile',
    )
