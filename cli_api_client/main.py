# main.py

import click
from cli_api_client.di.injector import configure_injector

# Configuring the dependency injection
configure_injector()

# Importing commands
from cli_api_client.commands.todo_commands import todos

# Adding commands to the main CLI
@click.group()
def cli():
    print("Todos Client.")

cli.add_command(todos)

if __name__ == '__main__':
    cli()
