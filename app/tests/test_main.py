from typer.testing import CliRunner

from ..main import app


runner = CliRunner()


def test_hello_world():
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert 'Hello world!' in result.stdout


def test_hello_ben():
    result = runner.invoke(app, 'Ben')
    assert result.exit_code == 0
    assert 'Hello Ben!' in result.stdout
