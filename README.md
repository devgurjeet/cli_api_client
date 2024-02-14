# Todo CLI Client

**Todo CLI Client** is a command-line interface (CLI) client for managing todos using a remote API.

## Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Tests](#tests)
- [Docker](#docker)

## Project Structure

```plaintext
cli_api_client/
|-- commands/
|   |-- __init__.py
|   |-- todo_commands.py
|-- di/
|   |-- __init__.py
|   |-- injector.py
|-- services/
|   |-- __init__.py
|   |-- api_service.py
|   |-- authentication_service.py
|   |-- todo_service.py
|-- tests/
|   |-- __init__.py
|   |-- test_main.py
|   |-- test_todo_service.py
|-- utlis/
|   |-- __init__.py
|   |-- display_formatter.py
|-- __init__.py
|-- main.py

```

## Installation

Clone the repository:

   ```
   git clone https://github.com/devgurjeet/cli_api_client.git
   cd cli_api_client
   ```
  
## Install dependencies:

```pip install -r requirements.txt```

## Setup

```export PYTHONPATH=/path/to/your/project_root:$PYTHONPATH```

## Usage

## Running the CLI
> Execute the main.py script to run the CLI:

```
python main.py
```
## Exercise
> command line tool that consumes the first 20 even numbered TODO's :
> ```python main.py todos even 20```


## Available Commands

1. **todos**: Main command for managing todos.
2. **all**: List all todos.
3. **id <id>**: Get a todo by ID.
4. **odd <count>**: Get a range of todos with odd IDs.
5. **even <count>**: Get a range of todos with even IDs.

## Tests
> Run tests using pytest:

```pytest tests/```

## Docker

#### Docker Build 
```docker build -t cli-api-client .``` 

#### Docker run
``` docker run cli-api-client```

#### Verify the Container Contents
```docker run -it --entrypoint /bin/bash cli-api-client```
