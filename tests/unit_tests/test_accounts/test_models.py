def test_create_user_method(new_user):
    assert not new_user.is_staff


def test_create_superuser_method(new_superuser):
    assert new_superuser.is_staff
    assert new_superuser.is_superuser


def test_string_representation(new_user):
    assert str(new_user) == f"{new_user.first_name} {new_user.last_name}"


def test_get_full_name_method(new_user):
    assert new_user.get_full_name() == f"{new_user.first_name} {new_user.last_name}"


def test_get_short_name_method(new_user):
    assert new_user.get_short_name() == new_user.first_name
