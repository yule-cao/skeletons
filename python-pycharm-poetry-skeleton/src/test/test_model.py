from model import User


def test_user():
    assert User(name="Yu").name == "Yu"
