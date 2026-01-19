import click
import sys
from report import run_scan

if sys.platform.startswith("win"):
    import os
    os.system("")

@click.group()
def cli():
    pass

@cli.command()
def scan():
    """Scan system health"""
    run_scan()

if __name__ == "__main__":
    cli()
