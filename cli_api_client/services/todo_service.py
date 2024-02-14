from injector import inject
from cli_api_client.services.api_service import ApiService

class TodoService:
    base_url = f"https://jsonplaceholder.typicode.com/todos"

    @inject
    def __init__(self, api_service: ApiService):
        self.api_service = api_service

    def get_todos(self):
        url = f"{self.base_url}/"
        response = self.api_service.make_request("GET", url)
        # Process and return the response
        return response.json() if response else None

    def get_todo(self, id):
        url = f"{self.base_url}/{id}"
        response = self.api_service.make_request("GET", url)
        # Process and return the response
        return response.json() if response else None

    def get_todos_range(self, count, start=1, step = 2):
        todos = []
        odd_range = range(start, (count * 2) + 1, step)
        
        for idx in odd_range:
            todo = self.get_todo(idx)
            
            if todo:
                todos.append(todo)
            
        return todos if todos else None

