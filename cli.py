import click
from report import run_scan

@click.group()
def cli():
    pass

@cli.command()
def scan():
    """Scan system health"""
    run_scan()

if __name__ == "__main__":
    cli()
