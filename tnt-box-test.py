# test Script to test if Docker Container from list is runnig

import docker
import sys


def docker_test():
    # Test 1 - Check if Docker Container is running
    # Get list of containers
    client = docker.from_env()

    # Containers names that should be tested if running
    TNT_BOX_CONTAINERS = ['tntnbox_configuration_app', 'chronograf', 'influxdb', 'telegraf', 'revproxy', 'telepresence']
    RUNNING = 'running'

    for container in TNT_BOX_CONTAINERS:
        # Get container
        container = client.containers.get(container)
        # Get container status
        container_status = container.status
        # Check if container is running
        if container_status == RUNNING:
            print('Container is running')
        else:
            print('Container is not running')
    return 


docker_test()


