### Pysubstitutor

[![MIT License](https://img.shields.io/github/license/crsiebler/pysubstitutor)](https://github.com/crsiebler/pysubstitutor/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/pysubstitutor)](https://pypi.org/project/pysubstitutor/)
[![Build Status](https://github.com/crsiebler/pysubstitutor/actions/workflows/test.yml/badge.svg)](https://github.com/crsiebler/pysubstitutor/actions)
[![Python Versions](https://img.shields.io/pypi/pyversions/pysubstitutor)](https://pypi.org/project/pysubstitutor/)
[![GitHub last commit](https://img.shields.io/github/last-commit/crsiebler/pysubstitutor.svg?style=flat)](https://github.com/crsiebler/pysubstitutor/commits/main)
[![GitHub issues](https://img.shields.io/github/issues/crsiebler/pysubstitutor)](https://github.com/crsiebler/pysubstitutor/issues)
[![GitHub stars](https://img.shields.io/github/stars/crsiebler/pysubstitutor)](https://github.com/crsiebler/pysubstitutor/stargazers)
[![Twitter Follow](https://img.shields.io/twitter/follow/CorySiebler.svg?style=social)](https://twitter.com/CorySiebler)

# Description

`pysubstitutor` is a Python package designed to convert text substitution files between different formats. It supports reading and exporting text substitutions in formats such as Apple `.plist`, Gboard `.gboard`, and Markdown `.md`. The package is modular, extensible, and includes utilities for handling file conversions and zipping output files.

This tool is particularly useful for managing and migrating text substitution dictionaries across platforms or exporting them for documentation purposes.

### Features

- **Plist to Gboard Conversion**: Convert Apple `.plist` files to Gboard `.gboard` format.
- **Markdown Export**: Export text substitutions to a Markdown table for easy documentation.
- **Extensible Handlers**: Easily add support for new file formats by implementing custom handlers.
- **Command-Line Interface**: Run the tool via the command line with customizable input and output paths.
- **Dockerized Environment**: Run the application and tests in a Docker container for consistency.

### Installation

#### Using Conda

1. Create the conda environment:
   ```bash
   conda env create -f environment.yml
   ```

2. Activate the environment:
   ```bash
   conda activate pysubstitutor
   ```

3. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

#### Using Docker

1. Build the Docker image:
   ```bash
   make build
   ```

2. Verify the Docker image is built:
   ```bash
   docker images
   ```

### Testing

Run the tests inside the Conda environment:
```bash
pytest tests
```

Or, run the tests inside the Docker container:
```bash
make test
```

### Test Coverage

**Prerequisites:** Ensure that the `coverage.py` tool is installed. It is included in the `environment.yml` file for the Conda environment and the Docker image. The commands below rely on this tool to generate and view coverage reports.

To generate and view test coverage results, use the following commands:

#### Generate Coverage Report
Run the following command to generate a coverage report:
```bash
make coverage
```

#### View Coverage Summary
To view the coverage summary in the terminal:
```bash
make coverage-report
```

#### View Coverage HTML
To generate and open an HTML report in your browser:
```bash
make coverage-html
```

The HTML report provides a detailed breakdown of the test coverage for each file in the project.

### Execution

Run the application inside the Docker container:
```bash
make run
```

Replace the `--input` and `--output` arguments in the `Makefile` if you need to customize the input and output file paths.
