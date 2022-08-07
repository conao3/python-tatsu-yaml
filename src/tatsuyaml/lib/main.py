def READ(x: str) -> str:
    return x


def EVAL(x: str, env: dict) -> str:
    return x


def PRINT(x: str) -> str:
    return x


def rep(x: str) -> str:
    return PRINT(EVAL(READ(x), {}))
