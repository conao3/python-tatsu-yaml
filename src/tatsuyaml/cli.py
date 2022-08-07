import argparse
import logging
import pathlib
import readline

from . import lib


logger = logging.getLogger(__name__)


def repl() -> None:
    readline.set_history_length(1000)
    history_file = pathlib.Path("~/.tatsuyaml_history").expanduser()

    try:
        readline.read_init_file(history_file)
    except FileNotFoundError:
        history_file.touch()

    while True:
        try:
            inpt = input("tatsuyaml> ")
            readline.add_history(inpt)
        except EOFError:
            break

        try:
            print(lib.main.rep(inpt))
        except Exception:
            logger.exception("Exception")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='YAML parser powered by TatSu')
    parser.add_argument('-i', '--input', help='Input file')

    return parser.parse_args()


def main():
    args = parse_args()

    if not args.input:
        repl()
        return

    with open(args.input) as f:
        inpt = f.read()

    lib.main.rep(inpt)
