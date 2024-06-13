FROM python:3.12
# Set the working directory in the container
WORKDIR /app

# Create a non-root user with no password
# 'user' can be replaced with a username of your choice
RUN useradd -m me

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Change ownership of the /app directory to the non-root user
RUN chown -R user:user /app

# Switch to non-root user
USER me

# Specify the port the app runs on
EXPOSE 8000