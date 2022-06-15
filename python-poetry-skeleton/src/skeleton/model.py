"""Domain models."""

from dataclasses import dataclass


@dataclass
class User:
    """User model."""

    name: str
