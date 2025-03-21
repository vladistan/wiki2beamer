#!/usr/bin/env python3

"""Command-line interface for wiki2beamer."""

import sys

from .main import main


def cli():
    """Entry point for the command-line interface."""
    sys.exit(main())


if __name__ == "__main__":
    cli()
