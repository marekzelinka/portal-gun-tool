import typer

from portal_gun_tool.gun.reload import app as reload_app
from portal_gun_tool.gun.shoot import app as shoot_app

app = typer.Typer()

app.add_typer(shoot_app)
app.add_typer(reload_app)
