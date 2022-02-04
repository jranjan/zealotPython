# (c) Copyright 2018 Hewlett Packard Enterprise Development LP
"""request module."""

import logging
import uuid
import random


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import time


pf9_credentials = {
    "clients": dict()
}

def add_v1():
    pf9_credentials["clients"] = random.randint(0, 1000)

def add_versioned_clients(version):
    client_ver = 'clients' + '_' + str(version)
    pf9_credentials[client_ver] = random.randint(0, 10)

if __name__ == "__main__":
    print(pf9_credentials)
    print(str('.' * 60))
    add_v1()
    print(pf9_credentials)
    print(str('.' * 60))
    add_versioned_clients('v1')
    print(pf9_credentials)
    print(str('.' * 60))
    add_versioned_clients('v2')
    print(pf9_credentials)
    print(str('.' * 60))
    add_versioned_clients('v3')
    print(pf9_credentials)
    print(str('.' * 60))
    add_versioned_clients('v4')
    print(pf9_credentials)
