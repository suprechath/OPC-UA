#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from opcua.tools import uals


if __name__ == "__main__":
    uals()