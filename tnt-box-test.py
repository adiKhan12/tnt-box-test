# test Script to test if Docker Container from list is runnig

import docker
import os
import time
import sys


def docker_test():
    # Test 1 - Check if Docker Container is running
    
    print('     TEST 1: Check if Docker Container is running')

    # Create Doker Client 
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
            print(f'Docker Container: {container} is running...')
            time.sleep(1)
        else:
            print(f'Docker Container: {container} is not running...')
            time.sleep(1)
            break
    return 

def dpkg_test():
    # Test 2 - Check if Docker is installed
    print('     TEST 2: Check if Required Packages are installed...')
    # Test if the list of required deb packages is installed
    DEB_PACKAGES = ['puppet-agent', 'htpdate', 'libisccfg-export163', 'libirs-export161','isc-dhcp-server', 'net-tools', 'libblas3', 'liblinear4', 'liblua5.3-0', 'lua-lpeg', 'nmap-common', 'nmap', 'fping', 'atop', 'iotop', 'ncdu', 'tree', 'libssh2-1', 'mc-data', 'mc', 'libonig5', 'libjq1', 'jq', 'jo', 'iperf', 'pv', 'socat', 'conntrack', 'zip', 'unzip', 'liblockfile-bin', 'liblockfile1', 'ssl-cert', 'nullmailer', 'bsd-mailx', 'libmhash2', 'aide', 'aide-common', 'libseccomp2', 'containerd.io', 'docker-ce-cli', 'docker-ce', 'libsensors-config', 'libsensors5', 'chrony']

    CHECK_PARA = 'installed'

    for package in DEB_PACKAGES: 
        # Get package status
        package_status = os.popen('dpkg -s ' + package + ' | sed -e "s/Status: install ok //g"').read()
        # Check if package is installed
        if CHECK_PARA in package_status:
            print(f'Debian Package: {package} is installed...')
            time.sleep(1)
        else:
            print(f'Debian Package: {package} is not installed...')
            time.sleep(1)
            break
    return

print('             ......TNT-BOX TESTING......             ')

docker_test()
dpkg_test()


