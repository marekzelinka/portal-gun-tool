import unittest.mock

import pytest
import typer.testing

from portal_gun_tool import app
from portal_gun_tool.main import version_callback


def test_version_option(runner: typer.testing.CliRunner) -> None:
    with (
        unittest.mock.patch("portal_gun_tool.main.__project_name__", new="fake-tool"),
        unittest.mock.patch("portal_gun_tool.main.get_version") as mocked_version,
    ):
        mocked_version.return_value = "9.9.9-alpha"

        result = runner.invoke(app, ["--version"])

        assert result.exit_code == 0
        assert "fake-tool version 9.9.9-alpha" in result.stdout

        # Ensure the function was actually called once
        mocked_version.assert_called_once()


def test_version_callback() -> None:
    assert version_callback(False) is None

    with pytest.raises(typer.Exit):
        version_callback(True)
