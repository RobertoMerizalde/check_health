#!/usr/bin/env python3

import os
import sys


def check_reboot():
    """Returns True if the computer has a pending reboot"""
    # The OS will automatically create this file if the machine is expecting a reboot
    return os.path.exists("/run/reboot-required")



def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)



main()


