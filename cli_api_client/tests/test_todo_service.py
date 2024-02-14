import pytest
from unittest.mock import MagicMock, patch
from cli_api_client.services.todo_service import TodoService

@pytest.fixture
def api_service_mock():
    return MagicMock()

@pytest.fixture
def todo_service(api_service_mock):
    return TodoService(api_service_mock)

def test_get_todos_success(todo_service, api_service_mock):
    # Mock the ApiService's make_request method to return a successful response
    api_service_mock.make_request.return_value = MagicMock(json=lambda: [{'id': 1, 'title': 'Todo 1'}])

    # Call the method under test
    result = todo_service.get_todos()

    # Assertions
    assert result is not None
    assert len(result) == 1
    assert result[0]['id'] == 1
    assert result[0]['title'] == 'Todo 1'

def test_get_todos_failure(todo_service, api_service_mock):
    # Mock the ApiService's make_request method to return None (simulating a failed API request)
    api_service_mock.make_request.return_value = None

    # Call the method under test
    result = todo_service.get_todos()

    # Assertions
    assert result is None

@patch.object(TodoService, 'get_todo')  # Mock the get_todo method for testing get_todos_range
def test_get_todos_range_success(get_todo_mock, todo_service):
    # Mock the get_todo method to return a successful response
    get_todo_mock.return_value = {'id': 1, 'title': 'Todo 1'}

    # Call the method under test
    result = todo_service.get_todos_range(count=3)

    # Assertions
    assert result is not None
    assert len(result) == 3
    assert result[0]['id'] == 1
    assert result[0]['title'] == 'Todo 1'
