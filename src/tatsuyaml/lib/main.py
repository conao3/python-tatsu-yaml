from . import parser


parser_ = parser.Parser()


def READ(x: str) -> list[str]:
    return parser_.read(x)


def EVAL(x: list[str], env: dict) -> str:
    return str(x)


def PRINT(x: str) -> str:
    return x


def rep(x: str) -> str:
    return PRINT(EVAL(READ(x), {}))
