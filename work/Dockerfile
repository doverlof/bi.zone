# Use the official Python slim image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /work

# Copy the requirements file into the container
COPY requirements.txt /work/requirements.txt

# Install the dependencies from the requirements file
RUN pip install --no-cache-dir -r /work/requirements.txt

# Copy the rest of the project files into the container
COPY . /work

# Set the PYTHONPATH so the project modules can be discovered
ENV PYTHONPATH=/work

# Expose the port Django will run on
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]