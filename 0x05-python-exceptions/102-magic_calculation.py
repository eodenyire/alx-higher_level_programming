def magic_calculation(a, b):
    """
    Replicates the behavior of the provided Python bytecode.

    Args:
        a (int): First parameter.
        b (int): Second parameter.

    Returns:
        int: Result of the magic calculation.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except Exception:
            result = b + a
            break
    return result
