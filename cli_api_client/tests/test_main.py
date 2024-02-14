import click
from click.testing import CliRunner
from cli_api_client.main import cli

def test_cli_runs():
    runner = CliRunner()
    result = runner.invoke(cli)

    assert result.exit_code == 0
    assert 'Usage: cli [OPTIONS] COMMAND [ARGS]...' in result.output

def test_todos_command():
    runner = CliRunner()
    
    # Assuming your 'todos' command has a 'list' subcommand
    result = runner.invoke(cli, ['todos', 'all'])

    # Assert that the command ran successfully
    assert result.exit_code == 0

   
    # Add more assertions based on the expected output of the 'todos all' command
    assert 'delectus aut autem' in result.output

def test_todos_ID_command():
    runner = CliRunner()
    
    # Assuming your 'todos' command has a 'list' subcommand
    result = runner.invoke(cli, ['todos', 'id', '2'])

    # Assert that the command ran successfully
    assert result.exit_code == 0


    # Add more assertions based on the expected output of the 'todos ID 2' command
    assert 'quis ut nam facilis et officia qui' in result.output
    
    # Add more assertions based on the expected output of the 'todos ID 2' command
    assert 'False' in result.output
