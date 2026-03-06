import typer

app = typer.Typer()


@app.command()
def shoot() -> None:
    """
    Shoot the portal gun
    """
    typer.echo("Shooting portal gun")
