# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the entire project into the container at /app
COPY . .

# Set PYTHONPATH to include the project root
ENV PYTHONPATH /app:$PYTHONPATH

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV NAME cli_api_client

# Run main.py when the container launches
CMD ["python", "cli_api_client/main.py", "todos", "even", "20"]
