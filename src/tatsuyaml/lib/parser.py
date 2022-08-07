import tatsu

class Parser:
    def __init__(self):
        with open("./src/tatsuyaml/lib/grammar.ebnf") as f:
            grammar = f.read()

        self.model = tatsu.compile(grammar)

    def read(self, inpt: str):
        return self.model.parse(inpt)
