from typer import Typer, echo

app = Typer()


@app.callback()
def callback() -> None:
    """
    Awesome Portal Gun
    """


@app.command()
def shoot() -> None:
    """
    Shoot the portal gun
    """
    echo("Shooting portal gun")


@app.command()
def reload() -> None:
    """
    Reload the portal gun
    """
    echo("Reloading portal gun")
