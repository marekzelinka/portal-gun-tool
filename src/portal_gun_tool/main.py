from typing import Annotated

import typer

from portal_gun_tool.config import __project_name__, get_version
from portal_gun_tool.gun import app as gun_app

app = typer.Typer()


app.add_typer(gun_app, name="gun")


def version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__project_name__} version {get_version()}")
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        bool | None, typer.Option(callback=version_callback, is_eager=True)
    ] = None,
) -> None:
    """
    Awesome Portal Gun
    """
