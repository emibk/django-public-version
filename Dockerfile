# syntax=docker/dockerfile:1
FROM python:3.9

# Open port 8000
EXPOSE 8000

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app

# Install the project dependecies
RUN pip3 install -r requirements.txt --no-cache-dir

# Copy the project code into the container
COPY . /app




# Run the Django server
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]