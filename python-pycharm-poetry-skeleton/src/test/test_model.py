from model import User


def test_user() -> None:
    assert User(name="Yu").name == "Yu"
