def e(y: int = 3, makeList: bool = False):
    if makeList:
        return ["e" for e in range(y)]
    return "e" * y


def into_e(input):
    input_type = type(input)

    if input_type is str:
        return e(len(input))

    elif input_type is list:
        return e(len(input), makeList=True)

    elif input_type is tuple:
        return tuple(e(len(input), makeList=True))

    else:
        raise ValueError("Unsupported input type!")
