import typer.testing

from portal_gun_tool import app


def test_version_callback(runner: typer.testing.CliRunner):
    result = runner.invoke(app, ["--version"])

    assert result.exit_code == 0
    assert "portal_gun_tool version" in result.stdout

    import re

    assert re.search(r"\d+\.\d+\.\d+", result.stdout)
