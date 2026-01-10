FROM mcr.microsoft.com/devcontainers/python:3.12-trixie

# Set the working directory
WORKDIR /workspace

# Install any necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies if needed
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# Set the default command
CMD ["bash"]