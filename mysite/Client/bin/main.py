#!/usr/bin/python3
import os
import sys

from mysite.Client.core.handler import ArgvHandler

BASE_DIR = os.path.dirname(os.getcwd())
sys.path.append(BASE_DIR)


if __name__ == '__main__':

    ArgvHandler(sys.argv)