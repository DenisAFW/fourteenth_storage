# На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.
from pathlib import Path
import pytest
# Не использовал свой файл, потому что он мне не нравится =)
from DZ_prepoda import User, Project, AccessError, LevelError


@pytest.fixture
def new_set():
    data = {
        User(name='Admin', id=999, access_level=1),
        User(name='user', id=246, access_level=3),
        User(name='Alex', id=123, access_level=3)
    }
    return data


@pytest.fixture
def good_user():
    return User(name='user', id=246, access_level=3)


def test_load(new_set):
    project = Project()
    result = project.load_users_from_json(Path('test_bd.json'))
    assert result == new_set


def test_enter(good_user):
    project = Project()
    project.load_users_from_json(Path('test_bd.json'))


def test_no_enter():
    project = Project()
    project.load_users_from_json(Path('test_bd.json'))
    with pytest.raises(AccessError):
        project.login('qwerty', 246)


def test_add_user(new_user):
    project = Project()
    project.load_users_from_json(Path('test_bd.json'))
    project.login('user', 246)
    result = project.add_user('new', 52534, 7)
    assert new_user == result


def test_not_add_user():
    project = Project()
    project.load_users_from_json(Path('test_bd.json'))
    project.login('user', 246)
    with pytest.raises(LevelError,
                       match='Нельзя добавить пользователя с уровнем 1'):
        project.add_user('new', 52534, 1)


if __name__ == '__main__':
    pytest.main('-vv')
