#!/usr/bin/env python3

import glob
import re
import os
import subprocess
import time
import argparse

try:
    raw_input
except NameError:
    raw_input = input


source_files = []
project_files = source_files + [] #Additional Files

parser = argparse.ArgumentParser(description='Project0 Pre-Upload Script')
parser.add_argument('directory', metavar='D', type=str,
                   help='Submission Directory')
parser.add_argument('course', metavar='C', type=str,
                   help='Course')
parser.add_argument('assignment', metavar='A', type=str,
                   help='Assignment')
parser.add_argument('username', metavar='U', type=str,
                   help='Username')


def main ():
    args = parser.parse_args()
    print("Hi thanks for submitting project[1]!")


if __name__ == '__main__':
    main()
 