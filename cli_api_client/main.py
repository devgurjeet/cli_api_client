# main.py

import click
from di.injector import configure_injector

# Configuring the dependency injection
configure_injector()

# Importing commands
from commands.todo_commands import todos

# Adding commands to the main CLI
@click.group()
def cli():
    pass

cli.add_command(todos)

if __name__ == '__main__':
    cli()
