import typer.testing

from portal_gun_tool.main import app


def test_reload_command(runner: typer.testing.CliRunner):
    result = runner.invoke(app, ["gun", "reload"])

    assert result.exit_code == 0
    assert "Reloading portal gun" in result.stdout


def test_shoot_command(runner: typer.testing.CliRunner):
    result = runner.invoke(app, ["gun", "shoot"])

    assert result.exit_code == 0
    assert "Shooting portal gun" in result.stdout
