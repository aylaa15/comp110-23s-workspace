"""EX07 - Dictionary Functions."""
___author___ = "730386998"

def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Returns a dict of str that inverts the keys and the values."""
    output: dict[str, str] = {}

    for key in dictionary:
        if dictionary[key] in output:
            raise KeyError("KeyError")
        output[dictionary[key]] = key
    return output

def favorite_color(color: dict[str, str]) -> str:
    """Returns a str which is the color that appears most frequently."""
    count: dict[str, int] = {}

    for elem in color:
        if color[elem] in count:
            count[color[elem]] += 1
        else:
            count[color[elem]] = 1
    
    max_count: int = 0
    color: str = ""
    for key in count:
        if count[key] > max_count:
            max_count = count[key]
            color = key
    return color

def count(values: list[str]) -> dict[str, int]:
    """Returns a dict where each key is a unique value in the list and each value associated is the count of the number of times that value appeared in the input list."""
    result = {}

    for elem in values:
        if elem in result:
            result[elem] += 1
        else:
            result[elem] = 1
    return result