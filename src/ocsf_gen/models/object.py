# generated by datamodel-codegen:
#   filename:  object.json
#   timestamp: 2024-02-16T16:46:55+00:00

from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, constr

from . import deprecated, observable


class Constraints(BaseModel):
    """
    Constraints that apply to the attribute requirements.
    """

    model_config = ConfigDict(
        extra='forbid',
    )
    at_least_one: Optional[List[str]] = None
    just_one: Optional[List[str]] = None


class Attributes(BaseModel):
    """
    A dictionary of attributes for the object.
    """

    model_config = ConfigDict(
        extra='forbid',
    )
    field_include: Optional[List[str]] = Field(
        None,
        alias='$include',
        description='A reference to another schema for attributes to include.',
    )


class Object1(BaseModel):
    """
    An object is a collection of contextually related attributes, usually representing an entity, and may include other objects. Each object is also a data type in OCSF. Examples of object data types are Process, Device, User, Malware and File.
    """

    field_deprecated: Optional[deprecated.Deprecated] = Field(None, alias='@deprecated')
    description: str = Field(..., description='A concise description of the object.')
    caption: str = Field(
        ..., description='A short, human friendly name for the object.'
    )
    name: constr(pattern=r'^[a-z0-9_]*$') = Field(
        ...,
        description='A name of the object. It must be a unique name. The name is all lower case letters, combine words using underscore.',
    )
    extends: Optional[str] = Field(
        None, description='An object that this one extends from.'
    )
    observable: Optional[observable.Observable] = None
    constraints: Optional[Constraints] = Field(
        None, description='Constraints that apply to the attribute requirements.'
    )
    profiles: Optional[List[str]] = Field(
        None, description='The list of profiles used to create the event.'
    )
    attributes: Attributes = Field(
        ..., description='A dictionary of attributes for the object.'
    )


class Object2(BaseModel):
    """
    An object is a collection of contextually related attributes, usually representing an entity, and may include other objects. Each object is also a data type in OCSF. Examples of object data types are Process, Device, User, Malware and File.
    """

    field_deprecated: Optional[deprecated.Deprecated] = Field(None, alias='@deprecated')
    description: Optional[str] = Field(
        None, description='A concise description of the object.'
    )
    caption: Optional[str] = Field(
        None, description='A short, human friendly name for the object.'
    )
    name: Optional[constr(pattern=r'^[a-z0-9_]*$')] = Field(
        None,
        description='A name of the object. It must be a unique name. The name is all lower case letters, combine words using underscore.',
    )
    extends: str = Field(..., description='An object that this one extends from.')
    observable: Optional[observable.Observable] = None
    constraints: Optional[Constraints] = Field(
        None, description='Constraints that apply to the attribute requirements.'
    )
    profiles: Optional[List[str]] = Field(
        None, description='The list of profiles used to create the event.'
    )
    attributes: Optional[Attributes] = Field(
        None, description='A dictionary of attributes for the object.'
    )


class Object(RootModel[Union[Object1, Object2]]):
    root: Union[Object1, Object2] = Field(
        ...,
        description='An object is a collection of contextually related attributes, usually representing an entity, and may include other objects. Each object is also a data type in OCSF. Examples of object data types are Process, Device, User, Malware and File.',
        title='Object',
    )
