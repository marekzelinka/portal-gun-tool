import typer

app = typer.Typer()


@app.command()
def reload() -> None:
    """
    Reload the portal gun
    """
    typer.echo("Reloading portal gun")
