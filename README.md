# tatsuyaml

A YAML parser built with [TatSu](https://github.com/neogeny/TatSu), a Python library for parsing expression grammars.

## Features

- Parse YAML content using TatSu's PEG parser
- Interactive REPL with command history
- File-based parsing via CLI

## Requirements

- Python 3.10

## Installation

```bash
pip install tatsuyaml
```

### Development Setup

Clone the repository and install in editable mode:

```bash
git clone https://github.com/conao3/python-tatsu-yaml.git
cd python-tatsu-yaml

python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Usage

### Interactive REPL

Start the interactive REPL by running:

```bash
tatsuyaml
```

This opens a prompt where you can enter YAML content and see the parsed output. Command history is saved to `~/.tatsuyaml_history`.

### Parse a File

Parse a YAML file directly:

```bash
tatsuyaml -i path/to/file.yaml
```

## License

See [LICENSE](LICENSE) for details.
