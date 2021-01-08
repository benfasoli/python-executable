# Python standalone executables

This demonstrates how to use GitHub Actions to build standalone python executables across multiple operating systems.

The sample [app/main.py](app/main.py) uses the fantastic [typer](https://typer.tiangolo.com/) package to build a CLI executable written in Python.

The [workflow](.github/workflows/build.yaml) installs necessary dependencies, ensures `pytest` passes, bundles a standalone executable using [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/usage.html), and uploads build artifacts.
