def split(A: list, separator: list) -> list[list]:
    if not A:
        return []

    sep = set(separator)
    res = [[]]

    for a in A:
        if a not in sep:
            res[-1].append(a)
        else:
            res.append([])

    return res
