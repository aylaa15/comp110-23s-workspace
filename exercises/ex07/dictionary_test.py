"""Dictionary tests for Dictionary Functions."""
___author___ = "730386998"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_empty_invert() -> None:
    """Testing empty dict for invert."""
    test_list: dict[str, str] = {}
    assert invert(test_list) == {}


def test_many_invert() -> None:
    """Testing the invert function."""
    test_list: dict[str, str] = {'happy': 'sad'}
    assert invert(test_list) == {'sad': 'happy'}


def test_many_invert_again() -> None:
    """Testing the invert function again."""
    test_list: dict[str, str] = {'dog': 'cat'}
    assert invert(test_list) == {'cat': 'dog'}


def test_empty_favorite_color() -> None:
    """Testing empty dict for favorite color."""
    test_list: dict[str, str] = {}
    color: str = ""
    assert favorite_color(color) == ""


def test_many_favorite_color() -> None:
    """Testing the favorite color function."""
    test_list: dict[str, str] = {'Alex': 'yellow', 'Mark': 'pink', 'John': 'yellow'}
    assert favorite_color(test_list) == 'yellow'


def test_many_favorite_color_again() -> None:
    """Testing the favorite color function again."""
    test_list: dict[str, str] = {'Ayla': 'purple', 'Grant': 'blue', 'Madison': 'purple'}
    assert favorite_color(test_list) == 'purple'


def test_empty_count() -> None:
    """Testing empty dict for count."""
    test_list: list[str, int] = {}
    assert count(test_list) == {}


def test_many_count() -> None:
    """Testing the count function."""
    test_list: list[str, int] = ['apple', 'strawberry', 'apple']
    assert count(test_list) == {'apple': 2, 'strawberry': 1}


def test_many_count_again() -> None:
    """Testing the count function again."""
    test_list: list[str, int] = ['blue', 'yellow', 'blue', 'green', 'blue', 'purple']
    assert count(test_list) == {'blue': 3, 'yellow': 1, 'green': 1, 'purple': 1}

    