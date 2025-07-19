FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install system dependencies for OpenCV and other CV libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt if it exists
COPY requirements.txt ./

# Install Python dependencies if requirements.txt exists
RUN if [ -f requirements.txt ]; then pip install --upgrade pip && pip install -r requirements.txt; fi

# Copy the rest of the project files
COPY . .

# Default to bash for interactive use
CMD ["bash"] 