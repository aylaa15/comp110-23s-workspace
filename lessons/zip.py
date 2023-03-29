"""CQ4 - Dict Function Writing."""

def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """returns a dict where keys are the items of the first list and the values are the corresponding items at the same index of the second list."""
    if len(keys) != len(values):
        return {}
