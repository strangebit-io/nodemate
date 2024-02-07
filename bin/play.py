from sys import argv
import argparse
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
print(os.path.dirname(SCRIPT_DIR))
from lib.nodebook.nodebook import NodeBook

parser = argparse.ArgumentParser(
                    prog='NodeMate',
                    description='Telecommunication devices provisioning tool')

parser.add_argument('filename')
args = parser.parse_args()

nodebook = NodeBook()
nodebook.load(args.filename)