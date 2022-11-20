# test Script to test if Docker Container from list is runnig

import docker
import sys

# Get list of containers
client = docker.from_env()

# Get Container Names only
containers = client.containers.list()

# Get Container Names only
container_names = [container.name for container in containers]

# Display Container Names
print("Container Names: ", container_names)