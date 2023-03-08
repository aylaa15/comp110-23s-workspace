"""Challenge Question 2 - for... in... loops"""

def sum(xs: list[float]) -> float:
    """return sum of all elements in xs"""

    sum_total: float = 0.0
    for elem in xs:
        sum_total += elem
    return sum_total