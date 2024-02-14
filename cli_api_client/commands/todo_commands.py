import click
from di.injector import configure_injector
from services.todo_service import TodoService
from utlis.display_formatter import DisplayFormatter

injector = configure_injector()

display_fields = [ 'id', 'title', 'completed']


@click.group()
def todos():
   pass

@todos.command()
def all():
    """List all todos"""
    todo_service = injector.get(TodoService)
    todos = todo_service.get_todos()
    #click.echo(todos)
    DisplayFormatter.display_table(todos, display_fields)

@todos.command()
@click.argument('id', nargs=1)
def id(id: int):
    """Get Todo by Id"""
    items = []

    todo_service = injector.get(TodoService)
    todo = todo_service.get_todo(id)

    items.append(todo)
    DisplayFormatter.display_table(items, display_fields)


@todos.command()
@click.argument('count', nargs=1)
def odd(count: int):
    """Get range of todo with ODD id"""
    todo_service = injector.get(TodoService)
    todos = todo_service.get_todos_range(int(count))
   
    DisplayFormatter.display_table(todos, display_fields)


@todos.command()
@click.argument('count', nargs=1)
def even(count: int):
    """Get range of todo with EVEN ids"""
    todo_service = injector.get(TodoService)
    todos = todo_service.get_todos_range(int(count), 2)
   
    DisplayFormatter.display_table(todos, display_fields)
