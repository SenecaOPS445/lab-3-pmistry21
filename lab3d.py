#!/usr/bin/env python3
# Author ID: pmistry21@myseneca.ca

import os

def free_space():
    # Launches the Linux command: df -h | grep '/$' | awk '{print $4}' using os.system().
    command = "df -h | grep '/$' | awk '{print $4}'"
    result = os.popen(command).read().strip()
    # Returns a string in utf-8 format with newline characters stripped.
    return result.encode('utf-8').decode('utf-8').strip('\n')

if __name__ == "__main__":
    # Prints the free disk space.
    print(free_space())