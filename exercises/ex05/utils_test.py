"""Unit tests for Utils."""
___author___ = "730386998"

from exercises.ex05.utils import only_evens, concat, sub


def test_empty_evens() -> None:
    """Testing empty list for only_evens."""
    test_list: list[int] = [1, 1, 1]
    assert only_evens(test_list) == []


def test_many_evens() -> None:
    """Testing the only_evens function."""
    test_list: list[int] = [1, 2, 3]
    assert only_evens(test_list) == [2]


def test_many_evens_again() -> None:
    """Testing the only_evens function again."""
    test_list: list[int] = [2, 4, 7]
    assert only_evens(test_list) == [2, 4]


def test_empty_concat() -> None:
    """Testing empty list for concat."""
    test_list1: list[int] = []
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == []


def test_many_concact() -> None:
    """Testing the concat function."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [7, 8, 9]
    assert concat(test_list1, test_list2) == [1, 2, 3, 7, 8, 9]


def test_many_concat_again() -> None:
    """Testing the concact function again."""
    test_list1: list[int] = [4, 5, 6]
    test_list2: list[int] = [3, 8, 1]
    assert concat(test_list1, test_list2) == [4, 5, 6, 3, 8, 1]


def test_empty_sub() -> None:
    """Testing empty list for sub."""
    a_list: list[int] = []
    assert sub(a_list, 1, 3) == []


def test_many_sub() -> None:
    """Testing the sub function."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_many_sub_again() -> None:
    """Testing the sub function again."""
    a_list: list[int] = [55, 66, 77, 88, 99]
    assert sub(a_list, 1, 4) == [66, 77, 88]
    