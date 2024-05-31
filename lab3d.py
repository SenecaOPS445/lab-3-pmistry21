#!/usr/bin/env python3

# Author ID: pmistry21@myseneca.ca

import os

# Finds free space.
def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    result = os.popen(command).read().strip()
    return result

# Prints the free space.
if __name__ == "__main__":
    print(free_space())