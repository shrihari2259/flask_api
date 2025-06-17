# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /step ahead tasks

# Copy all files into the container
COPY . .

# Install required Python packages
RUN pip install -r requirements.txt

# Expose Flask's default port
EXPOSE 5000

# Run your specific Flask file
CMD ["python", "T11 query and path.py"]
