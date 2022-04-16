# Pony stubs

Python type hint stubs for [Pony ORM](https://github.com/ponyorm/pony)

**NOTE:** This project is still very much a WIP, the types shouldn't be expected to be anywhere close to completion.

## Goals
1. Provide type hints for Pony ORM that support both MyPy and Pyright on their strictest modes
2. Integrate the contents of this package into the official Pony ORM repository (self-deprecation)
3. Focus primarily on the aspects that users of Pony ORM most often run into (defining models, querying them etc.)

## Progress so far
1. Model fields should get dynamically typed correctly by using `Required`, `Set` etc.
2. Querying models (without using attribute lifting) should be well typed

## Development
The development environment for this package requires `poetry` (https://python-poetry.org/docs/master/#installing-with-the-official-installer)

Using VSCode as the editor is recommended!

### Setting up the repo
1. Clone the repo
    - `git clone git@github.com:Jonesus/pony-stubs.git`
2. Install dependencies
    - `poetry install`
3. Install commit hooks
    - `poetry run pre-commit install --install-hooks`
4. Type ahead!

## Contributing
Contributions are always most welcome! Please run the pre-commit hooks before setting up a pull request, and in case the Github actions fail, please try to fix those issues so the review itself can go as smoothly as possible

## License
This project is licensed under the MIT license (see LICENSE.md)
