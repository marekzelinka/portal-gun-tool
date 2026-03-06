import pytest
from typer import testing


@pytest.fixture
def runner() -> testing.CliRunner:
    return testing.CliRunner()
