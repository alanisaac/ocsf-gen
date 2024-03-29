# generated by datamodel-codegen:
#   filename:  event.json
#   timestamp: 2024-02-16T20:53:52+00:00

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, conint


class Category(Enum):
    """
    The category that the event belongs to.
    """

    system = 'system'
    findings = 'findings'
    iam = 'iam'
    network = 'network'
    discovery = 'discovery'
    application = 'application'
    other = 'other'


class Event(BaseModel):
    """
    Event classes are particular sets of attributes and objects representing a log line or telemetry submission at a point in time. Event classes have semantics that describe what happened: either a particular activity, disposition or both.
    """

    associations: Optional[Dict[str, List[str]]] = Field(
        None,
        description="Associations indicate attributes in a schema which 'go together'. For example, if a schema has multiple users and multiple endpoints, associations can indicate which user attribute goes with which endpoint.",
    )
    category: Optional[Category] = Field(
        None, description='The category that the event belongs to.'
    )
    uid: Optional[conint(ge=0, le=999)] = Field(
        None,
        description='A unique identifier for this event, must be unique within the category.',
    )
