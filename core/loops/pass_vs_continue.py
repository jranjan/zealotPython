# (c) Copyright 2018 Hewlett Packard Enterprise Development LP
"""request module."""

import logging
import uuid
import random
from collections import defaultdict
from datetime import MINYEAR, datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import time

def f():
    a = 39
    for i in range(10):
        if a == 3:
            print("3")
        elif a == 9:
            print("9")
        else:
            pass
        print("After continue")



if __name__ == "__main__":
    f()
