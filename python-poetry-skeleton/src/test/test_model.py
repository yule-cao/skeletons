"""Unit test for domain models."""

from model import User


def test_user() -> None:
    """Test user model."""
    assert User(name="Yu").name == "Yu"
